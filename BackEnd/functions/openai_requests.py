import openai
from decouple import config

# Import custom functions
from functions.database import get_recent_messages

# Set up OpenAI credentials
openai.organization = config("OPEN_AI_ORG")
openai.api_key = config("OPEN_AI_KEY")

# OpenAI - Whisper
# Convert Audio to Text


def convert_audio_to_text(audio_file):
    try:
        transcript = openai.Audio.transcribe("whisper-1", audio_file)
        message_text = transcript["text"]
        return message_text
    except Exception as e:
        print(e)
        return

# OpenAI - ChatGPT
# Feed decoded text message to ChatGPT and get response
# Get responses to our message


def get_chat_response(message_input):
    user_message = {"role": "user", "content": message_input}
    messages = get_recent_messages()
    messages.append(user_message)
    print("All Messages:", messages)

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        print("OpenAI response:", response)
        message_text = response["choices"][0]["message"]["content"]
        return message_text
    except Exception as e:
        print("Error:", e)
        return "An error occurred while generating the response."
