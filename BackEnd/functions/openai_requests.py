import openai
from decouple import config

# Retrieve Environment variables
openai.organization = config("OPEN_AI_ORG")
openai.api_key = config("OPEN_AI_KEY")

# OPEN AI -Whisper
# Convert Audio to Text


def convertAudioToText(audio_file):
    try:
        transcript = openai.Audio.transcribe("whisper-1", audio_file)
        messaeg_text = transcript["text"]
        return messaeg_text
    except Exception as e:
        print(e)
        return
