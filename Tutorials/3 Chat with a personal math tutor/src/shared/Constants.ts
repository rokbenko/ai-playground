import { OpenAIModel } from "@/types/model";

export const GPT_35_MODEL = {
  name: "GPT-3.5 (gpt-3.5-turbo)",
  id: "gpt-3.5-turbo",
  available: true,
};

export const GPT_4_MODEL = {
  name: "GPT-4 (gpt-4)",
  id: "gpt-4",
  available: true,
};

export const OPENAI_MODELS: OpenAIModel[] = [GPT_35_MODEL, GPT_4_MODEL];
