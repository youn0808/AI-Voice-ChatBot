import json
import random


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
    if x < 0.2:
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

# store messages


def store_messages(request_message, response_message):
    # define the file name
    file_name = "stored_data.json"

    # Get recent messages ( when user create, it automatically added default message so it exclude first message)
    messages = get_recent_messages()[1:]

    # add messages to data
    user_message = {"role": "user", "content": request_message}
    assistant_message = {"role": "assistant", "content": response_message}
    messages.append(user_message)
    messages.append(assistant_message)

    # Save the updated file
    with open(file_name, "w") as f:
        json.dump(messages, f)


# Reset message
def reset_messages():
    # overwrite current file with nothing
    open("stored_data.json", "w")
