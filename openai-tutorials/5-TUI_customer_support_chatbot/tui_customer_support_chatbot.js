const readline = require("readline");
const OpenAI = require("openai");
const openai = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY,
});
const term = require("terminal-kit").terminal;

// Load environment variables from .env
require("dotenv").config();

// Existing file and assistant information
// Get file and assistant IDs from environment variables
const fileID = process.env.OPENAI_FILE_ID;
const assistantID = process.env.OPENAI_ASSISTANT_ID;

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
        "\nAssistant: ",
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
        file_ids: [fileID],
      }
    );

    // Run the assistant
    const myRun = await openai.beta.threads.runs.create(
      (thread_id = myThread.id),
      {
        assistant_id: assistantID,
        instructions: "Please address the user as Rok Benko.",
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
