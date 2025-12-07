from flask import Flask, render_template, request, jsonify
from groq import Groq
import os

app = Flask(__name__)

# Initialize Groq client
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    # Fail fast with a clear message when the key isn't set
    raise ValueError("GROQ_API_KEY environment variable not set")

client = Groq(api_key=api_key)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate-email', methods=['POST'])
def generate_email():
    data = request.json
    subject = data.get('subject', '')
    
    if not subject:
        return jsonify({'error': 'Subject is required'}), 400
    
    try:
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": "Welcome! You are an expert email writer. Create polished, professional Gmail emails based on the subject provided. Keep the tone professional yet friendly. The email should be concise but comprehensive."
                },
                {
                    "role": "user",
                    "content": f"Please write a professional email with the subject: {subject}"
                }
            ],
            temperature=1,
            # older/newer groq client bindings expect `max_tokens` rather than
            # `max_completion_tokens`. Use `max_tokens` which is widely accepted.
            max_tokens=1024,
            top_p=1,
            stream=False,
            stop=None
        )
        
        email_content = completion.choices[0].message.content
        return jsonify({'email': email_content})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Use PORT env var provided by hosting platforms (Render, Heroku, etc.)
    port = int(os.environ.get('PORT', 5000))
    # Allow overriding debug mode via FLASK_DEBUG env var (false by default)
    debug = os.environ.get('FLASK_DEBUG', 'false').lower() in ('1', 'true', 'yes')
    app.run(host='0.0.0.0', port=port, debug=debug)
