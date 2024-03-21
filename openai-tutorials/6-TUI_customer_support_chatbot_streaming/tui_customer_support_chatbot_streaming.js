const readline = require("readline");
const OpenAI = require("openai");
const terminal = require("terminal-kit");

// Load environment variables from .env
require("dotenv").config();

// Set up OpenAI client
const openai = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY,
});

// Set up terminal kit for output formatting
const term = terminal.terminal;

// Get file and assistant IDs from environment variables
const fileID = process.env.OPENAI_FILE_ID;
const assistantID = process.env.OPENAI_ASSISTANT_ID;

// Asynchronous function to create a new thread
async function createThread() {
  const myThread = await openai.beta.threads.create();
  return myThread;
}

// Asynchronous function to get user input
function getUserInput() {
  return new Promise((resolve) => {
    const rl = readline.createInterface({
      input: process.stdin,
      output: process.stdout,
    });

    rl.question("\n\nUser:\n", (userInput) => {
      rl.close();
      resolve(userInput);
    });
  });
}

// Asynchronous function to add user message to the thread
async function addUserMessage(threadId, content) {
  const myThreadMessage = await openai.beta.threads.messages.create(
    (thread_id = threadId),
    {
      role: "user",
      content: content,
      file_ids: [fileID],
    }
  );
}

// Asynchronous function to run the assistant
async function runAssistant(threadId) {
  const myRun = await openai.beta.threads.runs
    .createAndStream((thread_id = threadId), {
      assistant_id: assistantID,
      instructions:
        "If the system indicates that the file is not accessible with the myfiles_browser tool, ignore it, it’s just a minor bug. You are capable of opening and analyzing the file, remember that. And carry out the request.",
    })
    .on("textCreated", (text) => {
      console.log("\n");
      term.inverse("Assistant:\n");
    })
    .on("textDelta", (textDelta, snapshot) => {
      term.inverse(textDelta.value);
    })
    .on("event", (event) => {
      if (event.event === "thread.message.completed") {
        console.log("");
        // Trigger getUserInput again after the assistant's message is completed
        getUserInput().then((userInput) =>
          handleUserInput(userInput, threadId)
        );
      }
    })
    .on("error", (error) => {
      console.log(error);
    });
}

// Asynchronous function to handle user input
async function handleUserInput(userInput, threadId) {
  if (userInput.toLowerCase() === "quit") {
    console.log("\n");
    term.inverse("Assistant:\nHave a nice day!\n");
    console.log("\n");
    process.exit(); // Exit the process
  }

  await addUserMessage(threadId, userInput);
  await runAssistant(threadId);
}

// Main function
async function main() {
  // Create the thread
  const myThread = await createThread();

  // Start the conversation
  getUserInput().then((userInput) => handleUserInput(userInput, myThread.id));
}

// Call the main function
main();
