import json
import random

# Get recent messages


def get_recent_messages():
    # Define the file name and lean insturction (What we feed to chatGPT)
    file_name = "stored_data.json"
    learn_instruction = {
        "role": "system",
        "content": "You are helping user which country to travel. Your name is ExploreMentor Bot. Keep your answer to under 30 words and you should answer with english"
    }

    # Init messages
    messages = []

    # Add a random element
    x = random.uniform(0, 1)
    if x < 0.5:
        learn_instruction["content"] = learn_instruction["content"] + \
            " Your response will include some light humour."
    else:
        learn_instruction["content"] = learn_instruction["content"] + \
            " Your response will include another question for user."

    # Append instruction to message
    messages.append(learn_instruction)

    # Get last messages
    try:
        with open(file_name) as user_file:
            data = json.load(user_file)

            # Append last 5 items of data (<5 then add all data else add last 5 data)
            if data:
                if len(data) < 5:
                    for item in data:
                        messages.append(item)
                else:
                    for item in data[-5:]:
                        messages.append(item)
    except Exception as e:
        print(e)
        pass

    # Return
    return messages
