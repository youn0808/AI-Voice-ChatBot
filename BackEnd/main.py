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
from functions.database import store_messages, reset_messages
from functions.openai_requests import convert_audio_to_text, get_chat_response
from functions.text_to_voice import convert_text_to_voice
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


@app.get("/")
async def welcome():
    return {"message": "Welcome"}


@app.get("/reset")
async def reset_conversation():
    reset_messages()
    return {"message": "reset conversation"}


@app.post("/post-audio")
async def post_audio(file: UploadFile = File(...)):

    # Get Saved audio
    # audio_input = open("voice.mp3", "rb")

    # Save file from frontend
    with open(file.filename, "wb") as buffer:
        buffer.write(file.file.read())
    audio_input = open(file.filename, "rb")

    # Decode audio (Convert audio to text)
    message_decoded = convert_audio_to_text(audio_input)

    # Guard: Ensure message decoded
    if not message_decoded:
        return HTTPException(status_code=400, detail="Failed to decode audio")

    # Get chatGPT responses (Feed decoded message to chatGPT and get response)
    chat_response = get_chat_response(message_decoded)
    store_messages(message_decoded, chat_response)

    if not chat_response:
        return HTTPException(status_code=400, detail="Failed to chat response")

    # convert chat response to audio
    audio_output = convert_text_to_voice(chat_response)
    if not audio_output:
        return HTTPException(status_code=400, detail="Failed to audio response")

    # create a generator that yiel chunck of data
    def iterfile():
        yield audio_output

    # Return audio file
    return StreamingResponse(iterfile(), media_type="application/octet-stream")


# Post bot response
# Note: Not playing in browser when using past requests
