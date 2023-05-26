import { useState } from "react";
import axios from "axios";

type Props = {
  setMessages: any;
};

function Title({ setMessages }: Props) {
  const [isResetting, setIsRestting] = useState(false);

  //   Reset tje cpmverstatopm
  const resetConversation = async () => {
    setIsRestting(true);

    await axios
      .get("http://localhost:8000/reset")
      .then((res) => {
        if (res.status == 200) {
          setMessages([]);
        } else {
          console.error("An error with API request to backend");
        }
      })
      .catch((e) => {
        console.error(e.message);
      });
    // Add logic
    setIsRestting(false);
  };

  return (
    <div>
      <button className="bg-indigo-500 p-5">Reset Button</button>
    </div>
  );
}

export default Title;
