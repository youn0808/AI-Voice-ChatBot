# Explormentor Bot - AI Voice Chat Travel Advisor

Explormentor Bot is an AI-powered voice chat travel advisor application that assists users in planning their trips through voice interactions. The application is built with React for the frontend and FastAPI for the backend. It features a human-like voice assistant powered by ChatGPT and Eleven Lab to provide the most advanced chatbot experience.

## Features

- Interactive Voice Interaction: Users can interact with the chatbot using voice commands for an intuitive experience.
- Trip Planning Assistance: The chatbot helps users create travel plans by responding to their queries and providing recommendations.
- Advanced AI Models: The chatbot's responses are generated using advanced AI models, including ChatGPT and Eleven Lab.
- Frontend: The user interface is developed using React, providing a responsive and user-friendly design.
- Backend: The backend is powered by FastAPI, a high-performance web framework for building APIs with Python.

### API Route Endpoints

1. **Save Audio Input**: This endpoint allows the application to store user audio inputs. These inputs initiate conversations with the chatbot.

2. **Convert Audio to Text (OpenAI Whisper)**: Audio inputs are processed using OpenAI Whisper to transform spoken language into text format. This text data is then used for chatbot interaction.

3. **Get Chatbot Response (OpenAI ChatGPT)**: Through this endpoint, OpenAI's ChatGPT generates contextually relevant responses based on the processed text from Whisper.

4. **Add to Chat History**: Conversation history, comprising both user messages and chatbot responses, is managed via this endpoint to maintain the flow of the conversation.

5. **Convert Text to Speech (eelevenLab AI)**: Chatbot-generated text is converted back to speech using eelevenLab AI's text-to-speech conversion service. The resulting audio is sent to the front-end for user feedback.

- **Styling with Tailwind CSS**: The UI is styled using Tailwind CSS, a utility-first CSS framework. Tailwind's classes enable rapid UI development and easy customization.

### Run server

### Frontend

To build and start the frontend development server, follow these steps:

1. Navigate to the `frontend` directory: `cd frontend`
2. Build the project: `yarn build`
3. Start the development server: `yarn dev`

### Backend

To run the FastAPI backend server, follow these steps:

1. Navigate to the `backend` directory: `cd backend`
2. Create a virtual environment: `python3 -m venv venv`
3. Activate the virtual environment:
   - On Windows: `venv\Scripts\activate`
   - On macOS and Linux: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Start the FastAPI server: `uvicorn main:app --reload`

## .env File Configuration

Create a `.env` file in the root directory of the project and configure the following environment variables:

```dotenv
ELEVEN_LABS_API_KEY=
OPEN_AI_KEY=
OPEN_AI_ORG=
```
