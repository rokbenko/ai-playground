import { OpenAIModel } from "@/types/model";

export const CODE_INTERPRETER = {
  name: "GPT-4 (gpt-4) w/ the Assistants API using the Code Interpreter tool",
  id: "gpt-4",
  available: true,
};

export const OPENAI_MODELS: OpenAIModel[] = [CODE_INTERPRETER];
