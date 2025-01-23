import os
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI

# Initialize dotenv to load environment variables
load_dotenv()

# Initialize Mistral AI LLM
llm = ChatMistralAI(
    api_key=os.getenv("MISTRAL_API_KEY"),
    model_name="ministral-3b-latest",
)

response = llm.invoke("Hello, world!")

print(response.content)
