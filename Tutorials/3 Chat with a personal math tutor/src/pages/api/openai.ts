import { NextApiRequest, NextApiResponse } from "next";
import { OpenAI } from "openai";
import dotenv from "dotenv";

dotenv.config();

const openai = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY,
});

const delay = (ms: any) => new Promise((resolve) => setTimeout(resolve, ms));

export default async function handler(
  req: NextApiRequest,
  res: NextApiResponse
) {
  if (req.method !== "POST") {
    res.status(405).json({ error: "Method not allowed" });
    return;
  }

  const body = req.body;
  const messages = (body?.messages || []).map((message: any) => ({
    role: message.role,
    content: message.content,
  }));

  try {
    const assistantId = process.env.OPENAI_ASSISTANT_ID as string;
    const threadId = process.env.OPENAI_THREAD_ID as string;

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

    const responseMessage =
      Array.isArray(allMessages.data[0].content) &&
      allMessages.data[0].content[0]?.type === "text"
        ? allMessages.data[0].content[0].text.value
        : "No text content found";

    res.status(200).json({ message: responseMessage });
  } catch (error) {
    console.error(error);
    res.status(500).json({
      error:
        "An error occurred during the conversation with OpenAI. Please try again.",
    });
  }
}
