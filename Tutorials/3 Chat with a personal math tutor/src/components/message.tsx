// Importing necessary modules and components
import { useState, useEffect } from "react";
import { SiOpenai } from "react-icons/si";
import { HiUser } from "react-icons/hi";

// Functional component representing a chat message
const Message = (props: any) => {
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

  // JSX structure for rendering the component
  return (
    <div
      className={`group w-full text-gray-800 dark:text-gray-100 border-b border-black/10 dark:border-gray-900/50 ${
        isUser ? "dark:bg-gray-800" : "bg-gray-50 dark:bg-[#444654]"
      }`}
    >
      <div className="text-base gap-4 md:gap-6 md:max-w-2xl lg:max-w-xl xl:max-w-3xl flex lg:px-0 m-auto w-full">
        <div className="flex flex-row gap-4 md:gap-6 md:max-w-2xl lg:max-w-xl xl:max-w-3xl p-4 md:py-6 lg:px-0 m-auto w-full">
          {/* User or OpenAI icon */}
          <div className="w-8 flex flex-col relative items-end">
            <div className="relative h-7 w-7 p-1 rounded-lg text-white flex items-center justify-center bg-black/75 text-opacity-100r">
              {isUser ? (
                <HiUser className="h-4 w-4 text-white" />
              ) : (
                <SiOpenai className="h-4 w-4 text-white" />
              )}
            </div>
          </div>
          {/* Message content */}
          <div className="relative flex w-[calc(100%-50px)] flex-col gap-1 md:gap-3 lg:w-[calc(100%-115px)]">
            <div className="flex flex-grow flex-col gap-3">
              <div className="min-h-20 flex flex-col items-start gap-4 whitespace-pre-wrap break-words">
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
                    <p>{text}</p>
                  )}
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

// Exporting the component
export default Message;
