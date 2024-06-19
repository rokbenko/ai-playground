"use client";

// Imports
import * as React from "react";
import { useEffect, useRef, useState } from "react";
import Image from "next/image";
import Message from "./message";
import useAutoResizeTextArea from "../hooks/useAutoResizeTextArea";
import { OPENAI_MODELS_AND_TOOLS } from "../shared/constants";
import Box from "@mui/material/Box";
import InputLabel from "@mui/material/InputLabel";
import MenuItem from "@mui/material/MenuItem";
import FormControl from "@mui/material/FormControl";
import Select from "@mui/material/Select";
import Tooltip from "@mui/material/Tooltip";
import { TbArrowUp } from "react-icons/tb";
import {
  FaLinkedin,
  FaStackOverflow,
  FaGithub,
  FaYoutube,
  FaPatreon,
} from "react-icons/fa";

// Main functional component representing the chat
export default function Chat() {
  // State variables
  const [isLoading, setIsLoading] = useState(false);
  const [errorMessage, setErrorMessage] = useState("");
  const [showEmptyChat, setShowEmptyChat] = useState(true);
  const [conversation, setConversation] = useState<any[]>([]);
  const [message, setMessage] = useState("");
  const textAreaRef = useAutoResizeTextArea();
  const bottomOfChatRef = useRef<HTMLDivElement>(null);
  const [selectedAssistant, setSelectedAssistant] = React.useState("");

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

  // Function to handle assistant selection change
  const handleAssistantChange = (event: any) => {
    setSelectedAssistant(event.target.value);
  };

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

      // Make the OpenAI API call
      const response = await fetch(`/api/openai`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          messages: userMessages,
          passSelectedAssistant: selectedAssistant,
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
        console.log(response);
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

  // Function to handle change assistant
  const changeAssistant = () => {
    setShowEmptyChat(true);
    setConversation([]);
    setSelectedAssistant("");
  };

  // Render the main chat component
  return (
    <div className="flex max-w-full flex-1 flex-col">
      {/* Main chat container */}
      <div className="relative h-full w-full transition-width flex flex-col overflow-hidden items-stretch flex-1">
        <div className="flex-1 overflow-hidden">
          <div className="relative h-full dark:bg-[#212121]">
            <div className="w-full h-full overflow-y-auto">
              {/* Render conversation if not empty */}
              {!showEmptyChat && conversation.length > 0 ? (
                <div className="flex flex-col items-center text-sm bg-gray-800">
                  {/* Model information */}
                  <div className="text-xs flex w-full items-center justify-center gap-1 border-b border-black/10 bg-gray-50 p-3 text-gray-500 dark:border-gray-900/50 dark:bg-[#2f2f2f] dark:text-gray-300">
                    Selected assistant: {selectedAssistant}{" "}
                    <button
                      className="border px-2 py-1 rounded-lg ms-2"
                      onClick={changeAssistant}
                    >
                      Change assistant
                    </button>
                  </div>
                  {/* Render each message in the conversation */}
                  {conversation.map((message, index) => (
                    <Message key={index} message={message} />
                  ))}
                  {/* Placeholder for scrolling to the bottom of the chat */}
                  <div className="w-full h-32 md:h-48 flex-shrink-0 dark:bg-[#212121]"></div>
                  <div ref={bottomOfChatRef}></div>
                </div>
              ) : null}
              {/* Render empty chat on first load */}
              {showEmptyChat ? (
                <div className="pb-10 sm:pt-10 pt-4 px-2 relative w-full flex flex-col h-full">
                  {/* Assistant selection dropdown */}
                  <div className="flex items-center justify-center gap-2">
                    <div className="relative w-full sm:w-1/2 md:w-1/2 lg:w-1/3 xl:w-1/4">
                      <Box>
                        <FormControl
                          fullWidth
                          sx={{
                            ".MuiOutlinedInput-root .MuiOutlinedInput-notchedOutline":
                              {
                                borderColor: "rgba(255, 255, 255, 0.5)",
                              },
                            ".MuiOutlinedInput-root .MuiSvgIcon-root ": {
                              fill: "rgba(255, 255, 255, 0.75) !important",
                            },
                          }}
                        >
                          {/* Assistant selection label */}
                          <InputLabel
                            id="assistant-select-label"
                            sx={{
                              color: "rgba(255, 255, 255, 0.5)",
                              "&.Mui-focused": {
                                color: "rgba(255, 255, 255, 0.75) !important",
                              },
                            }}
                          >
                            Assistant
                          </InputLabel>
                          {/* Assistant selection dropdown */}
                          <Select
                            labelId="assistant-select-label"
                            id="assistant-select"
                            value={selectedAssistant || ""}
                            label="Assistant"
                            onChange={handleAssistantChange}
                            sx={{
                              color: "rgba(255, 255, 255, 0.75)",
                              boxShadow: "none",
                              "&.MuiOutlinedInput-root:hover .MuiOutlinedInput-notchedOutline":
                                {
                                  borderColor: "rgba(255, 255, 255, 0.75)",
                                },
                              "&.MuiOutlinedInput-root.Mui-focused .MuiOutlinedInput-notchedOutline":
                                {
                                  borderColor: "rgba(255, 255, 255, 0.75)",
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
                                    color: "rgb(236, 236, 236)",
                                    backgroundColor:
                                      "rgb(32 33 35 / var(--tw-bg-opacity))",
                                  },
                                },
                              },
                            }}
                          >
                            {/* Map through OPENAI_MODELS_AND_TOOLS to generate MenuItems */}
                            {OPENAI_MODELS_AND_TOOLS.map((item) => (
                              <MenuItem key={item.id} value={item.title}>
                                {item.title}
                              </MenuItem>
                            ))}
                          </Select>
                        </FormControl>
                      </Box>
                    </div>
                  </div>
                  {/* Branding and information */}
                  <div className="font-semibold text-center text-[#ececec] dark:text-white flex flex-col gap-2 items-center justify-center h-screen">
                    <h1 className="text-2xl sm:text-3xl">
                      Next.js GUI for the<br></br> OpenAI Assistants API{" "}
                      <code>v2</code> beta
                    </h1>
                    {/* "Powered by OpenAI" badge */}
                    <Image
                      src="powered-by-openai-badge-outlined-on-dark.svg"
                      width={165.92}
                      height={32}
                      alt="Powered by OpenAI badge"
                      className="pt-3"
                    />
                    {/* Footer information */}
                    <div className="font-normal text-sm pt-6">
                      Made with ❤️ by Rok Benko
                    </div>
                    {/* Social media icons */}
                    <div className="flex pt-0 gap-2 text-3xl sm-text-4xl">
                      <a
                        target="_blank"
                        href="https://www.linkedin.com/in/rokbenko/"
                        className="opacity-50 hover:opacity-75 duration-200"
                      >
                        <FaLinkedin className="scale-75" />
                      </a>
                      <a
                        target="_blank"
                        href="https://stackoverflow.com/users/10347145/rok-benko?tab=profile"
                        className="opacity-50 hover:opacity-75 duration-200"
                      >
                        <FaStackOverflow className="scale-75" />
                      </a>
                      <a
                        target="_blank"
                        href="https://github.com/rokbenko"
                        className="opacity-50 hover:opacity-75 duration-200"
                      >
                        <FaGithub className="scale-75" />
                      </a>
                      <a
                        target="_blank"
                        href="https://www.youtube.com/@CodeAIwithRok"
                        className="opacity-50 hover:opacity-75 duration-200"
                      >
                        <FaYoutube className="scale-75" />
                      </a>
                      <a
                        target="_blank"
                        href="https://www.patreon.com/rokbenko"
                        className="opacity-50 hover:opacity-75 duration-200"
                      >
                        <FaPatreon className="scale-75" />
                      </a>
                    </div>
                  </div>
                </div>
              ) : null}
              {/* Placeholder for additional content */}
              <div className="flex flex-col items-center text-sm dark:bg-[#212121]"></div>
            </div>
          </div>
        </div>
        {/* Form for user input */}
        <div className="absolute bottom-0 left-0 w-full !bg-[#212121] pt-6">
          <form className="stretch mx-2 flex flex-row gap-3 last:mb-2 md:last:mb-6 mx-auto max-w-[768px]">
            <div className="relative flex flex-col h-full flex-1 items-stretch md:flex-col lg:ps-0 lg:pe-0 ps-4 pe-8">
              {/* Display error message if any */}
              {errorMessage ? (
                <div className="mb-2 md:mb-0">
                  <div className="h-full flex ml-1 md:w-full md:m-auto md:mb-2 gap-0 md:gap-2 justify-center">
                    <span className="text-red-500 text-sm">{errorMessage}</span>
                  </div>
                </div>
              ) : null}
              {/* Text area for user input */}
              <Tooltip
                title={
                  !selectedAssistant
                    ? "Please select an assistant you want to chat with using the dropdown at the top of the screen."
                    : ""
                }
                placement="top"
              >
                <div
                  className={`flex flex-col w-full flex-grow pl-4 py-4 pr-12 relative bg-white dark:text-[#ececec] dark:bg-[#2f2f2f] rounded-[26px] shadow-[0_0_20px_rgba(0,0,0,0.025)] dark:shadow-[0_0_20px_rgba(0,0,0,0.025)] ${
                    !selectedAssistant ? "hover:cursor-not-allowed" : ""
                  }`}
                >
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
                    placeholder={`Chat with ${
                      selectedAssistant
                        ? `the ${selectedAssistant}`
                        : "an assistant"
                    }...`}
                    className={`placeholder:text-[#7d7d7d] focus:outline-none focus:shadow-none m-0 w-full resize-none border-0 bg-transparent p-0 pr-7 focus:ring-0 focus-visible:ring-0 dark:bg-transparent pl-2 md:pl-0 ${
                      !selectedAssistant ? "hover:cursor-not-allowed" : ""
                    }`}
                    onChange={(e) => setMessage(e.target.value)}
                    onKeyDown={handleKeypress}
                    disabled={!selectedAssistant}
                  ></textarea>
                  {/* Send button */}
                  <button
                    disabled={isLoading || message?.length === 0}
                    onClick={sendMessage}
                    className={`w-[2rem] h-[2rem] flex justify-center items-center absolute p-1 rounded-[9999px] bottom-3 text-[#ececec] bg-white disabled:bg-[#676767] disabled:text-gray-400 right-2 md:right-3 transition-colors ${
                      !selectedAssistant ? "hover:cursor-not-allowed" : ""
                    }`}
                  >
                    <TbArrowUp className="text-white dark:text-black" />
                  </button>
                </div>
              </Tooltip>
            </div>
          </form>
          {/* Informational text */}
          <div className="px-2 py-2 text-center text-xs text-gray-600 dark:text-[#7d7d7d]">
            <span>The assistant can make mistakes. Check important info.</span>
          </div>
        </div>
      </div>
    </div>
  );
}
