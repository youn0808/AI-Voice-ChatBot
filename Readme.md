# AI Voice Chatbot Project (Start)11

Welcome to the AI Voice Chatbot project! This project aims to create an advanced voice chatbot that leverages cutting-edge technologies to deliver a seamless conversational experience. The back-end employs OpenAI Whisper and OpenAI ChatGPT for speech-to-text and text generation, while eelevenLab AI is used for text-to-speech conversion. The front-end, built with React and styled using Tailwind CSS, provides an intuitive user interface to interact with the chatbot.

## Run servers (Update needed)

- Backend : `uvicorn main:app --reload; `
- Frontend: `npm run start`

## Table of Contents

- [Back-end](#back-end)
  - [API Route Endpoints](#api-route-endpoints)
- [Front-end](#front-end)
  - [Technology Stack](#technology-stack)
  - [Styling](#styling)

## Front-end

The front-end offers an engaging and user-friendly interface for interacting with the AI voice chatbot. Key features of the front-end include:

- **WireFrame**: The user interface design is based on a wireframe that outlines the layout and components, ensuring a cohesive design structure.

- **React**: The front-end is developed using React, providing a modular and efficient way to manage UI components and state.

## Back-end

The back-end components are designed to handle the processing of user inputs and the generation of chatbot responses. Here's an overview of the API route endpoints:

### API Route Endpoints

1. **Save Audio Input**: This endpoint allows the application to store user audio inputs. These inputs initiate conversations with the chatbot.

2. **Convert Audio to Text (OpenAI Whisper)**: Audio inputs are processed using OpenAI Whisper to transform spoken language into text format. This text data is then used for chatbot interaction.

3. **Get Chatbot Response (OpenAI ChatGPT)**: Through this endpoint, OpenAI's ChatGPT generates contextually relevant responses based on the processed text from Whisper.

4. **Add to Chat History**: Conversation history, comprising both user messages and chatbot responses, is managed via this endpoint to maintain the flow of the conversation.

5. **Convert Text to Speech (eelevenLab AI)**: Chatbot-generated text is converted back to speech using eelevenLab AI's text-to-speech conversion service. The resulting audio is sent to the front-end for user feedback.

- **Styling with Tailwind CSS**: The UI is styled using Tailwind CSS, a utility-first CSS framework. Tailwind's classes enable rapid UI development and easy customization.

We're excited to introduce this AI Voice Chatbot project, which brings together cutting-edge technologies to create a natural and interactive conversational experience. You're encouraged to explore the codebase, contribute, and tailor the project to your requirements.

For inquiries, feedback, or collaboration opportunities, please reach out to [your contact information].

---
