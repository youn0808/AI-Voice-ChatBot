import { useState } from "react";
import Title from "./Title";
import RecordMsg from "./RecordMsg";
import axios from "axios";
import { BsGithub } from "react-icons/bs";

function Controller() {
  const [isLoading, setIsLoading] = useState(false);
  const [messages, setMessages] = useState<any[]>([]);

  // Function to create a blob URL from binary data
  const createBlobUrl = (data: any) => {
    const blob = new Blob([data], { type: "audio/*" });
    return URL.createObjectURL(blob);
  };

  // Function to handle the stop event when recording audio
  const handleStop = async (blobUrl: string) => {
    setIsLoading(true);

    //Append recorded new message to messages
    const myMessage = { sender: "me", blobUrl };
    const messagesArray = [...messages, myMessage];

    //Convert blob url to blob object
    fetch(blobUrl)
      .then((res) => res.blob())
      .then(async (blob) => {
        //construct audio to send file
        const formData = new FormData();
        formData.append("file", blob, "myFile.wav");

        //send the form data to backend API endpoint
        // "http://localhost:8000/post-audio"
        // "https://ai-voice-chatbot-ouq9.onrender.com/post-audio",
        await axios
          .post(
            "https://ai-voice-chatbot-ouq9.onrender.com/post-audio",
            formData,
            {
              headers: { "Content-Type": "audio/mpeg" },
              responseType: "arraybuffer",
            }
          )
          .then((res: any) => {
            //displaying to front-end
            const blob = res.data;
            const audio = new Audio();
            audio.src = createBlobUrl(blob);

            //Append to audio
            const botMessage = { sender: "Explor Mentor", blobUrl: audio.src };
            messagesArray.push(botMessage);
            setMessages(messagesArray);

            //Alay audio
            audio.play();
            setIsLoading(false);
          })
          .catch((err) => {
            console.error("error occur!", err.message);
            setIsLoading(false);
          });
      });
  };

  return (
    <div className="h-screen overflow-y-hidden">
      <Title setMessages={setMessages} />
      <div className="flex flex-col justify-between h-full overflow-y-scroll pb-96">
        {/* Conversation */}
        <div className="mt-3 px-3">
          {messages?.map((audio, index) => {
            return (
              <div
                key={index + audio.sender}
                className={
                  "flex flex-col" +
                  (audio.sender === "Explor Mentor" ? " flex items-end" : "")
                }
              >
                {/* Sender */}
                <div className="mt-2">
                  <p
                    className={
                      audio.sender == "Explor Mentor"
                        ? "text-right mr-2 italic text-green-500 text"
                        : "ml-2 italic text-blue-500"
                    }
                  >
                    {audio.sender.charAt(0).toUpperCase() +
                      audio.sender.slice(1)}
                  </p>
                  {/* audio messages */}
                  <audio src={audio.blobUrl} controls />
                </div>
              </div>
            );
          })}
          {messages.length == 0 && !isLoading && (
            <div className="text-center italic mt-10">
              Feel free to ask any questions about your trip plans
            </div>
          )}
          {isLoading ? (
            <div className="text-center italic mt-10 animate-pulse">
              Give me a few seconds....
            </div>
          ) : (
            ""
          )}
        </div>
        {/* {Recorder} */}
        <div className="fixed bottom-0 w-full py-3 border-t text-center bg-gradient-to-r from-blue-600 to-green-200 text-white">
          <div className="flex justify-center items-center w-full">
            <RecordMsg handleStop={handleStop} />
          </div>
          <div className="ml-3 mb-3 text-3xl">
            <a href="https://github.com/youn0808" target="_blank">
              <BsGithub />
            </a>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Controller;
