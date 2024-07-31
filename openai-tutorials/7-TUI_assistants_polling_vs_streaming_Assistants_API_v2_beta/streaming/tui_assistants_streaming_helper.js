const readline = require("readline");
const dotenv = require("dotenv");
const OpenAI = require("openai");
const { OpenAIError } = require("openai");
const terminalKit = require("terminal-kit");

// Load environment variables from the .env file
dotenv.config();

// Initialize OpenAI client with the API key from environment variables
const client = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY,
});

// Initialize Terminal Kit for better output formatting and visualization
const outputFormatter = terminalKit.terminal;

// Initialize variables
const attachments = [];
const myFiles = [];

// Get assistant ID from environment variables starting with "OPENAI_ASSISTANT_ID_"
const assistantID = process.env.OPENAI_ASSISTANT_ID;

// Get all file IDs from environment variables
// Collect all environment variables starting with "OPENAI_FILE_ID_"
const fileIDs = Object.fromEntries(
  Object.entries(process.env).filter(([key, value]) =>
    key.startsWith("OPENAI_FILE_ID_")
  )
);

// Convert the object with key-value pairs (i.e., dictionary) to an array containing a list of values
const fileIDvalues = Object.values(fileIDs);

// Display the header and subheader
outputFormatter.defaultColor(
  "\nTerminal user interface for the OpenAI Assistants API v2 beta\nMade with ❤️  by Rok Benko\n"
);

// Check if assistant ID is added in the .env file and display an error message if not
if (!assistantID) {
  outputFormatter.red(
    "\nExiting the script...\nPlease edit the .env file and add the environment variable OPENAI_ASSISTANT_ID. Then run the script again.\n\n"
  );
  process.exit(1);
}

// Define an async function to get user input
function userInput(message) {
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

// Define an async function to retrieve assistant details
async function retrieveAssistantDetails() {
  try {
    // Retrieve assistant details
    const assistantDetails = await client.beta.assistants.retrieve(assistantID);

    // Initialize variables
    let getName = "";
    let getInstructions = "";
    let getModel = "";

    // Get assistant name
    if (assistantDetails.name) {
      getName = assistantDetails.name;
    }

    // Get assistant instructions
    if (assistantDetails.instructions) {
      getInstructions = assistantDetails.instructions;
    }

    // Get assistant LLM
    if (assistantDetails.model) {
      getModel = assistantDetails.model;
    }

    // Get assistant tools
    const allTools = [];

    if (assistantDetails.tools) {
      for (const tool of assistantDetails.tools) {
        if (tool) {
          allTools.push(tool.type);
        }
      }
    }

    // Display assistant details
    outputFormatter.bgBlue("\nAssistant found in the .env file");
    outputFormatter.blue(`\nAssistant: ${getName}`);
    outputFormatter.blue(`\nInstructions: ${getInstructions}`);
    outputFormatter.blue(`\nTools: ${allTools.join(", ")}`);
    outputFormatter.blue(`\nLLM: ${getModel}\n`);
  } catch (error) {
    // Handle error when retrieving assistant details
    if (error instanceof OpenAIError) {
      outputFormatter.red(
        `\nExiting the script...\nError retrieving assistant details:\n${error.message}\n\n`
      );
    } else {
      outputFormatter.red(
        `\nExiting the script...\nUnexpected error retrieving assistant details:\n${error.message}\n\n`
      );
    }
    process.exit(1);
  }
}

// Define an async function to check if files are added in the .env file
async function checkFiles() {
  // Check if file IDs are added in the .env file
  if (fileIDvalues.length === 0) {
    // If no, display a warning message
    outputFormatter.yellow(
      "\nWarning: There are no environment variables starting with OPENAI_FILE_ID_ added in the .env file. Consequently, no files will be added to the assistant.\n\n"
    );

    // Ask the user if they are okay with no files being added to the assistant
    const confirm = await userInput("Are you okay with this? (y/n): ");

    // If no, exit the script
    if (confirm.toLowerCase() === "n" || confirm.toLowerCase() === "no") {
      outputFormatter.red(
        "\nExiting the script...\nPlease edit the .env file and add environment variables starting with OPENAI_FILE_ID_. Then run the script again.\n\n"
      );
      process.exit(1);
    }
  } else {
    // If yes, display the files
    console.log("");
    outputFormatter.bgBlue("Files found in the .env file\n");

    for (const value of fileIDvalues) {
      // Initialize variables
      let fileDetails = "";

      try {
        // Retrieve file details
        fileDetails = await client.files.retrieve((file_id = value));
      } catch (error) {
        // Handle error when retrieving file details
        if (error instanceof OpenAIError) {
          outputFormatter.red(
            `\nExiting the script...\nError retrieving file details:\n${error.message}\n\n`
          );
        } else {
          outputFormatter.red(
            `\nExiting the script...\nUnexpected error retrieving file details:\n${error.message}\n\n`
          );
        }
        process.exit(1);
      }

      // Get file name
      const getFilename = fileDetails.filename;

      console.log(`File: ${getFilename}`);

      // Ask user for the tool
      const addTool = await userInput(
        `Please add a tool for ${getFilename} file  (code_interpreter/file_search): `
      );

      // If invalid tool is entered, display an error message
      if (
        addTool.toLowerCase() !== "code_interpreter" &&
        addTool.toLowerCase() !== "file_search"
      ) {
        outputFormatter.red(
          `\nExiting the script...\nYou entered an invalid tool. A tool must be either code_interpreter or file_search. Please try again.\n\n`
        );
        process.exit(1);
      }

      // Add file details to attachments
      attachments.push({
        fileName: getFilename,
        fileID: value,
        tools: [{ type: addTool }],
      });

      // Generate table
      await generateTable();
    }
  }
}

// Define an async function to generate a table
async function generateTable() {
  // Define the initial table structure with headers
  let tableData = [["File name", "File ID", "Tool"]];

  for (const attachment of attachments) {
    // Get file name
    const getFilename = attachment.fileName;

    // Get file ID
    const getFileID = attachment.fileID;
    const getFileIDmasked =
      "file-" + "*".repeat(getFileID.length - 5) + getFileID.slice(-5);

    // Get tools
    const getTools = attachment.tools.map((tool) => tool.type).join(", ");

    // Add a new row to the table data
    tableData.push([getFilename, getFileIDmasked, getTools]);
  }

  // Generate the table using the collected data
  let table = outputFormatter.table(tableData, {
    width: 80,
  });
}

// Define an async function to create a new thread
async function createThread() {
  try {
    // Create a new thread
    const myThread = await client.beta.threads.create();

    return myThread;
  } catch (error) {
    // Handle error when creating a new thread
    if (error instanceof OpenAIError) {
      outputFormatter.red(
        `\nExiting the script...\nError creating a new thread:\n${error.message}\n\n`
      );
    } else {
      outputFormatter.red(
        `\nExiting the script...\nUnexpected error creating a new thread:\n${error.message}\n\n`
      );
    }
    process.exit(1);
  }
}

// Define an async function to add user message to the thread
async function addUserMessage(myThread, userInput) {
  try {
    // Check if file IDs are added in the .env file
    if (fileIDvalues.length === 0) {
      // If no, don't add the attachments parameter
      // Add the user question to the thread messages
      const myThreadMessage = await client.beta.threads.messages.create(
        (thread_id = myThread),
        {
          role: "user",
          content: userInput,
        }
      );

      return myThreadMessage;
    } else {
      // If yes, add the attachments parameter

      // Iterate over attachments
      for (const attachment of attachments) {
        const fileID = attachment.fileID;
        const tools = attachment.tools;

        // Construct the attachment object with key-value pairs (i.e., dictionary)
        const attachmentObject = {
          file_id: fileID,
          tools: tools,
        };

        // Push the constructed attachment to myFiles
        myFiles.push(attachmentObject);
      }

      // Add the user question to the thread messages
      const myThreadMessage = await client.beta.threads.messages.create(
        (thread_id = myThread),
        {
          role: "user",
          content: userInput,
          attachments: myFiles, // Change from v1 to v2 beta: Messages have the attachments parameter instead of the file_ids parameter
        }
      );

      return myThreadMessage;
    }
  } catch (error) {
    // Handle error when adding the user question to the thread messages
    if (error instanceof OpenAIError) {
      outputFormatter.red(
        `\nExiting the script...\nError adding the user question to thread messages:\n${error.message}\n\n`
      );
    } else {
      outputFormatter.red(
        `\nExiting the script...\nUnexpected error adding the user question to thread messages:\n${error.message}\n\n`
      );
    }
    process.exit(1);
  }
}

// Define an async function to run the assistant and stream its answer
async function runAssistantAndStreamAnswer(myThread) {
  // Run the assistant and stream its answer
  const myRun = await client.beta.threads.runs
    .stream((thread_id = myThread), {
      assistant_id: assistantID,
      instructions:
        "If the system indicates that the file is not accessible, ignore it. It’s just a minor bug. You are capable of opening and analyzing the file, remember that. And carry out the request.",
    })
    .on("textCreated", (text) => {
      console.log("");
      outputFormatter.inverse("Assistant:\n");
    })
    .on("textDelta", (textDelta, snapshot) => {
      outputFormatter.inverse(textDelta.value);
    })
    .on("event", (event) => {
      if (event.event === "thread.message.completed") {
        console.log("");
        // Trigger the userInput function again after the assistant answer is streamed
        userInput("\nUser:\n").then((userInput) =>
          handleUserInput(myThread, userInput)
        );
      }
    })
    .on("error", (error) => {
      // Handle error when running and streaming the assistant answer
      if (error instanceof OpenAIError) {
        outputFormatter.red(
          `\nExiting the script...\nError running and streaming the assistant answer:\n${error.message}\n\n`
        );
      } else {
        outputFormatter.red(
          `\nExiting the script...\nUnexpected error running and streaming the assistant answer:\n${error.message}\n\n`
        );
      }
      process.exit(1);
    });
}

// Define an async function to handle user input
async function handleUserInput(myThread, userInput) {
  // Check if the user wants to quit the chat
  // If yes, exit the script
  if (userInput.toLowerCase() === "quit") {
    console.log("");
    outputFormatter.inverse("Assistant:\nHave a nice day!\n");
    console.log("");
    process.exit(1);
  } else {
    // If no, add the user message to the thread, run the assistant and stream its answer
    await addUserMessage(myThread, userInput);
    await runAssistantAndStreamAnswer(myThread);
  }
}

// Define an async function to execute the main logic
async function main() {
  // Retrieve assistant details
  await retrieveAssistantDetails();

  // Check if files are added in the .env file
  await checkFiles();

  // Step 1: Create a new thread
  const myThread = await createThread();

  // Start the chat
  // Step 2: Get the user question and display it
  // Step 3: Add the user question to the thread messages
  // Step 4: Run the assistant and stream its answer
  userInput("\nUser:\n").then((userInput) =>
    handleUserInput(myThread.id, userInput)
  );
}

// Call the main function
main();
