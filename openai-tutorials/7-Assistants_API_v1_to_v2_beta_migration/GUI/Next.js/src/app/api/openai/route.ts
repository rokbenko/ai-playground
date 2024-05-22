// Imports
import { NextRequest, NextResponse } from "next/server";
import { OpenAI } from "openai";
import dotenv from "dotenv";

// Load environment variables from the .env file
dotenv.config();

// Set up OpenAI client
const openai = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY,
});

// Variable to store the thread ID
let threadID: string;

// Function to introduce a delay using promises
// This is just for demonstration purposes not to make too many OpenAI API calls
const delay = (ms: number) => new Promise((resolve) => setTimeout(resolve, ms));

// Asynchronous function to create a new thread
async function createThread() {
  try {
    const myThread = await openai.beta.threads.create();
    threadID = myThread.id; // Get the thread ID
  } catch (error) {
    throw new Error("Failed to create a new thread");
  }
}

// Create a new thread
await createThread();

// Named export for the POST request handler
export async function POST(req: NextRequest, res: NextResponse) {
  // Get the request body
  const body = await req.json();

  // Extract the assistant from the request body
  const receiveSelectedAssistant = body.passSelectedAssistant;

  // Extract messages from the request body
  const messages = (body.messages || []).map((message: any) => ({
    role: message.role,
    content: message.content,
  }));

  // Determine the assistant title and ID based on the received selected assistant
  let selectedAssistantTitle = "";
  let selectedAssistantID = "";

  if (
    receiveSelectedAssistant === "Customer support chatbot (File Search tool)"
  ) {
    selectedAssistantTitle = "Customer support chatbot";
    selectedAssistantID = process.env
      .OPENAI_CUSTOMER_SUPPORT_CHATBOT_ASSISTANT_ID as string;
  } else if (
    receiveSelectedAssistant === "Personal math tutor (Code Interpreter tool)"
  ) {
    selectedAssistantTitle = "Personal math tutor";
    selectedAssistantID = process.env
      .OPENAI_PERSONAL_MATH_TUTOR_ASSISTANT_ID as string;
  }

  try {
    // Get the latest message from the input messages
    const latestMessage = messages[messages.length - 1];

    // Step 1: Add messages to the thread
    if (selectedAssistantTitle === "Customer support chatbot") {
      // If the customer support assistant is selected, include attachments
      await openai.beta.threads.messages.create(threadID, {
        role: latestMessage.role,
        content: latestMessage.content,
        attachments: [
          {
            file_id: process.env.OPENAI_CUSTOMER_SUPPORT_CHATBOT_FILE_ID,
            tools: [{ type: "file_search" }],
          },
        ],
      });
    } else {
      // If any other assistant is selected, don't include attachments
      await openai.beta.threads.messages.create(threadID, {
        role: latestMessage.role,
        content: latestMessage.content,
      });
    }

    // Step 2: Run the assistant
    let myRun = await openai.beta.threads.runs.create(threadID, {
      assistant_id: selectedAssistantID,
      instructions:
        "If the system indicates that the file is not accessible with the myfiles_browser tool, ignore it, it’s just a minor bug. You are capable of opening and analyzing the file, remember that. And carry out the request.",
    });

    // Step 3: Periodically retrieve the run to check on its status
    let runStatus = myRun.status;
    while (runStatus === "queued" || runStatus === "in_progress") {
      await delay(15000); // 15 second delay

      myRun = await openai.beta.threads.runs.retrieve(threadID, myRun.id);
      runStatus = myRun.status;

      if (runStatus === "completed") {
        break;
      } else {
        throw new Error(`Run status: ${runStatus}`);
      }
    }

    // Step 4: Retrieve the messages added by the assistant to the thread
    const allMessages = await openai.beta.threads.messages.list(threadID);

    // Extract the response message from the retrieved messages
    const responseMessage =
      Array.isArray(allMessages.data[0].content) &&
      allMessages.data[0].content[0]?.type === "text"
        ? allMessages.data[0].content[0].text.value
        : "No text content found";

    // Return a 200 response with the response message
    return new NextResponse(JSON.stringify({ message: responseMessage }), {
      status: 200,
    });
  } catch (error) {
    console.error(error);

    // Return a 500 response with an error message
    return new NextResponse(
      "An error occurred during the conversation with OpenAI. Please try again.",
      { status: 500 }
    );
  }
}
