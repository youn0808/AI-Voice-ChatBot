import json
import random

# Constants
LEARN_INSTRUCTION = {
    "role": "system",
    "content": "You are helping the user choose a travel destination. Your name is ExploreMentor Bot. Keep your answer under 30 words and use English."
}
MAGIC_NUMBER_THRESHOLD = 0.2
RECENT_MESSAGES_LIMIT = 5
FILE_NAME = "stored_data.json"


def get_recent_messages():

    # Init messages
    messages = []

    # Add a random element
    x = random.uniform(0, 1)
    if x < MAGIC_NUMBER_THRESHOLD:
        learn_instruction = LEARN_INSTRUCTION.copy()
        learn_instruction["content"] += " Your response will include some light humour."
    else:
        learn_instruction = LEARN_INSTRUCTION.copy()
        learn_instruction["content"] += " Your response will include another question for the user."

    # Append instruction to message
    messages.append(learn_instruction)
    try:
        with open(FILE_NAME) as user_file:
            data = json.load(user_file)
            messages.extend(data[-RECENT_MESSAGES_LIMIT:])
    except Exception as e:
        print("Error while loading recent messages:", e)

    return messages


def store_messages(request_message, response_message):

    # Get recent messages ( when user create, it automatically added default message so it exclude first message)
    messages = get_recent_messages()[1:]

    # add messages to data
    user_message = {"role": "user", "content": request_message}
    assistant_message = {"role": "assistant", "content": response_message}
    messages.append(user_message)
    messages.append(assistant_message)

    # Save the updated file
    with open(FILE_NAME, "w") as f:
        json.dump(messages, f)


def reset_messages():
    try:
        open(FILE_NAME, "w").close()
    except Exception as e:
        print("Error while resetting messages:", e)
