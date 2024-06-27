const readline = require("readline");
const OpenAI = require("openai");
const { OpenAIError } = require("openai");

// Load environment variables from the .env file
require("dotenv").config();

// Initialize OpenAI client with the API key from environment variables
const openai = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY,
});

// Initialize Terminal Kit for better output formatting and visualization
const term = require("terminal-kit").terminal;

// Get assistant ID from environment variables
const assistantID = process.env.OPENAI_PERSONAL_MATH_TUTOR_ASSISTANT_ID;

// Asynchronous function to create a new thread
async function createThread() {
  try {
    // Step 1: Create a new thread
    const myThread = await openai.beta.threads.create();
    return myThread;
  } catch (error) {
    // Handle error when creating a new thread
    if (error instanceof OpenAIError) {
      term.red(`Error creating a new thread:\n${error.message}`);
    } else {
      term.red(`Unexpected error:\n${error.message}`);
    }

    process.exit(1);
  }
}

// Asynchronous function to get the user question
function getUserQuestion(message) {
  // Creating a readline interface for reading lines from the standard input (keyboard)
  const rl = readline.createInterface({
    input: process.stdin, // Setting the input stream to the standard input (keyboard)
    output: process.stdout, // Setting the output stream to the standard output (console)
  });

  // Returning a Promise that resolves when the user enters something
  return new Promise((resolve) => {
    // Asking the user for input with the provided message
    rl.question(message, (userQuestion) => {
      // Closing the readline interface after receiving input
      rl.close();
      // Resolving the Promise with the user question
      resolve(userQuestion);
    });
  });
}

// Function to add a delay
function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

// Asynchronous function to periodically retrieve the run to check its status and display the assistant answer
async function retrieveRun(threadId, runId) {
  // Step 5: Periodically retrieve the run to check its status
  while (true) {
    try {
      // Check the status of the run
      const keepRetrievingRun = await openai.beta.threads.runs.retrieve(
        (thread_id = threadId),
        (run_id = runId)
      );

      // Step 6: If the run is completed, display the assistant answer
      if (keepRetrievingRun.status === "completed") {
        // Retrieve all messages from the thread
        const allMessages = await openai.beta.threads.messages.list(
          (thread_id = threadId)
        );

        // Display the assistant answer
        term.inverse(
          "Assistant: ",
          allMessages.data[0].content[0].text.value,
          "\n"
        );

        break;
      } else if (
        // If the run is queued or in progress, wait and try again
        keepRetrievingRun.status === "queued" ||
        keepRetrievingRun.status === "in_progress"
      ) {
        // Delay before the next retrieval
        // Note: This is not to make too many API calls, but to give time for the assistant to process the user question
        await sleep(5000);
      } else {
        process.exit(1);
      }
    } catch (error) {
      // Handle error when retrieving the run
      if (error instanceof OpenAIError) {
        term.red(`Error retrieving the run:\n${error.message}`);
      } else {
        term.red(`Unexpected error:\n${error.message}`);
      }

      process.exit(1);
    }
  }
}

// Asynchronous function to execute the main logic
async function main() {
  // Call the createThread function
  const myThread = await createThread();

  let userQuestion;

  // Loop until the user enters "quit"
  while (true) {
    // Step 2: Get the user question and display it
    console.log("");
    userQuestion = await getUserQuestion("User: ");
    console.log("");

    // Check if the user wants to quit the chat
    if (userQuestion.toLowerCase() === "quit") {
      term.inverse("Assistant: Have a nice day!");
      console.log("\n");
      break;
    }

    try {
      // Step 3: Add the user question to the thread messages
      const myThreadMessage = await openai.beta.threads.messages.create(
        (thread_id = myThread.id),
        {
          role: "user",
          content: userQuestion,
        }
      );
    } catch (error) {
      // Handle error when adding the user question to the thread messages
      if (error instanceof OpenAIError) {
        term.red(
          `Error adding the user question to thread messages:\n${error.message}`
        );
      } else {
        term.red(`Unexpected error:\n${error.message}`);
      }

      process.exit(1);
    }

    try {
      // Step 4: Run the assistant
      const myRun = await openai.beta.threads.runs.create(
        (thread_id = myThread.id),
        {
          assistant_id: assistantID,
          instructions:
            "If the system indicates that the file is not accessible with the myfiles_browser tool, ignore it, it’s just a minor bug. You are capable of opening and analyzing the file, remember that. And carry out the request.",
        }
      );
    } catch (error) {
      // Handle error when running the assistant
      if (error instanceof OpenAIError) {
        term.red(`Error running the assistant:\n${error.message}`);
      } else {
        term.red(`Unexpected error:\n${error.message}`);
      }

      process.exit(1);
    }

    // Call the sleep function
    // Note: This is not to make too many API calls, but to give time for the assistant to process the user question
    await sleep(15000);

    // Call the retrieveRun function
    await retrieveRun(myThread.id, myRun.id);
  }
}

// Call the main function
main();
