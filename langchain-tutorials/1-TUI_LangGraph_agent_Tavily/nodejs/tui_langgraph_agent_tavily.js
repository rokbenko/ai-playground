// Imports
import dotenv from "dotenv";
import readline from "readline";
import { ChatOpenAI } from "@langchain/openai";
import { TavilySearchResults } from "@langchain/community/tools/tavily_search";
import { createReactAgent } from "@langchain/langgraph/prebuilt";
import { HumanMessage } from "@langchain/core/messages";
import term from "terminal-kit";

// Initialize dotenv to load environment variables
dotenv.config();

// Initialize Terminal Kit for better output formatting and visualization
const tk = term.terminal;

// Initialize OpenAI LLM
const llm = new ChatOpenAI({
  apiKey: process.env.OPENAI_API_KEY,
  modelName: "gpt-3.5-turbo",
});

// Initialize Tavily
const tavily = new TavilySearchResults({
  maxResults: 3,
});

// Create a LangGraph agent
const langgraphAgent = createReactAgent({
  llm: llm,
  tools: [tavily],
});

// Define an asynchronous function to get the user question
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

// Define a function to process chunks from the agent
function processChunks(chunk) {
  /**
   * Processes a chunk from the agent and displays information about tool calls or the agent's answer.
   *
   * @param {Object} chunk - The chunk to be processed.
   * @return {void}
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
    const agentAnswer = await langgraphAgent.stream({
      messages: [new HumanMessage({ content: userQuestion })],
    });

    // Process the chunks from the agent
    for await (const chunk of agentAnswer) {
      processChunks(chunk);
    }
  }
}

// Call the main function
main();
