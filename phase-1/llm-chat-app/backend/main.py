from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests

app = FastAPI()

# Allow communication from Streamlit frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request model
class PromptRequest(BaseModel):
    prompt: str
    stream: bool = False

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "mistral"

@app.post("/generate")
def generate_recipe(data: PromptRequest):
    try:
        res = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL_NAME,
                "prompt": data.prompt,
                "stream": data.stream
            },
            stream=data.stream
        )

        if data.stream:
            # Streamed responses aren't ideal for API → frontend, use full output
            return {"error": "Streaming not supported in this mode"}

        result = res.json()
        return {"response": result.get("response", "")}
    
    except Exception as e:
        return {"error": str(e)}
