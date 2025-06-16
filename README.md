# Meeting Notes Generator

An AI-powered application that transcribes audio from meetings and generates summaries and action items.

## Features
- Audio file transcription
- Meeting summary generation
- Action items extraction
- Progress tracking
- Support for files up to 50MB

## Deployment Options

### Option 1: Web Deployment
1. Frontend (Streamlit):
   - Sign up for [Streamlit Cloud](https://streamlit.io/cloud)
   - Connect your GitHub repository
   - Deploy the frontend app

2. Backend (FastAPI):
   - Deploy to a cloud provider (e.g., Heroku, DigitalOcean, AWS)
   - Set up environment variables
   - Update the frontend API URL

### Option 2: Microsoft Teams App
1. Create a Teams app manifest
2. Package the application
3. Deploy to Teams

## Local Development
1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Start the backend:
```bash
cd backend
uvicorn main:app --host 0.0.0.0 --port 8000
```

3. Start the frontend:
```bash
cd frontend
streamlit run app.py
```

## Environment Variables
Create a `.env` file with:
```
BACKEND_URL=your_backend_url
```

## License
MIT 