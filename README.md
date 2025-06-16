# Audio Transcription App

A Python application that uses AI to transcribe meeting audio and generate summaries.

## Code Structure

### Backend (FastAPI)
- `main.py`: FastAPI server with endpoints:
  - `/transcribe`: Upload and process audio files
  - `/health`: Health check endpoint

### Frontend (Streamlit)
- `app.py`: Streamlit interface for:
  - File upload
  - Progress tracking
  - Results display

## Dependencies

### Core Dependencies
- streamlit==1.32.0
- fastapi==0.110.0
- uvicorn==0.27.1
- python-multipart==0.0.9
- requests==2.31.0
- python-dotenv==1.0.1

### Local Development Dependencies
- openai-whisper==20231117
- ollama==0.1.6

## Setup

1. Clone the repository
2. Install dependencies:
   - For local development: `pip install -r requirements-local.txt`
   - For deployment: `pip install -r requirements.txt`

## Environment Variables

Create a `.env` file:
```
BACKEND_URL=http://localhost:8000
```

## Local Development

1. Start the backend:
```bash
cd backend
uvicorn main:app --reload
```

2. Start the frontend:
```bash
streamlit run frontend/app.py
```

## License

MIT License
