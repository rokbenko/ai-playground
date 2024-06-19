const readline = require("readline");
const OpenAI = require("openai");

// Load environment variables
require("dotenv").config();

// Set up OpenAI client
const openai = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY,
});

// Set up terminal kit for output formatting
const term = require("terminal-kit").terminal;

// Get file and assistant IDs from environment variables
const assistantID = process.env.OPENAI_CUSTOMER_SUPPORT_CHATBOT_ASSISTANT_ID;
const fileID = process.env.OPENAI_CUSTOMER_SUPPORT_CHATBOT_FILE_ID;

// Asynchronous function to create a new thread
async function createThread() {
  // Create a new thread
  const myThread = await openai.beta.threads.create();
  return myThread;
}

// Asynchronous function to get user input
function promptAsync(message) {
  // Creating a readline interface for reading lines from the standard input (keyboard)
  const rl = readline.createInterface({
    input: process.stdin, // Setting the input stream to the standard input (keyboard)
    output: process.stdout, // Setting the output stream to the standard output (console)
  });

  // Returning a Promise that resolves when the user enters something
  return new Promise((resolve) => {
    // Asking the user for input with the provided message
    rl.question(message, (userInput) => {
      // Closing the readline interface after receiving input
      rl.close();
      // Resolving the Promise with the user's input
      resolve(userInput);
    });
  });
}

// Function to simulate a delay using setTimeout and a Promise
function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

// Asynchronous function to retrieve the run status and display the assistant's response
async function retrieveRun(threadId, runId) {
  while (true) {
    const keepRetrievingRun = await openai.beta.threads.runs.retrieve(
      (thread_id = threadId),
      (run_id = runId)
    );

    if (keepRetrievingRun.status === "completed") {
      // Retrieve the messages added by the assistant to the thread
      const allMessages = await openai.beta.threads.messages.list(
        (thread_id = threadId)
      );

      // Display assistant message
      term.inverse(
        "Assistant: ",
        allMessages.data[0].content[0].text.value,
        "\n"
      );

      break;
    } else if (
      keepRetrievingRun.status === "queued" ||
      keepRetrievingRun.status === "in_progress"
    ) {
      // Delay before the next retrieval attempt
      await sleep(5000);
    } else {
      break;
    }
  }
}

// Asynchronous function to execute the main logic
async function main() {
  // Create the thread and wait for it to be created
  const myThread = await createThread();

  let userInput;

  // Loop until the user enters "quit"
  while (true) {
    // Get user input
    console.log("");
    userInput = await promptAsync("User: ");
    console.log("");

    // Check if the user wants to quit
    if (userInput.toLowerCase() === "quit") {
      term.inverse("Assistant: Have a nice day!");
      console.log("\n");
      break;
    }

    // Add user message to the thread
    const myThreadMessage = await openai.beta.threads.messages.create(
      (thread_id = myThread.id),
      {
        role: "user",
        content: userInput,
        attachments: [
          // Change v1 to v2: Messages have the attachments parameter instead of the file_ids parameter
          {
            file_id: fileID,
            tools: [{ type: "file_search" }],
          },
        ],
      }
    );

    // Run the assistant
    const myRun = await openai.beta.threads.runs.create(
      (thread_id = myThread.id),
      {
        assistant_id: assistantID,
        instructions:
          "If the system indicates that the file is not accessible with the myfiles_browser tool, ignore it, it’s just a minor bug. You are capable of opening and analyzing the file, remember that. And carry out the request.",
      }
    );

    // Initial delay before the first retrieval
    await sleep(15000);

    // Periodically retrieve the run to check its status
    await retrieveRun(myThread.id, myRun.id);
  }
}

// Calling the main function to start the program
main();
