import { ReactMediaRecorder } from "react-media-recorder";
import RecordIcon from "./RecordIcon";

type Props = {
  handleStop: any;
};

function RecordMsg({ handleStop }: Props) {
  return (
    <ReactMediaRecorder
      audio
      onStop={handleStop}
      render={({ status, startRecording, stopRecording }) => (
        <div className="mt-2">
          <button
            onMouseDown={startRecording}
            onMouseUp={stopRecording}
            className="bg-white p-4 rounded-full text-black"
          >
            <RecordIcon
              classText={
                status == "recording"
                  ? "animate-pulse text-red-500"
                  : "text-sky-500"
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
