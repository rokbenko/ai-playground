import streamlit as st
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
from llama_index.core.evaluation import RelevancyEvaluator
from llama_index.core.llama_dataset.generator import RagDatasetGenerator
from llama_index.llms.openai import OpenAI
import pandas as pd

# Load data from the specified directory
reader = SimpleDirectoryReader(input_files = ["./dummy_data.json"])
documents = reader.load_data()

# Generate questions from the loaded documents
data_generator = RagDatasetGenerator.from_documents(documents)
eval_questions = data_generator.generate_questions_from_nodes()[:3]  # Take only the first 3 questions

# Initialize the OpenAI model
openai_model = OpenAI(
    system_prompt = "You are a helpful travel assistant. When asked a question, answer from the data directory. \
        If you don't know the answer, say 'Oh, snap! It seems I've hit a road bump in my knowledge highway. \
        No worries, though! How about we detour to another fantastic journey waiting for you in the directory?'. \
        If you know the answer, please provide trip information not in a list but in text.",
    model = "gpt-3.5-turbo",
    api_key = st.secrets["OPENAI_API_KEY"],
    max_tokens = 250
)

# Initialize the evaluator for assessing response relevancy
evaluator = RelevancyEvaluator(llm = openai_model)

# Create a vector index from the loaded documents
vector_index = VectorStoreIndex.from_documents(documents)

# Create an empty DataFrame to store all evaluation results
all_eval_df = pd.DataFrame(
    columns = ["Query", "Response", "Source", "Evaluation Result", "Reasoning"]
)

# Function to display evaluation results and update the global DataFrame
def display_eval_df(query: str, response, eval_result: str) -> None:
    eval_df = pd.DataFrame(
        {
            "Query": [query],
            "Response": [str(response)],
            "Source": [response.source_nodes[0].node.get_content()],
            "Evaluation Result": "Pass" if eval_result.passing else "Fail",
            "Reasoning": [eval_result.feedback],
        }
    )

    print(eval_df)

    # Append the DataFrame to the global DataFrame
    global all_eval_df
    all_eval_df = pd.concat([all_eval_df, eval_df], ignore_index = True)

# Loop through each question, query the vector index, evaluate the response, and display the results
for question in eval_questions:
    query_engine = vector_index.as_query_engine()
    response_vector = query_engine.query(question.query)
    eval_result = evaluator.evaluate_response(
        query = question.query,
        response = response_vector
    )

    display_eval_df(question.query, response_vector, eval_result)

# Save the global DataFrame to an Excel file using xlsxwriter
with pd.ExcelWriter('eval_result.xlsx', engine = 'xlsxwriter') as writer:
    all_eval_df.to_excel(writer, sheet_name = 'Sheet1', index = False)