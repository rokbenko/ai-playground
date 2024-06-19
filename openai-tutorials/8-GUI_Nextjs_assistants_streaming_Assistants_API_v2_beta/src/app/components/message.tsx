// Imports
import { useState, useEffect } from "react";
import { SiOpenai } from "react-icons/si";
import { HiUser } from "react-icons/hi";

// Functional component representing a chat message
export default function Message(props: any) {
  // Destructuring props to extract the 'message' object
  const { message } = props;
  const { role, content: text } = message;

  // Checking if the message is from the user
  const isUser = role === "user";

  // State to control the typing animation visibility
  const [showTypingAnimation, setShowTypingAnimation] = useState(true);

  // Effect to control the typing animation based on the message content
  useEffect(() => {
    if (text === "Typing") {
      setShowTypingAnimation(true);
    } else {
      setShowTypingAnimation(false);
    }
  }, [text]);

  // Render the message component
  return (
    <div
      className={`group w-full text-gray-800 dark:text-gray-100 dark:bg-[#212121]`}
    >
      <div className="text-base gap-4 md:gap-6 flex lg:px-0 m-auto w-full max-w-[768px]">
        <div
          className={`flex flex-row gap-4 md:gap-6 p-4 md:py-6 lg:px-0 m-auto w-full ${
            isUser ? "justify-end" : ""
          }`}
        >
          {/* User or OpenAI icon */}
          <div
            className={`w-8 flex flex-col relative items-${
              isUser ? "end order-1" : "start"
            }`}
          >
            <div className="relative h-8 w-8 p-1 rounded-full text-white flex items-center justify-center bg-black/75">
              {isUser ? (
                <HiUser className="h-4 w-4 text-white" />
              ) : (
                <SiOpenai className="h-4 w-4 text-white" />
              )}
            </div>
          </div>
          {/* Message content */}
          <div className="relative flex flex-col gap-1 md:gap-3 max-w-[70%]">
            <div className="flex flex-grow flex-col gap-3">
              <div className="flex flex-col items-start gap-4 whitespace-pre-wrap break-words">
                {/* Markdown content */}
                <div className="markdown prose w-full break-words dark:prose-invert dark">
                  {/* Typing animation or message text */}
                  {!isUser && showTypingAnimation ? (
                    <div className="typing flex items-center mt-[10px]">
                      <span className="typing-dot"></span>
                      <span className="typing-dot"></span>
                      <span className="typing-dot"></span>
                    </div>
                  ) : (
                    <p
                      className={` ${
                        isUser
                          ? "dark:bg-[#2f2f2f] py-2.5 px-5 rounded-3xl"
                          : ""
                      }`}
                    >
                      {text}
                    </p>
                  )}
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
