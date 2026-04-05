from fastapi import FastAPI, HTTPException
import requests
from pydantic import BaseModel
import uvicorn

app = FastAPI()

# Dán link Pinggy từ Colab vào đây Ollama-Pinggy.ipynb]
OLLAMA_URL = "https://uqcxw-34-148-42-172.run.pinggy-free.link/api/generate"

class EmailRequest(BaseModel):
    text: str

@app.get("/")
async def root():
        return {"message": "Welcome to the Spam Detection API!"}

@app.post("/health")
async def health_check():
        if not OLLAMA_URL:
                raise HTTPException(status_code=500, detail="OLLAMA_URL is not configured.")    
        return {"status": "OK", "message": "API is healthy and running."}

@app.post("/predict")
async def predict(request: EmailRequest):
    if not request.text or request.text.strip() == "":
        raise HTTPException(status_code=400, detail="Input text cannot be empty.")
    payload = {
        "model": "artyann-gemma", 
        "prompt": request.text,
        "stream": False
    }

    try:
        response = requests.post(OLLAMA_URL, json=payload, timeout=60)
        res_data = response.json()
        prediction = res_data['response'].strip().upper()
        
        return {
            "label": "SPAM" if "SPAM" in prediction else "HAM",
            "confidence": "High (Gemma 2 Engine)"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)