# #3 Python TUI for a LangGraph agent with persistent memory using PostgreSQL

<br>

## 📖 Description 📖

Add persistent memory using PostgreSQL to the [#1 TUI for a LangGraph agent with a web connection via the Tavily tool](https://github.com/rokbenko/ai-playground/tree/main/langchain-tutorials/1-TUI_LangGraph_agent_Tavily) tutorial.

> [!NOTE]
> This tutorial currently includes an example in Python only. While I typically provide both Python and Node.js examples, the LangGraph Node.js SDK has not yet implemented the specific class (i.e., `AsyncPostgresSaver`) required for this tutorial.
>
> Once the LangGraph Node.js SDK is updated to include this feature, I will add the Node.js example to this tutorial.

This directory has the following structure:

```
│   README.md
│
└───python
        my-venv
        .env
        .gitignore
        requirements.txt
        tui_langgraph_agent_postgresql_memory.py
```

<br>

## 🧠 Learning goal 🧠

- **Implementing persistent storage using the `AsyncPostgresSaver` class:** We'll show how to enhance a LangGraph ReAct agent by adding persistent storage capabilities using the `AsyncPostgresSaver` class. The `AsyncPostgresSaver` class provides a practical implementation of a PostgreSQL checkpointer with a LangGraph agent. This feature allows your agent to memorize the conversation even if the script exits or the program is terminated, as it's stored persistently. The implementation leverages an async connection pool to manage connections to the PostgreSQL database. Async connections allow non-blocking database operations, enabling other parts of your application to continue running while waiting for database tasks to complete. This is particularly useful in high-concurrency scenarios or when dealing with I/O-bound operations, ensuring your application remains responsive and efficient.

<br>

## 🚀 Installation 🚀

Before running [`tui_langgraph_agent_postgresql_memory.py`](https://github.com/rokbenko/ai-playground/blob/main/langchain-tutorials/3-TUI_LangGraph_agent_PostgreSQL_memory/python/tui_langgraph_agent_postgresql_memory.py), follow the instructions below.

> [!NOTE]
> The instructions are specific to Windows. For macOS or Linux, please use the corresponding commands for your operating system.

### Python

1. Clone the repository: `git clone https://github.com/rokbenko/ai-playground.git`
2. Change the directory: `cd ai-playground/langchain-tutorials/3-TUI_LangGraph_agent_PostgreSQL_memory/python`
3. Create a virtual environment named `my-venv`: `python -m venv my-venv`
4. Activate the virtual environment `my-venv`: `my-venv/scripts/activate`
5. Install the dependencies: `python -m pip install -r requirements.txt`
6. Create an `.env` file to set up your environment variables
7. Run the Python script: `python tui_langgraph_agent_postgresql_memory.py`

> [!WARNING]
> Deactivate the virtual environment `my-venv` after you're finished by running the following command:
>
> ```
> deactivate
> ```

> [!IMPORTANT]
> Your `.env` file should contain the following environment variables:
>
> ```bash
> OPENAI_API_KEY = "sk-xxxxxxxxxxxxxxxxxxxxxxxxx"
> TAVILY_API_KEY = "tvly-xxxxxxxxxxxxxxxxxxxxxxxxx"
> ```

> [!TIP]
> You can verify that the virtual environment is _created_ successfully if you see a folder named `my-venv` inside the `python` directory.
>
> ```
> │   README.md
> │
> └───python
>         my-venv 👈
>         .env
>         .gitignore
>         requirements.txt
>         tui_langgraph_agent_postgresql_memory.py
> ```
>
> You can verify that the virtual environment is _activated_ successfully if you see `(my-venv)` at the beginning of your terminal prompt, like this:
>
> ```
> (my-venv) C:\your\path\to\ai-playground\langchain-tutorials\3-TUI_LangGraph_agent_PostgreSQL_memory\python
> ```
>
> You can verify that the virtual environment is _deactivated_ successfully if you don't see `(my-venv)` anymore at the beginning of your terminal prompt, like this:
>
> ```
> C:\your\path\to\ai-playground\langchain-tutorials\3-TUI_LangGraph_agent_PostgreSQL_memory\python
> ```

> [!NOTE]
> `venv` is a built-in Python module that allows you to create and manage virtual environments. If you have Python `3.3` or higher installed, you can start using `venv` right away.

<br>

## 🔥 Working example in Python 🔥

If you run [`tui_langgraph_agent_postgresql_memory.py`](https://github.com/rokbenko/ai-playground/blob/main/langchain-tutorials/3-TUI_LangGraph_agent_PostgreSQL_memory/python/tui_langgraph_agent_postgresql_memory.py), you should be able to chat with the agent in a terminal:

#### Chat #1

> User:<br>
> Hi, I'm Bob!
> <br><br>
> Agent:<br>
> Hello Bob! How can I assist you today?
> <br><br>
> User:<br>
> Quit
> <br><br>
> Agent:<br>
> Have a nice day! 👋

*The Python script was reran...*

#### Chat #2

> User:<br>
> Tell me what's my name.
> <br><br>
> Agent:<br>
> Your name is Bob!
> <br><br>
> User:<br>
> Quit
> <br><br>
> Agent:<br>
> Have a nice day! 👋

> [!NOTE]
> If the persistent memory wouldn't be implemented, the chat would look as follows:
>
> #### Chat #1
> > User:<br>
> Hi, I'm Bob!
> <br><br>
> Agent:<br>
> Hello Bob! How can I assist you today?
> <br><br>
> User:<br>
> Quit
> <br><br>
> Agent:<br>
> Have a nice day! 👋
>
> *The Python script was reran...*
> 
> #### Chat #2
>
> > User:<br>
> Tell me what's my name.
> <br><br>
> Agent:<br>
> I'm unable to know your name as I don't have that information. If there's anything specific you'd like me to help you with, feel free to ask!
> <br><br>
> User:<br>
> Quit
> <br><br>
> Agent:<br>
> Have a nice day! 👋

### ⚒️ Tech stack ⚒️

OS:

- Windows `10`

Dependencies:

- [Python](https://www.python.org/) `3.11.8`
- [Dotenv](https://pypi.org/project/python-dotenv/) `1.0.1`
- [LangChain Python SDK](https://pypi.org/project/langchain/) `0.2.14`
- [LangChain Core Python SDK](https://pypi.org/project/langchain-core/) `0.2.33`
- [LangChain Community Python SDK](https://pypi.org/project/langchain-community/) `0.2.12`
- [LangChain OpenAI Python SDK](https://pypi.org/project/langchain-openai/) `0.1.22`
- [LangGraph Python SDK](https://pypi.org/project/langgraph/) `0.2.4`
- [LangGraph PostgreSQL Checkpointer](https://pypi.org/project/langgraph-checkpoint-postgres/) `1.0.3`
- [PostgreSQL Python Adapter](https://pypi.org/project/psycopg/) `3.2.1`
- [PostgreSQL Python Connection Pool](https://pypi.org/project/psycopg-pool/) `3.2.2`
- [Rich](https://pypi.org/project/rich/) `13.7.1`

<br>

## 📽️ Demonstration 📽️

An example of a question where the agent doesn't need to use the Tavily tool (the goal is for the agent to know what's the user's name *after the first chat is quitted* — the answer is Bob):

Coming soon... ✨

An example of a question where the agent does need to use the Tavily tool (the goal is for the agent to know what we want to know about New York *after the first chat is quitted* — the answer is weather):

Coming soon... ✨
