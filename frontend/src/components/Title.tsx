import { useState } from "react";
import axios from "axios";

type TitleProps = {
  setMessages: any; // Function to set messages, should have a more specific type
};

function Title({ setMessages }: TitleProps) {
  const [isResetting, setIsRestting] = useState(false);
  // Function to reset the conversation by making an API request
  const resetConversation = async () => {
    setIsRestting(true);

    try {
      // const response = await axios.get("http://localhost:8000/reset");

      const response = await axios.get(
        "https://ai-voice-chatbot-ouq9.onrender.com/reset"
      );

      if (response.status === 200) {
        setMessages([]); // Reset messages
      } else {
        console.error("An error with API request to backend");
      }
    } catch (error: any) {
      console.error(error.message);
    }

    setIsRestting(false);
  };

  return (
    <div className="flex justify-between items-center w-full p-4 bg-gray-900 text-white text-lg">
      <div className="italic">ExploreMentor Bot</div>

      <button
        onClick={resetConversation}
        className={
          "transition-all duration-300 text-blue-100 hover:text-blue-500 " +
          (isResetting ? "animate-pulse" : "")
        }
      >
        <div className="flex text-center">
          <p className="flex text-center items-center pr-4">Reset</p>
          <svg
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 24 24"
            strokeWidth={1.5}
            stroke="currentColor"
            className="w-6 h-6"
          >
            <path
              strokeLinecap="round"
              strokeLinejoin="round"
              d="M16.023 9.348h4.992v-.001M2.985 19.644v-4.992m0 0h4.992m-4.993 0l3.181 3.183a8.25 8.25 0 0013.803-3.7M4.031 9.865a8.25 8.25 0 0113.803-3.7l3.181 3.182m0-4.991v4.99"
            />
          </svg>
        </div>
      </button>
    </div>
  );
}

export default Title;
