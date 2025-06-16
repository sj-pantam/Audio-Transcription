import ollama
from fastapi import FastAPI, UploadFile, File, HTTPException
import tempfile as tmp
import whisper
from fastapi.responses import JSONResponse
import asyncio
from typing import Optional
import os
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model = whisper.load_model("base")

# Maximum file size (50MB)
MAX_FILE_SIZE = 50 * 1024 * 1024

# Supported audio formats
SUPPORTED_FORMATS = {
    'audio/mp3': '.mp3',
    'audio/mpeg': '.mp3',
    'audio/wav': '.wav',
    'audio/x-wav': '.wav',
    'audio/mp4': '.m4a',
    'audio/x-m4a': '.m4a',
    'video/mp4': '.mp4'
}

def call_ollama(prompt: str) -> str:
    response = ollama.generate(
        model="llama3.2",
        prompt=prompt,
        stream=False
    )
    return response["response"].strip()

async def process_audio_chunk(chunk_path: str) -> dict:
    try:
        transcript_result = model.transcribe(chunk_path)
        transcript = transcript_result["text"]
        
        summary_prompt = f"Summarize the following meeting transcript:\n\n{transcript}"
        tasks_prompt = f"List the key action items from this meeting:\n\n{transcript}"

        # Run these in parallel
        summary, tasks = await asyncio.gather(
            asyncio.to_thread(call_ollama, summary_prompt),
            asyncio.to_thread(call_ollama, tasks_prompt)
        )

        return {
            "transcript": transcript.strip(),
            "summary": summary,
            "actions": tasks
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing audio: {str(e)}")

@app.post("/transcribe")
async def transcribe_audio(file: UploadFile = File(...)):
    try:
        # Validate file type
        if file.content_type not in SUPPORTED_FORMATS:
            raise HTTPException(
                status_code=400,
                detail=f"Unsupported file type. Supported types are: {', '.join(SUPPORTED_FORMATS.keys())}"
            )

        # Save uploaded file with appropriate extension
        file_extension = SUPPORTED_FORMATS[file.content_type]
        file_location = f"temp_{file.filename}{file_extension}"
        
        with open(file_location, "wb+") as file_object:
            file_object.write(await file.read())
            
        # Transcribe with increased timeout
        result = model.transcribe(file_location, fp16=False, language="en")
        
        # Clean up
        os.remove(file_location)
        
        # Generate summary using Ollama
        summary = await process_audio_chunk(file_location)
        
        return {
            "transcript": result["text"],
            "summary": summary["summary"],
            "actions": summary["actions"]
        }
    except Exception as e:
        if os.path.exists(file_location):
            os.remove(file_location)
        raise HTTPException(status_code=500, detail=str(e))

# Health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "healthy"}    
