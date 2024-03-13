import streamlit as st
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
from llama_index.core.llama_dataset.generator import RagDatasetGenerator
from llama_index.llms.openai import OpenAI
from llama_index.core.evaluation import (
    BatchEvalRunner,
    CorrectnessEvaluator,
    FaithfulnessEvaluator,
    RelevancyEvaluator
)
import asyncio
import pandas as pd

# Load data from the specified directory
reader = SimpleDirectoryReader(input_files = ["./dummy_data.json"])
documents = reader.load_data()

# Generate questions from the loaded documents
dataset_generator = RagDatasetGenerator.from_documents(
    documents = documents,
    llm = OpenAI(
        model = "gpt-3.5-turbo",
        api_key = st.secrets["OPENAI_API_KEY"]
    )
)

# Take only the first 3 questions
eval_questions = dataset_generator.generate_dataset_from_nodes()[:3]

# Create a vector index from the loaded documents
vector_index = VectorStoreIndex.from_documents(documents)

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

# Initialize the evaluators
correctness_evaluator = CorrectnessEvaluator(llm = openai_model) # Useful for measuring if the response is correct against a reference answer
faithfulness_evaluator = FaithfulnessEvaluator(llm = openai_model) # Useful for measuring if the response is hallucinated
relevancy_evaluator = RelevancyEvaluator(llm = openai_model) # Useful for measuring if the query is actually answered by the response

# Define an asynchronous function for evaluation
async def evaluate_async():
    # Initialize the BatchEvalRunner
    runner = BatchEvalRunner(
        {
            "correctness": correctness_evaluator,
            "faithfulness": faithfulness_evaluator,
            "relevancy": relevancy_evaluator
        },
        show_progress = True
    )

    # Run the asynchronous evaluation
    eval_result = await runner.aevaluate_queries(
        query_engine = vector_index.as_query_engine(),
        queries = [question.query for question in eval_questions]
    )

    return eval_result

# Run the asynchronous function using asyncio
result = asyncio.run(evaluate_async())

# Extract relevant information from the evaluation results
data = []
for i, question in enumerate(eval_questions):
    correctness_result = result['correctness'][i]
    faithfulness_result = result['faithfulness'][i]
    relevancy_result = result['relevancy'][i]
    data.append({
        'Query': question.query,
        'Correctness response': correctness_result.response,
        'Correctness passing': correctness_result.passing,
        'Correctness feedback': correctness_result.feedback,
        'Correctness score': correctness_result.score,
        'Faithfulness response': faithfulness_result.response,
        'Faithfulness passing': faithfulness_result.passing,
        'Faithfulness feedback': faithfulness_result.feedback,
        'Faithfulness score': faithfulness_result.score,
        'Relevancy response': relevancy_result.response,
        'Relevancy passing': relevancy_result.passing,
        'Relevancy feedback': relevancy_result.feedback,
        'Relevancy score': relevancy_result.score,
    })

# Create a pandas DataFrame
df = pd.DataFrame(data)

# Save the pandas DataFrame to an Excel file using xlsxwriter
with pd.ExcelWriter('eval_report.xlsx', engine = 'xlsxwriter') as writer:
    df.to_excel(writer, sheet_name = 'Sheet1', index = False)