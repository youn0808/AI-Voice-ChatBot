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

    // Add logic
    setIsRestting(false);
  };

  return <div>Hello</div>;
}

export default Title;
