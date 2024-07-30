# #3 Evaluation of a travel recommendation RAG

<br>

## 📖 Description 📖

Evaluation of the <a href="https://github.com/rokbenko/ai-playground/tree/main/llamaindex-tutorials/2-GUI_travel_recommendation_RAG">#2 GUI for a travel recommendation RAG</a> tutorial.

<br>

## 🧠 Learning goal 🧠

- **Evaluating a RAG using LlamaIndex:** We will evaluate a travel recommendation RAG built in the [previous](https://github.com/rokbenko/ai-playground/tree/main/llamaindex-tutorials/2-GUI_travel_recommendation_RAG) tutorial. The steps include:

1. Loading and preprocessing data:
    - Load data from a JSON file using LlamaIndex's `SimpleDirectoryReader`.
    - Generate questions from the loaded documents using LlamaIndex's `RagDatasetGenerator`.
2. Creating a vector index:
    - Create a vector index from the documents with LlamaIndex's `VectorStoreIndex` to facilitate efficient data retrieval during evaluation.
3. Initializing OpenAI LLM:
    - Set up the OpenAI LLM with specific system prompts and configuration to handle query processing.
4. Setting up evaluators:
    - Initialize LlamaIndex's evaluation components: `CorrectnessEvaluator`, `FaithfulnessEvaluator`, and `RelevancyEvaluator`.
    - These evaluators will assess the responses based on correctness, faithfulness, and relevancy criteria.
5. Running asynchronous evaluation:
    - Define and run an asynchronous function using LlamaIndex's `BatchEvalRunner` to evaluate the generated questions against the vector index.
    - Handle the evaluation asynchronously to improve efficiency.
6. Compiling and reporting results:
    - Extract relevant evaluation data and compile it into a pandas `DataFrame`.
    - Save the evaluation results to an Excel file for detailed reporting and analysis.

<br>

## 🔥 Working example in Python 🔥

If you run [`travel_recommendation_rag_eval.py`](https://github.com/rokbenko/ai-playground/blob/main/llamaindex-tutorials/3-Eval_travel_recommendation_RAG/travel_recommendation_rag_eval.py), you should get the evaluation report in an <a href="https://github.com/rokbenko/ai-playground/blob/main/llamaindex-tutorials/3-Eval_travel_recommendation_RAG/eval_report.xlsx">Excel file</a>.

<br>

## ⚒️ Tech stack ⚒️

OS:

- Windows `10`

Dependencies:

- [Python](https://www.python.org/) `3.11.8`
- [Streamlit](https://pypi.org/project/streamlit/) `1.31.1`
- [LlamaIndex Python SDK](https://pypi.org/project/llama-index/) `0.10.12`
- [Pandas](https://pypi.org/project/pandas/) `2.2.0`
