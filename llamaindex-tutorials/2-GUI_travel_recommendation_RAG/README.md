# #2 Streamlit GUI for a travel recommendation RAG with response streaming

<br>

## 📖 Description 📖

Streamlit GUI for a travel recommendation RAG with response streaming using LlamaIndex with an OpenAI LLM.

<br>

## 🚀 Installation 🚀

To start using the app, follow these steps:

1. Clone the repository: `git clone https://github.com/rokbenko/ai-playground.git`
2. Change the directory: `cd ai-playground/llamaindex-tutorials/2-GUI_travel_recommendation_RAG`
3. Create a `.streamlit` folder and inside it create a `secrets.toml` file to set up your environment variables
4. Run the app: `streamlit run gui_travel_recommendation_rag.py`
5. To view the app, navigate to [http://localhost:8501](http://localhost:8501)

> [!IMPORTANT]
> Your `secrets.toml` file should contain the following environment variables:
>
> ```bash
> OPENAI_API_KEY = "sk-xxxxxxxxxxxxxxxxxxxxxxxxx"
> DATA_DIRECTORY_PATH = 'C:\\path\\to\\your\\data\\directory'
> ```

<br>

## ⚒️ Tech stack ⚒️

OS:

- Windows `10`

Dependencies:

- [Python](https://www.python.org/) `3.11.8`
- [Streamlit](https://pypi.org/project/streamlit/) `1.31.1`
- [LlamaIndex Python SDK](https://pypi.org/project/llama-index/) `0.10.12`

<br>

## 📽️ Demonstration 📽️

![Demonstration of how to chat with the travel recommendation RAG with response streaming in the Streamlit app](https://github.com/rokbenko/ai-playground/blob/main/llamaindex-tutorials/2-GUI_travel_recommendation_RAG/screenshot.gif)
