import { NextApiRequest, NextApiResponse } from "next";
import { GPT_35_MODEL, GPT_4_MODEL } from "@/shared/constants";
import { OpenAIModel } from "@/types/model";
import { OpenAI } from "openai";
import {
  ChatCompletionMessageParam,
  ChatCompletionFunctionMessageParam,
} from "openai/resources/chat";

const openai = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY,
});

export default async function handler(
  req: NextApiRequest,
  res: NextApiResponse
) {
  if (req.method !== "POST") {
    res.status(405).json({ error: "Method not allowed" });
    return;
  }

  const body = req.body;
  const messages = (body?.messages || []) as ChatCompletionMessageParam[];
  const model = GPT_35_MODEL.name
    ? (GPT_35_MODEL as OpenAIModel)
    : (GPT_4_MODEL as OpenAIModel);

  try {
    const promptMessage: ChatCompletionMessageParam = {
      role: "system",
      content: "You are ChatGPT. Respond to the user like you normally would.",
    };

    const initialMessages: ChatCompletionMessageParam[] = messages.splice(0, 3);

    const latestMessages: ChatCompletionMessageParam[] = messages
      .slice(-5)
      .map((message) => {
        if (message.role === "function") {
          return {
            role: message.role,
            content: message.content,
            name: "your_function_name",
          } as ChatCompletionFunctionMessageParam;
        } else {
          return {
            role: message.role,
            content: message.content,
          } as ChatCompletionMessageParam;
        }
      });

    const completion = await openai.chat.completions.create({
      model: model.id,
      temperature: 0.5,
      messages: [promptMessage, ...initialMessages, ...latestMessages],
    });

    const responseMessage = completion.choices[0]?.message?.content?.trim();

    if (!responseMessage) {
      res
        .status(400)
        .json({ error: "Unable get response from OpenAI. Please try again." });
    }

    res.status(200).json({ message: responseMessage });
  } catch (error) {
    console.error(error);
    res.status(500).json({
      error: "An error occurred during ping to OpenAI. Please try again.",
    });
  }
}
