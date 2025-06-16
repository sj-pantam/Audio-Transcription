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
async def process_audio(file: UploadFile = File(...)):
    try:
        # Check file size
        file_size = 0
        chunk_size = 1024 * 1024  # 1MB chunks
        
        with tmp.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_file:
            while chunk := await file.read(chunk_size):
                if file_size + len(chunk) > MAX_FILE_SIZE:
                    raise HTTPException(
                        status_code=413,
                        detail=f"File too large. Maximum size is {MAX_FILE_SIZE/1024/1024}MB"
                    )
                temp_file.write(chunk)
                file_size += len(chunk)
            tmp_path = temp_file.name

        try:
            result = await process_audio_chunk(tmp_path)
            return result
        finally:
            # Clean up temporary file
            if os.path.exists(tmp_path):
                os.unlink(tmp_path)

    except HTTPException as he:
        raise he
    except Exception as e:
        print("Error occurred:", e)
        return JSONResponse(content={"error": str(e)}, status_code=500)

# Health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "healthy"}    
