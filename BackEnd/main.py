# uvicorn main:app
# source venv/bin/activate
# uvicorn main:app --reload

# Main Imports
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from decouple import config
import openai

# Custom Functions Impoprts
# ....

# Initiate App
app = FastAPI()

# CORS - Origins
origins = [
    "http://localhost:3030",
]

# cors - Middleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# End Points


@app.get("/health")
async def check_health():
    return {"message": "healthy"}

# Post bot response
# Note: Not playing in browser when using past requests


@app.post("/post-audio/")
async def post_audio(file: UploadFile = File(...)):
    print("Got post")
