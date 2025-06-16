# AI Meeting Notes Generator

A Python application that uses AI to transcribe meeting audio and generate summaries.

## Code Structure

### Backend (`backend/main.py`)
- FastAPI server handling audio file uploads
- Whisper model for audio transcription
- LLaMA3.2 (via Ollama) for generating summaries and action items
- Endpoints:
  - `/transcribe`: Accepts MP3 files and returns transcript, summary, and action items
  - `/health`: Health check endpoint

### Frontend (`frontend/app.py`)
- Streamlit interface for file upload and results display
- Features:
  - Audio file upload (MP3)
  - Progress tracking
  - Summary and action items display
  - Full transcript view
  - Error handling

## Dependencies
```
fastapi==0.110.0
uvicorn==0.27.1
python-multipart==0.0.9
openai-whisper==20231117
ollama==0.1.6
requests==2.31.0
python-dotenv==1.0.1
streamlit==1.32.0
```

## Setup
1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Install LLaMA3.2:
```bash
ollama pull llama3.2
```

3. Run backend:
```bash
cd backend
uvicorn main:app --host 0.0.0.0 --port 8000
```

4. Run frontend:
```bash
cd frontend
streamlit run app.py
```

## Environment Variables
Create `.env` file:
```
BACKEND_URL=http://localhost:8000
```

## License
MIT
