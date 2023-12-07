// Importing necessary modules and libraries
import { NextApiRequest, NextApiResponse } from "next";
import { OpenAI } from "openai";
import dotenv from "dotenv";

// Load environment variables from a .env file
dotenv.config();

// Create an instance of the OpenAI class with the API key from the environment variables
const openai = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY,
});

// Function to introduce a delay using promises
const delay = (ms: any) => new Promise((resolve) => setTimeout(resolve, ms));

// Exporting the default function for handling API requests
export default async function handler(
  req: NextApiRequest,
  res: NextApiResponse
) {
  // Check if the request method is not POST
  if (req.method !== "POST") {
    // Return a 405 Method Not Allowed response
    res.status(405).json({ error: "Method not allowed" });
    return;
  }

  // Extract messages from the request body
  const body = req.body;
  const messages = (body?.messages || []).map((message: any) => ({
    role: message.role,
    content: message.content,
  }));

  try {
    // Get OpenAI assistant and thread IDs from environment variables
    const assistantId = process.env.OPENAI_ASSISTANT_ID as string;
    const threadId = process.env.OPENAI_THREAD_ID as string;

    // Get the latest message from the input messages
    const latestMessage = messages[messages.length - 1];

    // Step 1: Add Messages to the Thread
    await openai.beta.threads.messages.create(threadId, {
      role: latestMessage.role,
      content: latestMessage.content,
    });

    // Step 2: Run the Assistant
    let myRun = await openai.beta.threads.runs.create(threadId, {
      assistant_id: assistantId,
      instructions: "Please address the user as Rok Benko.",
    });

    // Step 3: Periodically retrieve the Run to check on its status
    let runStatus = myRun.status;
    while (runStatus !== "completed") {
      await delay(15000); // 15 seconds delay
      myRun = await openai.beta.threads.runs.retrieve(threadId, myRun.id);
      runStatus = myRun.status;
    }

    // Step 4: Retrieve the Messages added by the Assistant to the Thread
    const allMessages = await openai.beta.threads.messages.list(threadId);

    // Extract the response message from the retrieved messages
    const responseMessage =
      Array.isArray(allMessages.data[0].content) &&
      allMessages.data[0].content[0]?.type === "text"
        ? allMessages.data[0].content[0].text.value
        : "No text content found";

    // Return a 200 OK response with the response message
    res.status(200).json({ message: responseMessage });
  } catch (error) {
    // Handle errors and return a 500 Internal Server Error response
    console.error(error);
    res.status(500).json({
      error:
        "An error occurred during the conversation with OpenAI. Please try again.",
    });
  }
}
