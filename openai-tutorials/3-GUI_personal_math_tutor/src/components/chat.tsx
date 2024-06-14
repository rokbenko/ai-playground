// Importing necessary modules and components
import * as React from "react";
import { useEffect, useRef, useState } from "react";
import Message from "./message";
import Dialog from "./dialog";
import Image from "next/image";
import useAutoResizeTextArea from "@/hooks/useAutoResizeTextArea";
import { CODE_INTERPRETER } from "@/shared/constants";
import Box from "@mui/material/Box";
import InputLabel from "@mui/material/InputLabel";
import MenuItem from "@mui/material/MenuItem";
import FormControl from "@mui/material/FormControl";
import Select from "@mui/material/Select";
import { TbArrowUp } from "react-icons/tb";
import {
  FaGithub,
  FaStackOverflow,
  FaLinkedin,
  FaYoutube,
} from "react-icons/fa";

// Main functional component
const Chat = () => {
  // State variables
  const [isLoading, setIsLoading] = useState(false);
  const [errorMessage, setErrorMessage] = useState("");
  const [showEmptyChat, setShowEmptyChat] = useState(true);
  const [conversation, setConversation] = useState<any[]>([]);
  const [message, setMessage] = useState("");
  const textAreaRef = useAutoResizeTextArea();
  const bottomOfChatRef = useRef<HTMLDivElement>(null);
  const [selectedModel, setSelectedModel] = React.useState("");

  // Handler for model selection change
  const handleModelChange = (event: any) => {
    setSelectedModel(event.target.value);
  };

  // Effect for resizing the text area based on its content
  useEffect(() => {
    if (textAreaRef.current) {
      textAreaRef.current.style.height = "24px";
      textAreaRef.current.style.height = `${textAreaRef.current.scrollHeight}px`;
    }
  }, [message, textAreaRef]);

  // Effect for scrolling to the bottom of the chat when conversation changes
  useEffect(() => {
    if (bottomOfChatRef.current) {
      bottomOfChatRef.current.scrollIntoView({ behavior: "smooth" });
    }
  }, [conversation]);

  // Function to handle sending a message
  const sendMessage = async (e: any) => {
    e.preventDefault();

    // Don't send empty messages
    if (message.length < 1) {
      setErrorMessage("Please enter a message.");
      return;
    } else {
      setErrorMessage("");
    }

    setIsLoading(true);

    // Add the user message to the conversation immediately
    const updatedConversation = [
      ...conversation,
      { content: message, role: "user" },
    ];
    setConversation(updatedConversation);

    // Add a system message indicating typing immediately
    const typingMessage = { content: "Typing", role: "system" };
    setConversation([...updatedConversation, typingMessage]);

    // Clear the message & remove empty chat
    setMessage("");
    setShowEmptyChat(false);

    try {
      // Include both user and system messages for display purposes
      const allMessages = [...updatedConversation];

      // Separate user messages from the conversation for API call
      const userMessages = allMessages.filter((msg) => msg.role === "user");

      const response = await fetch(`/api/openai`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          messages: userMessages,
          model: selectedModel,
        }),
      });

      // Process the response and update the conversation
      if (response.ok) {
        const data = await response.json();

        // Replace the typing system message with the actual response
        const updatedMessages = [
          ...allMessages,
          { content: data.message, role: "system" },
        ];

        // Update the conversation with the actual response
        setConversation(updatedMessages);
      } else {
        console.error(response);
        setErrorMessage(response.statusText);
      }
    } catch (error: any) {
      console.error(error);
      setErrorMessage(error.message);
    } finally {
      setIsLoading(false);
    }
  };

  // Function to handle key press events
  const handleKeypress = (e: any) => {
    // It triggers by pressing the enter key
    if (e.keyCode == 13 && !e.shiftKey) {
      sendMessage(e);
      e.preventDefault();
    }
  };

  // JSX structure for rendering the component
  return (
    <div className="flex max-w-full flex-1 flex-col">
      {/* Main chat container */}
      <div className="relative h-full w-full transition-width flex flex-col overflow-hidden items-stretch flex-1">
        <div className="flex-1 overflow-hidden">
          <div className="relative h-full dark:bg-gray-800">
            <div className="w-full h-full overflow-y-auto">
              {/* Render conversation if not empty */}
              {!showEmptyChat && conversation.length > 0 ? (
                <div className="flex flex-col items-center text-sm bg-gray-800">
                  {/* Model information */}
                  <div className="flex w-full items-center justify-center gap-1 border-b border-black/10 bg-gray-50 p-3 text-gray-500 dark:border-gray-900/50 dark:bg-gray-700 dark:text-gray-300">
                    Model: {CODE_INTERPRETER.name}
                  </div>
                  {/* Render each message in the conversation */}
                  {conversation.map((message, index) => (
                    <Message key={index} message={message} />
                  ))}
                  {/* Placeholder for scrolling to the bottom of the chat */}
                  <div className="w-full h-32 md:h-48 flex-shrink-0"></div>
                  <div ref={bottomOfChatRef}></div>
                </div>
              ) : null}
              {/* Render empty chat if needed */}
              {showEmptyChat ? (
                <div className="pb-10 sm:pt-10 pt-4 px-2 relative w-full flex flex-col h-full">
                  {/* Model selection dropdown */}
                  <div className="flex items-center justify-center gap-2">
                    <div className="relative w-full md:w-1/2 lg:w-1/3 xl:w-1/4">
                      <Box>
                        <FormControl
                          fullWidth
                          sx={{
                            ".MuiOutlinedInput-root .MuiOutlinedInput-notchedOutline":
                              {
                                borderColor: "rgba(255, 255, 255, 0.25)",
                              },
                            ".MuiOutlinedInput-root .MuiSvgIcon-root ": {
                              fill: "rgba(255, 255, 255, 1) !important",
                            },
                          }}
                        >
                          {/* Model selection label */}
                          <InputLabel
                            id="model-select-label"
                            sx={{
                              color: "rgba(255, 255, 255, 0.75)",
                              "&.Mui-focused": {
                                color: "rgba(255, 255, 255, 1) !important",
                              },
                            }}
                          >
                            Model
                          </InputLabel>
                          {/* Model selection dropdown */}
                          <Select
                            labelId="model-select-label"
                            id="model-select"
                            value={selectedModel || ""}
                            label="Model"
                            onChange={handleModelChange}
                            sx={{
                              color: "rgba(255, 255, 255, 1)",
                              boxShadow: "none",
                              "&.MuiOutlinedInput-root:hover .MuiOutlinedInput-notchedOutline":
                                {
                                  borderColor: "rgba(255, 255, 255, 0.75)",
                                },
                              "&.MuiOutlinedInput-root.Mui-focused .MuiOutlinedInput-notchedOutline":
                                {
                                  borderColor: "rgba(255, 255, 255, 1)",
                                },
                              "&.MuiOutlinedInput-root.MuiInputBase-colorPrimary.MuiInputBase-formControl":
                                {
                                  borderRadius: "0.5rem",
                                },
                            }}
                            inputProps={{
                              MenuProps: {
                                PaperProps: {
                                  sx: {
                                    color: "rgba(255, 255, 255, 1)",
                                    backgroundColor:
                                      "rgb(32 33 35 / var(--tw-bg-opacity))",
                                  },
                                },
                              },
                            }}
                          >
                            {/* Model selection item */}
                            <MenuItem value={CODE_INTERPRETER.name}>
                              {CODE_INTERPRETER.name}
                            </MenuItem>
                          </Select>
                        </FormControl>
                      </Box>
                    </div>
                  </div>
                  {/* ChatMATH branding and information */}
                  <div className="text-2xl sm:text-4xl font-semibold text-center text-black dark:text-white flex flex-col gap-2 items-center justify-center h-screen">
                    <h1>chatMATH</h1>
                    {/* OpenAI badge */}
                    <Image
                      src="/powered-by-openai-badge-outlined-on-dark.svg"
                      width={165.92}
                      height={32}
                      alt="Powered by OpenAI badge"
                      className="pt-3"
                    />
                    {/* Footer information */}
                    <div className="font-normal text-sm pt-4">
                      Made with ❤️ by Rok
                    </div>
                    {/* Social media icons */}
                    <div className="flex pt-0 gap-2">
                      <a
                        target="_blank"
                        href="https://github.com/rokbenko"
                        className="opacity-50 hover:opacity-100 duration-200"
                      >
                        <FaGithub className="scale-75" />
                      </a>
                      <a
                        target="_blank"
                        href="https://stackoverflow.com/users/10347145/"
                        className="opacity-50 hover:opacity-100 duration-200"
                      >
                        <FaStackOverflow className="scale-75" />
                      </a>
                      <a
                        target="_blank"
                        href="https://www.linkedin.com/in/rokbenko/"
                        className="opacity-50 hover:opacity-100 duration-200"
                      >
                        <FaLinkedin className="scale-75" />
                      </a>
                      <a
                        target="_blank"
                        href="https://www.youtube.com/@rokbenko?sub_confirmation=1"
                        className="opacity-50 hover:opacity-100 duration-200"
                      >
                        <FaYoutube className="scale-75" />
                      </a>
                    </div>
                    {/* Dialog component */}
                    <div className="mt-12">
                      <Dialog />
                    </div>
                  </div>
                </div>
              ) : null}
              {/* Placeholder for additional content */}
              <div className="flex flex-col items-center text-sm dark:bg-gray-800"></div>
            </div>
          </div>
        </div>
        {/* Form for user input */}
        <div className="absolute bottom-0 left-0 w-full dark:border-white/20 md:border-transparent md:dark:border-transparent md:bg-vert-light-gradient bg-white dark:bg-gray-800 md:!bg-transparent dark:md:bg-vert-dark-gradient pt-2">
          <form className="stretch mx-2 flex flex-row gap-3 last:mb-2 md:mx-4 md:last:mb-6 lg:mx-auto lg:max-w-2xl xl:max-w-3xl">
            <div className="relative flex flex-col h-full flex-1 items-stretch md:flex-col">
              {/* Display error message if any */}
              {errorMessage ? (
                <div className="mb-2 md:mb-0">
                  <div className="h-full flex ml-1 md:w-full md:m-auto md:mb-2 gap-0 md:gap-2 justify-center">
                    <span className="text-red-500 text-sm">{errorMessage}</span>
                  </div>
                </div>
              ) : null}
              {/* Text area for user input */}
              <div className="flex flex-col w-full flex-grow py-[10px] pr-10 pl-3 md:pl-4 md:py-4 md:pr-12 relative border border-black/10 bg-white dark:border-gray-900/50 dark:text-white dark:bg-gray-700 rounded-2xl shadow-[0_0_20px_rgba(0,0,0,0.025)] dark:shadow-[0_0_20px_rgba(0,0,0,0.025)]">
                <textarea
                  ref={textAreaRef}
                  value={message}
                  tabIndex={0}
                  data-id="root"
                  style={{
                    height: "24px",
                    maxHeight: "200px",
                    overflowY: "hidden",
                  }}
                  placeholder="Message chatMATH..."
                  className="focus:outline-none focus:shadow-none m-0 w-full resize-none border-0 bg-transparent p-0 pr-7 focus:ring-0 focus-visible:ring-0 dark:bg-transparent pl-2 md:pl-0"
                  onChange={(e) => setMessage(e.target.value)}
                  onKeyDown={handleKeypress}
                ></textarea>
                {/* Send button */}
                <button
                  disabled={isLoading || message?.length === 0}
                  onClick={sendMessage}
                  className="w-[29px] h-[29px] flex justify-center items-center absolute p-1 rounded-lg bottom-1.5 md:bottom-3.5 text-white bg-white disabled:bg-gray-500 disabled:text-gray-400 right-2 md:right-3 transition-colors disabled:opacity-40"
                >
                  <TbArrowUp className="text-white dark:text-black" />
                </button>
              </div>
            </div>
          </form>
          {/* Informational text */}
          <div className="px-2 py-2 text-center text-xs text-gray-600 dark:text-gray-300">
            <span>
              chatMATH can make mistakes. Consider checking important
              information.
            </span>
          </div>
        </div>
      </div>
    </div>
  );
};

// Exporting the component
export default Chat;
