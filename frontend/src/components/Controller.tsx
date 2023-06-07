import { useState } from "react";
import Title from "./Title";
import RecordMsg from "./RecordMsg";
function Controller() {
  const [isLoading, setIsLoading] = useState(false);
  const [messages, setMessages] = useState<any[]>([]);

  const [blob, setBlob] = useState("");

  const createBlobUrl = (data: any) => {
    const blob = new Blob([data], { type: "audio/mpeg" });
    const url = window.URL.createObjectURL(blob);
    return url;
  };

  const handleStop = async (blobUrl: string) => {
    setIsLoading(true);

    //Append recorded new message to messages
    const myMessage = { sender: "me", blobUrl };
    const messagesArr = [...messages, myMessage];

    setIsLoading(false);
  };

  return (
    <div className="h-screen overflow-y-hidden">
      <Title setMessages={setMessages} />
      <div className="flex flex-col justify-between h-full overflow-y-scroll pb-96">
        {/* {Recorder} */}
        <div className="fixed bottom-0 w-full py-6 border-t text-center bg-gradient-to-r from-blue-600 to-green-200 text-white">
          <div className="flex justify-center items-center w-full">
            <RecordMsg handleStop={handleStop} />
          </div>
        </div>
      </div>
    </div>
  );
}

export default Controller;
