import ollama
from fastapi import FastAPI, UploadFile, File
import tempfile as tmp
import whisper
from fastapi.responses import JSONResponse

app = FastAPI()
model = whisper.load_model("base")


def call_ollama(prompt: str) -> str:
    response = ollama.generate(
        model="llama3.2",
        prompt=prompt,
        stream=False
    )
    return response["response"].strip()


@app.post("/transcribe")
async def process_audio(file: UploadFile = File(...)):
    try:
        with tmp.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_file:
            temp_file.write(await file.read())
            tmp_path = temp_file.name


        transcript_result = model.transcribe(tmp_path)

        transcript = transcript_result["text"]
        summary_prompt = f"Summarize the following meeting transcript:\n\n{transcript}"
        tasks_prompt = f"List the key action items from this meeting:\n\n{transcript}"

        summary = call_ollama(summary_prompt)

        tasks = call_ollama(tasks_prompt)

        return {
            "transcript": transcript.strip(),
            "summary": summary,
            "actions": tasks
        }

    except Exception as e:
        print("Error occurred:", e)
        return JSONResponse(content={"error": str(e)}, status_code=500)    
