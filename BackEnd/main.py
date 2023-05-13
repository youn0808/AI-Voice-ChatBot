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
from functions.openai_requests import convert_audio_to_text
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

# End Points--------------------------------------------------


@app.get("/health")
async def check_health():
    return {"message": "healthy"}


@app.get("/post-audio-get/")
async def get_audio():

    # Get Saved audio
    audio_input = open("voice.mp3", "rb")
    # Decode audio
    message_decoded = convert_audio_to_text(audio_input)

    # Decode Audio
    print(message_decoded)
    return "Done"

# Post bot response
# Note: Not playing in browser when using past requests


# @app.get("/post-audio-get/")
# async def post_audio(file: UploadFile = File(...)):
#     print("Got post")
