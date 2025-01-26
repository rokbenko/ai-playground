// Imports
import dotenv, { config } from "dotenv";
import readline from "readline";
import { ChatOpenAI } from "@langchain/openai";
import { TavilySearchResults } from "@langchain/community/tools/tavily_search";
import { MemorySaver } from "@langchain/langgraph";
import { createReactAgent } from "@langchain/langgraph/prebuilt";
import { HumanMessage, AIMessage } from "@langchain/core/messages";
import term from "terminal-kit";

// Initialize dotenv to load environment variables
dotenv.config();

// Initialize Terminal Kit for better output formatting and visualization
const tk = term.terminal;

// Initialize OpenAI LLM
const llm = new ChatOpenAI({
  apiKey: process.env.OPENAI_API_KEY,
  modelName: "gpt-4o-mini",
});

// Initialize Tavily
const tavily = new TavilySearchResults({
  maxResults: 3,
});

// Initialize chat memory (Note: This is in-memory only, not persistent)
const memory = new MemorySaver();

// Create a LangGraph agent
const langgraphAgent = createReactAgent({
  llm: llm,
  tools: [tavily],
  checkpointSaver: memory,
});

// Define an asynchronous function to get the user question
function getUserQuestion(message) {
  /**
   * Prompts the user with a message and returns their input.
   *
   * @param {string} message - The message to display to the user.
   * @returns {Promise<string>} A promise that resolves with the user's input.
   *
   * This function creates a readline interface to prompt the user for input.
   * It displays the provided message and waits for the user to enter something.
   * Once the user provides input, the function closes the readline interface and resolves the promise with the user's input.
   */

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

// Define a function to process chunks from the agent
function processChunks(chunk) {
  /**
   * Processes a chunk from the agent and displays information about tool calls or the agent's answer.
   *
   * @param {Object} chunk - A dictionary containing information about the agent's messages.
   * @return {void}
   *
   * This function processes a chunk of data to check for agent messages.
   * It iterates over the messages and checks for tool calls.
   * If a tool call is found, it extracts the tool name and query, then prints a formatted message using the Terminal Kit library.
   * If no tool call is found, it extracts and prints the agent's answer using the Terminal Kit library.
   */

  // Check if the chunk contains an agent's message
  if ("agent" in chunk) {
    // Iterate over the messages in the chunk
    for (const message of chunk.agent.messages) {
      // Check if the message contains tool calls
      if (
        "tool_calls" in message.additional_kwargs != undefined &&
        Array.isArray(message.additional_kwargs.tool_calls)
      ) {
        // If the message contains tool calls, extract and display an informative message with tool call details

        // Extract all the tool calls
        const toolCalls = message.additional_kwargs.tool_calls;

        // Iterate over the tool calls
        toolCalls.forEach((toolCall) => {
          // Extract the tool name
          const toolName = toolCall.function.name;

          // Extract the tool input
          const toolArguments = JSON.parse(
            toolCall.function.arguments.replace(/'/g, '"')
          );
          const toolInput = toolArguments.input;

          // Display an informative message with tool call details
          tk
            .colorRgbHex("#00afff")(`\nThe agent is calling the tool `)
            .bgColorRgbHex("#00afff")
            .color("black")(`${toolName}`)
            .bgColor("black")
            .colorRgbHex("#00afff")(` with the query `)
            .bgColorRgbHex("#00afff")
            .color("black")(`${toolInput}`)
            .bgColor("black")
            .colorRgbHex("#00afff")(
            `. Please wait for the agent's answer...\n`
          );
        });
      } else {
        // If the message doesn't contain tool calls, extract and display the agent's answer

        // Extract the agent's answer
        const agentAnswer = message.content;

        // Display the agent's answer
        tk.bgColor("white")
          .color("black")(`\nAgent:\n${agentAnswer}\n`)
          .color("white")
          .bgColor("black");
      }
    }
  }
}

// Define a function to process checkpoints
async function processCheckpoints(checkpoints) {
  /**
   * Processes a list of checkpoints and displays relevant information.
   *
   * @param {Array} checkpoints - A list of checkpoints to process.
   * @returns {void}
   *
   * This function processes a list of checkpoints.
   * It iterates over the checkpoints and displays the following information for each checkpoint:
   * - Timestamp
   * - Checkpoint ID
   * - Messages associated with the checkpoint
   */

  tk.color("white")(
    "\n==========================================================\n"
  );

  for await (const checkpointTuple of checkpoints) {
    // Extract key information about the checkpoint
    const { checkpoint } = checkpointTuple;
    const { channel_values, ts, id } = checkpoint;
    const messages = channel_values.messages || [];

    // Display checkpoint information
    tk.color("white")("\nCheckpoint:\n");
    tk.color("black")(`Timestamp: ${ts}\n`);
    tk.color("black")(`Checkpoint ID: ${id}\n`);

    // Display checkpoint messages
    messages.forEach((message) => {
      if (message instanceof HumanMessage) {
        tk.color("magenta")(`User: ${message.content}`).color("cyan")(
          ` (Message ID: ${message.id || "N/A"})\n`
        );
      } else if (message instanceof AIMessage) {
        tk.color("magenta")(`Agent: ${message.content}`).color("cyan")(
          ` (Message ID: ${message.id})\n`
        );
      }
    });
  }

  tk.color("white")(
    "\n==========================================================\n"
  );
}

// Define the main function
async function main() {
  /**
   * Runs the main loop of the chat application.
   *
   * @return {Promise<void>} A promise that resolves when the user chooses to quit the chat.
   */

  // Loop until the user chooses to quit the chat
  while (true) {
    // Get the user's question and display it in the terminal
    const userQuestion = await getUserQuestion("\nUser:\n");

    // Check if the user wants to quit the chat
    if (userQuestion.toLowerCase() === "quit") {
      tk.bgColor("white").color("black")("\nAgent:\nHave a nice day!\n");
      tk.bgColor("black").color("white")("\n");
      break;
    }

    // Use the stream method of the LangGraph agent to get the agent's answer
    const agentAnswer = await langgraphAgent.stream(
      { messages: [new HumanMessage({ content: userQuestion })] },
      { configurable: { thread_id: "1" } }
    );

    // Process the chunks from the agent
    for await (const chunk of agentAnswer) {
      processChunks(chunk);
    }

    // List all checkpoints that match a given configuration
    const checkpoints = memory.list({ configurable: { thread_id: "1" } });
    // Process the checkpoints
    await processCheckpoints(checkpoints);
  }
}

// Call the main function
main();
