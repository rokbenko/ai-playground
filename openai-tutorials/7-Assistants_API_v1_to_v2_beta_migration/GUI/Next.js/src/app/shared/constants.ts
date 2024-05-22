import { OpenAImodelAndTool } from "../types/OpenAImodelAndTool";

export const CUSTOMER_SUPPORT_CHATBOT = {
  title: "Customer support chatbot (File Search tool)",
  id: "customer-support-chatbot",
  openAImodel: "gpt-3.5-turbo",
  openAItool: "file_search",
};

export const PERSONAL_MATH_TUTOR = {
  title: "Personal math tutor (Code Interpreter tool)",
  id: "personal-math-tutor",
  openAImodel: "gpt-3.5-turbo",
  openAItool: "code_interpreter",
};

export const OPENAI_MODELS_AND_TOOLS: OpenAImodelAndTool[] = [
  CUSTOMER_SUPPORT_CHATBOT,
  PERSONAL_MATH_TUTOR,
];
