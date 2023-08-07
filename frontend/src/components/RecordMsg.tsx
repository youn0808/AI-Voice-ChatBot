import { ReactMediaRecorder } from "react-media-recorder";
import RecordIcon from "./RecordIcon";

// Define a specific type for the handleStop function
type HandleStopFunction = (blobUrl: string) => void;

type RecordMsgProps = {
  handleStop: HandleStopFunction; // Use the specific type
};

// Functional component to render the recording message and controls
function RecordMsg({ handleStop }: RecordMsgProps) {
  return (
    <ReactMediaRecorder
      audio // Configure ReactMediaRecorder for audio recording
      onStop={handleStop} // Pass the handleStop function to be executed on stop
      render={({ status, startRecording, stopRecording }) => (
        <div className="mt-1">
          <button
            onMouseDown={startRecording}
            onMouseUp={stopRecording}
            className="bg-white p-4 rounded-full text-black"
          >
            <RecordIcon
              classText={
                status == "recording"
                  ? "animate-pulse text-red-500"
                  : "text-sky-300"
              }
            />
          </button>
          <p className="font-light mt-2">{status}</p>
        </div>
      )}
    />
  );
}

export default RecordMsg;
