# MinAnjalagar

MinAnjalagar is a small Flask web application that uses the Groq LLM to generate professional email drafts from a short subject and tone selection. It provides a clean UI, tone controls, copy/download features, and is ready to deploy to services like Render.

## Features
- Generate professional emails from a subject line
- Select tone: Professional, Friendly, Formal, Casual
- Copy generated email to clipboard
- Download generated email as a `.txt` file
- Production-ready with `gunicorn` and a `Procfile`

## Prerequisites
- Python 3.10+ (the project was developed with Python 3.11)
- A Groq API key (set as `GROQ_API_KEY`)

## Local setup
1. Create and activate a virtual environment (recommended):

```powershell
python -m venv .venv
.\\.venv\\Scripts\\Activate
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. Set your Groq API key (PowerShell example):

```powershell
$env:GROQ_API_KEY = "your-api-key-here"
```

4. Run the app:

```powershell
python app.py
# then open http://localhost:5000
```

## Production / Render deployment
The repository includes a `Procfile` and `render.yaml` to simplify deployment on Render.

On Render:
- Create a new Web Service and connect your repo
- Branch: `feature/ui-tamil` (or `main` if you prefer)
- Build command: `pip install -r requirements.txt`
- Start command: `gunicorn app:app --bind 0.0.0.0:$PORT --workers 2`
- Add an environment variable `GROQ_API_KEY` in the Render dashboard (mark it as secret)

## Environment variables
- `GROQ_API_KEY` — required. Your Groq API key.
- `FLASK_DEBUG` — optional. Set to `true` to enable debug mode locally.

## Files of interest
- `app.py` — Flask backend and API route `/generate-email`
- `templates/index.html` — main UI template
- `static/style.css` and `static/script.js` — frontend styles and scripts
- `requirements.txt` — Python dependencies (includes `gunicorn`)
- `Procfile` — start command for Gunicorn
- `render.yaml` — optional Render infra-as-code (replace repo URL before use)

## Notes
- Do not commit your API keys or other secrets to the repository. Use environment variables on your host (Render, Heroku, etc.).
- If you need help pushing to GitHub, configuring Render, or adding CI, I can assist.

---
Made with care — MinAnjalagar
