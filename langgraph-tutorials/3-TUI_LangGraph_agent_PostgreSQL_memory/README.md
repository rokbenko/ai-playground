# #3 Python TUI for a LangGraph agent with persistent memory using PostgreSQL

## 📖 Description 📖

Add persistent memory using PostgreSQL to the [#1 TUI for a LangGraph agent with a web connection](https://github.com/rokbenko/ai-playground/tree/main/langgraph-tutorials/1-TUI_LangGraph_agent_Tavily) tutorial.

This directory will have the following structure after completing the steps in the [_Getting started_](https://github.com/rokbenko/ai-playground/tree/main/langgraph-tutorials/3-TUI_LangGraph_agent_PostgreSQL_memory#-getting-started-) section:

```
├── README.md
│
├── assets
│   └── images
│       └── demonstration.gif
│
└── python
    ├── my-venv
    ├── .env
    ├── .gitignore
    ├── requirements.txt
    └── tui_langgraph_agent_postgresql_memory.py
```

<br>

## 🧠 Learning goals 🧠

- **Understanding LangGraph [PostgreSQL checkpointers](https://github.com/langchain-ai/langgraph/tree/main/libs/checkpoint-postgres):** PostgreSQL checkpointers provide a persistence layer for LangGraph using PostgreSQL. They allow you to interact with and manage the graph's state, leveraging PostgreSQL. When you use a graph with a PostgreSQL checkpointer, the checkpointer saves a checkpoint of the graph state in PostgreSQL at every superstep, enabling several powerful capabilities like human-in-the-loop, "memory" between interactions, and more.
- **Implementing persistent storage using the [`AsyncPostgresSaver`](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.postgres.aio.AsyncPostgresSaver) class:** We'll show how to enhance a LangGraph ReAct agent by adding persistent storage capabilities using the `AsyncPostgresSaver` class. The `AsyncPostgresSaver` class provides a practical implementation of a PostgreSQL checkpointer with a LangGraph agent. This feature allows your agent to memorize the conversation even if the script exits or the program is terminated, as it's stored persistently. The implementation leverages an async connection pool to manage connections to the PostgreSQL database. Async connections allow non-blocking database operations, enabling other parts of your application to continue running while waiting for database tasks to complete.

<br>

## 🚀 Getting started 🚀

Before running [`tui_langgraph_agent_postgresql_memory.py`](https://github.com/rokbenko/ai-playground/blob/main/langgraph-tutorials/3-TUI_LangGraph_agent_PostgreSQL_memory/python/tui_langgraph_agent_postgresql_memory.py), follow the instructions below.

> [!NOTE]
> The instructions are specific to Windows. For macOS or Linux, please use the corresponding commands for your operating system.

### Python

1. Clone the repository: `git clone https://github.com/rokbenko/ai-playground.git`
2. Change the directory: `cd ai-playground/langgraph-tutorials/3-TUI_LangGraph_agent_PostgreSQL_memory/python`
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
> ANTHROPIC_API_KEY = "sk-xxxxxxxxxxxxxxxxxxxxxxxxx"
> TAVILY_API_KEY = "tvly-xxxxxxxxxxxxxxxxxxxxxxxxx"
> ```

> [!TIP]
> You can verify that the virtual environment is _created_ successfully if you see a folder named `my-venv` inside the `python` directory.
>
> ```
> ├── README.md
> │
> ├── assets
> │   └── images
> │       └── demonstration.gif
> │
> └── python
>     ├── my-venv 👈
>     ├── .env
>     ├── .gitignore
>     ├── requirements.txt
>     └── tui_langgraph_agent_postgresql_memory.py
> ```
>
> You can verify that the virtual environment is _activated_ successfully if you see `(my-venv)` at the beginning of your terminal prompt, like this:
>
> ```
> (my-venv) C:\your\path\to\ai-playground\langgraph-tutorials\3-TUI_LangGraph_agent_PostgreSQL_memory\python
> ```
>
> You can verify that the virtual environment is _deactivated_ successfully if you don't see `(my-venv)` anymore at the beginning of your terminal prompt, like this:
>
> ```
> C:\your\path\to\ai-playground\langgraph-tutorials\3-TUI_LangGraph_agent_PostgreSQL_memory\python
> ```

> [!NOTE]
> `venv` is a built-in Python module that allows you to create and manage virtual environments. If you have Python `3.3` or higher installed, you can start using `venv` right away.

<br>

## 🔥 Working example in Python 🔥

> [!NOTE]
> The check mark (i.e., ✔️) and cross mark (i.e., ❌) emojis are not part of the agent's actual responses. They were added manually in this README file to highlight the parts of the chat that the tutorial is designed to address.

If you run [`tui_langgraph_agent_postgresql_memory.py`](https://github.com/rokbenko/ai-playground/blob/main/langgraph-tutorials/3-TUI_LangGraph_agent_PostgreSQL_memory/python/tui_langgraph_agent_postgresql_memory.py), you should be able to chat with the agent in a terminal:

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

_The Python script was reran..._

#### Chat #2

> User:<br>
> Tell me what's my name.
> <br><br>
> Agent:<br>
> Your name is Bob! ✔️
> <br><br>
> User:<br>
> Quit
> <br><br>
> Agent:<br>
> Have a nice day! 👋

> [!NOTE]
> If only in-memory storage would be implemented (i.e., not persistent storage using PostgreSQL), the chat would look as follows:
>
> #### Chat #1
>
> > User:<br>
> > Hi, I'm Bob!
> > <br><br>
> > Agent:<br>
> > Hello Bob! How can I assist you today?
> > <br><br>
> > User:<br>
> > Quit
> > <br><br>
> > Agent:<br>
> > Have a nice day! 👋
>
> _The Python script was reran..._
>
> #### Chat #2
>
> > User:<br>
> > Tell me what's my name.
> > <br><br>
> > Agent:<br>
> > I'm unable to know your name as I don't have that information. If there's anything specific you'd like me to help you with, feel free to ask! ❌
> > <br><br>
> > User:<br>
> > Quit
> > <br><br>
> > Agent:<br>
> > Have a nice day! 👋

### ⚒️ Tech stack ⚒️

OS:

- Windows `10`

Dependencies:

- [Python](https://www.python.org/) `3.11.8`
- [Dotenv](https://pypi.org/project/python-dotenv/) `1.0.1`
- [LangChain Python SDK](https://pypi.org/project/langchain/) `0.3.8`
- [LangChain Core Python SDK](https://pypi.org/project/langchain-core/) `0.3.21`
- [LangChain Community Python SDK](https://pypi.org/project/langchain-community/) `0.3.8`
- [LangChain Anthropic Python SDK](https://pypi.org/project/langchain-anthropic/) `0.3.0`
- [LangGraph Python SDK](https://pypi.org/project/langgraph/) `0.2.53`
- [LangGraph PostgreSQL Checkpointer](https://pypi.org/project/langgraph-checkpoint-postgres/) `2.0.3`
- [PostgreSQL Python Adapter](https://pypi.org/project/psycopg/) `3.2.3`
- [PostgreSQL Python Connection Pool](https://pypi.org/project/psycopg-pool/) `3.2.3`
- [Rich](https://pypi.org/project/rich/) `13.9.4`

<br>

## 📽️ Demonstration 📽️

After the chat is restarted, the agent, whether it uses the Tavily tool or not to provide an answer, retains the user's name (i.e., Bob) and understands what information is needed about New York (i.e., weather).

![Demonstration](https://github.com/rokbenko/ai-playground/blob/main/langgraph-tutorials/3-TUI_LangGraph_agent_PostgreSQL_memory/assets/images/demonstration.gif)
