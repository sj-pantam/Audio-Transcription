# AI Meeting Notes Generator

An AI-powered application that transcribes audio from meetings and generates summaries and action items.

## Features
- Audio file transcription
- Meeting summary generation
- Action items extraction
- Progress tracking
- Support for files up to 50MB

## Technology Stack
- **Whisper** for transcription (locally, not via Ollama)
- **LLaMA3.2** via **Ollama** for summarization and task extraction
- **FastAPI** for the backend
- **Streamlit** for the frontend

## Local Development
1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Pull LLaMA3.2:
```bash
ollama pull llama3.2
```

3. Start the backend:
```bash
cd backend
uvicorn main:app --host 0.0.0.0 --port 8000
```

4. Start the frontend:
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
