# AI Meeting Notes Generator (Whisper + LLaMA2)
This app lets you upload a recorded meeting and returns:
- A short summary
- Action items
- Full transcript
It uses:
- **Whisper** for transcription (locally, not via Ollama)
- **LLaMA2** via **Ollama** for summarization and task extraction
- **FastAPI** for the backend
- **Streamlit** for the frontend

## How to Run
1. Install requirements: `pip install -r requirements.txt`
2. Pull LLaMA2: `ollama pull llama2`
3. Run backend: `uvicorn backend.main:app --reload`
4. Run frontend: `streamlit run frontend/app.py`
