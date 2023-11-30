import * as React from "react";
import { useEffect, useRef, useState } from "react";
import Message from "./message";
import Dialog from "./dialog";
import Image from "next/image";
import useAutoResizeTextArea from "@/hooks/useAutoResizeTextArea";
import { GPT_35_MODEL, GPT_4_MODEL } from "@/shared/constants";
import Box from "@mui/material/Box";
import InputLabel from "@mui/material/InputLabel";
import MenuItem from "@mui/material/MenuItem";
import FormControl from "@mui/material/FormControl";
import Select from "@mui/material/Select";
import { FiEdit } from "react-icons/fi";
import { TbArrowUp } from "react-icons/tb";
import { RxHamburgerMenu } from "react-icons/rx";
import { FaGithub } from "react-icons/fa";
import { FaStackOverflow } from "react-icons/fa";
import { FaLinkedin } from "react-icons/fa";
import { FaYoutube } from "react-icons/fa";

const Chat = (props: any) => {
  const { toggleComponentVisibility } = props;

  const [isLoading, setIsLoading] = useState(false);
  const [errorMessage, setErrorMessage] = useState("");
  const [showEmptyChat, setShowEmptyChat] = useState(true);
  const [conversation, setConversation] = useState<any[]>([]);
  const [message, setMessage] = useState("");
  const textAreaRef = useAutoResizeTextArea();
  const bottomOfChatRef = useRef<HTMLDivElement>(null);
  const [selectedModel, setSelectedModel] = React.useState("");

  const handleModelChange = (event: any) => {
    setSelectedModel(event.target.value);
  };

  useEffect(() => {
    if (textAreaRef.current) {
      textAreaRef.current.style.height = "24px";
      textAreaRef.current.style.height = `${textAreaRef.current.scrollHeight}px`;
    }
  }, [message, textAreaRef]);

  useEffect(() => {
    if (bottomOfChatRef.current) {
      bottomOfChatRef.current.scrollIntoView({ behavior: "smooth" });
    }
  }, [conversation]);

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

    // Add the message to the conversation
    setConversation([
      ...conversation,
      { content: message, role: "user" },
      { content: null, role: "system" },
    ]);

    // Clear the message & remove empty chat
    setMessage("");
    setShowEmptyChat(false);

    try {
      const response = await fetch(`/api/openai`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          messages: [...conversation, { content: message, role: "user" }],
          model: selectedModel,
        }),
      });

      if (response.ok) {
        const data = await response.json();

        // Add the message to the conversation
        setConversation([
          ...conversation,
          { content: message, role: "user" },
          { content: data.message, role: "system" },
        ]);
      } else {
        console.error(response);
        setErrorMessage(response.statusText);
      }

      setIsLoading(false);
    } catch (error: any) {
      console.error(error);
      setErrorMessage(error.message);

      setIsLoading(false);
    }
  };

  const handleKeypress = (e: any) => {
    // It's triggers by pressing the enter key
    if (e.keyCode == 13 && !e.shiftKey) {
      sendMessage(e);
      e.preventDefault();
    }
  };

  return (
    <div className="flex max-w-full flex-1 flex-col">
      <div className="sticky top-0 min-h-[40px] z-10 flex items-center bg-gray-900 text-gray-200 md:hidden">
        <button
          type="button"
          className="-ml-0.5 -mt-0.5 inline-flex h-10 w-10 items-center justify-center rounded-lg hover:text-gray-900 focus:outline-none focus:ring-2 focus:ring-inset focus:ring-white dark:hover:text-white"
          onClick={toggleComponentVisibility}
        >
          <span className="sr-only">Open sidebar</span>
          <RxHamburgerMenu size={18} />
        </button>
        <h1 className="flex-1 text-center text-base font-normal">New chat</h1>
        <button type="button" className="px-3">
          <FiEdit size={14} />
        </button>
      </div>
      <div className="relative h-full w-full transition-width flex flex-col overflow-hidden items-stretch flex-1">
        <div className="flex-1 overflow-hidden">
          <div className="relative h-full dark:bg-gray-800">
            <div className="w-full h-full overflow-y-auto">
              {!showEmptyChat && conversation.length > 0 ? (
                <div className="flex flex-col items-center text-sm bg-gray-800">
                  <div className="flex w-full items-center justify-center gap-1 border-b border-black/10 bg-gray-50 p-3 text-gray-500 dark:border-gray-900/50 dark:bg-gray-700 dark:text-gray-300">
                    Model:{" "}
                    {selectedModel === GPT_35_MODEL.name
                      ? GPT_35_MODEL.name
                      : GPT_4_MODEL.name}
                  </div>
                  {conversation.map((message, index) => (
                    <Message key={index} message={message} />
                  ))}
                  <div className="w-full h-32 md:h-48 flex-shrink-0"></div>
                  <div ref={bottomOfChatRef}></div>
                </div>
              ) : null}
              {showEmptyChat ? (
                <div className="py-10 px-2 relative w-full flex flex-col h-full">
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
                            ".MuiList-root": {
                              backgroundColor: "green",
                            },
                          }}
                        >
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
                            <MenuItem value={GPT_35_MODEL.name}>
                              {GPT_35_MODEL.name}
                            </MenuItem>
                            <MenuItem value={GPT_4_MODEL.name}>
                              {GPT_4_MODEL.name}
                            </MenuItem>
                          </Select>
                        </FormControl>
                      </Box>
                    </div>
                  </div>
                  <div className="text-2xl sm:text-4xl font-semibold text-center text-black dark:text-white flex flex-col gap-2 items-center justify-center h-screen">
                    <h1>chatMATH</h1>
                    <Image
                      src="/powered-by-openai-badge-outlined-on-dark.svg"
                      width={165.92}
                      height={32}
                      alt="Powered by OpenAI badge"
                      className="pt-3"
                    />
                    <div className="font-normal text-sm pt-4">
                      Made with ❤️ by Rok
                    </div>
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
                        href="https://stackoverflow.com/users/10347145/rok-benko?tab=profile"
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
                        href="https://www.youtube.com/@codewithrok"
                        className="opacity-50 hover:opacity-100 duration-200"
                      >
                        <FaYoutube className="scale-75" />
                      </a>
                    </div>
                  </div>
                </div>
              ) : null}
              <div className="flex flex-col items-center text-sm dark:bg-gray-800"></div>
            </div>
          </div>
        </div>
        <div className="absolute bottom-0 left-0 w-full dark:border-white/20 md:border-transparent md:dark:border-transparent md:bg-vert-light-gradient bg-white dark:bg-gray-800 md:!bg-transparent dark:md:bg-vert-dark-gradient pt-2">
          <form className="stretch mx-2 flex flex-row gap-3 last:mb-2 md:mx-4 md:last:mb-6 lg:mx-auto lg:max-w-2xl xl:max-w-3xl">
            <div className="relative flex flex-col h-full flex-1 items-stretch md:flex-col">
              {errorMessage ? (
                <div className="mb-2 md:mb-0">
                  <div className="h-full flex ml-1 md:w-full md:m-auto md:mb-2 gap-0 md:gap-2 justify-center">
                    <span className="text-red-500 text-sm">{errorMessage}</span>
                  </div>
                </div>
              ) : null}
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
                  // rows={1}
                  placeholder="Message chatMATH..."
                  className="focus:outline-none focus:shadow-none m-0 w-full resize-none border-0 bg-transparent p-0 pr-7 focus:ring-0 focus-visible:ring-0 dark:bg-transparent pl-2 md:pl-0"
                  onChange={(e) => setMessage(e.target.value)}
                  onKeyDown={handleKeypress}
                ></textarea>
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
          <div className="absolute bottom-8 right-8">
            <Dialog />
          </div>
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

export default Chat;
