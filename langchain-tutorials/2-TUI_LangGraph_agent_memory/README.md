# #2 Python and Node.js TUIs for a LangGraph agent with a memory

<br>

## 📖 Description 📖

Python and Node.js TUIs for a LangGraph ReAct agent using the MemorySaver class to get a memory, the Tavily tool and an OpenAI LLM.

This directory has the following structure:

```
│   README.md
│
├───nodejs
│       node_modules
│       .env
│       .gitignore
│       package-lock.json
|       package.json
│       tui_langgraph_agent_memory.js
│
└───python
        my-venv
        .env
        .gitignore
        requirements.txt
        tui_langgraph_agent_memory.py
```

<br>

## 🧠 Learning goals 🧠

- **Understanding LangGraph [checkpointers](https://github.com/langchain-ai/langgraph/tree/main/libs/checkpoint):** Checkpointers provide a persistence layer for LangGraph. They allow you to interact with and manage the graph's state. When you use a graph with a checkpointer, the checkpointer saves a checkpoint of the graph state at every superstep, enabling several powerful capabilities like human-in-the-loop, "memory" between interactions, and more.

- **Implementing in-memory storage using the [MemorySaver](https://langchain-ai.github.io/langgraphjs/reference/classes/index.MemorySaver.html) class:** We'll show how to enhance a LangGraph ReAct agent by adding in-memory storage capabilities using the MemorySaver class. The MemorySaver class provides a practical implementation of checkpointers with a LangGraph agent. This feature allows your agent to memorize the conversation. In-memory storage means the data is temporarily stored in the computer's RAM, allowing for quick access and retrieval during the agent's operation. However, this memory will be lost when the script exits or the program is terminated, as it is not stored persistently.

<br>

## 🚀 Installation 🚀

Before running [`tui_langgraph_agent_memory.py`](https://github.com/rokbenko/ai-playground/blob/main/langchain-tutorials/2-TUI_LangGraph_agent_memory/python/tui_langgraph_agent_memory.py) or [`tui_langgraph_agent_memory.js`](https://github.com/rokbenko/ai-playground/blob/main/langchain-tutorials/2-TUI_LangGraph_agent_memory/nodejs/tui_langgraph_agent_memory.js), follow the instructions below.

> [!NOTE]
> The instructions are specific to Windows. For macOS or Linux, please use the corresponding commands for your operating system.

### Python

1. Clone the repository: `git clone https://github.com/rokbenko/ai-playground.git`
2. Change the directory: `cd ai-playground/langchain-tutorials/2-TUI_LangGraph_agent_memory/python`
3. Create a virtual environment named `my-venv`: `python -m venv my-venv`
4. Activate the virtual environment `my-venv`: `my-venv\Scripts\activate`
5. Install the dependencies: `python -m pip install -r requirements.txt`
6. Create an `.env` file to set up your environment variables
7. Run the Python script: `python tui_langgraph_agent_memory.py`

> [!WARNING]
> Deactivate the virtual environment `my-venv` after you are finished by running the following command:
>
> ```
> deactivate
> ```

> [!IMPORTANT]
> Your `.env` file should contain the following environment variables:
>
> ```
> OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxx
> TAVILY_API_KEY=tvly-xxxxxxxxxxxxxxxxxxxxxxxxx
> ```

> [!TIP]
> You can verify that the virtual environment is _created_ successfully if you see a folder named `my-venv` inside the `python` directory.
>
> ```
> │   README.md
> │
> ├───nodejs
> │       node_modules
> │       .env
> │       .gitignore
> │       package-lock.json
> |       package.json
> │       tui_langgraph_agent_memory.js
> │
> └───python
>         my-venv 👈
>         .env
>         .gitignore
>         requirements.txt
>         tui_langgraph_agent_memory.py
> ```
>
> You can verify that the virtual environment is _activated_ successfully if you see `(my-venv)` at the beginning of your terminal prompt, like this:
>
> ```
> (my-venv) C:\your\path\to\ai-playground\langchain-tutorials\2-TUI_LangGraph_agent_memory\python
> ```
>
> You can verify that the virtual environment is _deactivated_ successfully if you don't see `(my-venv)` anymore at the beginning of your terminal prompt, like this:
>
> ```
> C:\your\path\to\ai-playground\langchain-tutorials\2-TUI_LangGraph_agent_memory\python
> ```

> [!NOTE]
> `venv` is a built-in Python module that allows you to create and manage virtual environments. If you have Python `v3.3` or higher installed, you can start using `venv` right away.

### Node.js

1. Clone the repository: `git clone https://github.com/rokbenko/ai-playground.git`
2. Change the directory: `cd ai-playground/langchain-tutorials/2-TUI_LangGraph_agent_memory/nodejs`
3. Install the dependencies: `npm i`
4. Create an `.env` file to set up your environment variables
5. Run the Node.js script: `node tui_langgraph_agent_memory.js`

> [!IMPORTANT]
> Your `.env` file should contain the following environment variables:
>
> ```
> OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxx
> TAVILY_API_KEY=tvly-xxxxxxxxxxxxxxxxxxxxxxxxx
> ```

<br>

## 🔥 Working example in Python 🔥

If you run [`tui_langgraph_agent_memory.py`](https://github.com/rokbenko/ai-playground/blob/main/langchain-tutorials/2-TUI_LangGraph_agent_memory/python/tui_langgraph_agent_memory.py), you should be able to chat with the agent in a terminal:

> User:<br>
> Hi, I'm Bob!
> <br><br>
> Agent:<br>
> Hello Bob! How can I assist you today?
> <br><br>
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
> If the memory wouldn't be implemented, the chat would look as follows:
> <br>
> > User:<br>
> Hi, I'm Bob!
> <br><br>
> Agent:<br>
> Hello Bob! How can I assist you today?
> <br><br>
> User:<br>
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
- [LangChain Python SDK](https://pypi.org/project/langchain/) `0.2.12`
- [LangChain Core Python SDK](https://pypi.org/project/langchain-core/) `0.2.29`
- [LangChain Community Python SDK](https://pypi.org/project/langchain-community/) `0.2.11`
- [LangChain OpenAI Python SDK](https://pypi.org/project/langchain-openai/) `0.1.20`
- [LangGraph Python SDK](https://pypi.org/project/langgraph/) `0.2.3`
- [Rich](https://pypi.org/project/rich/) `13.7.1`

<br>

## 🔥 Working example in Node.js 🔥

If you run [`tui_langgraph_agent_memory.js`](https://github.com/rokbenko/ai-playground/blob/main/langchain-tutorials/2-TUI_LangGraph_agent_memory/nodejs/tui_langgraph_agent_memory.js), you should be able to chat with the agent in a terminal:

> User:<br>
> Hi, I'm Bob!
> <br><br>
> Agent:<br>
> Hello Bob! How can I assist you today?
> <br><br>
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
> Have a nice day!

> [!NOTE]
> If the memory wouldn't be implemented, the chat would look as follows:
> <br>
> > User:<br>
> Hi, I'm Bob!
> <br><br>
> Agent:<br>
> Hello Bob! How can I assist you today?
> <br><br>
> User:<br>
> Tell me what's my name.
> <br><br>
> Agent:<br>
> I'm unable to know your name as I don't have that information. If there's anything specific you'd like me to help you with, feel free to ask!
> <br><br>
> User:<br>
> Quit
> <br><br>
> Agent:<br>
> Have a nice day!

### ⚒️ Tech stack ⚒️

OS:

- Windows `10`

Dependencies:

- [Node.js](https://nodejs.org/en) `21.2.0`
- [LangChain Node.js SDK](https://www.npmjs.com/package/langchain) `0.2.15`
- [LangChain Core Node.js SDK](https://www.npmjs.com/package/@langchain/core) `0.2.23`
- [LangChain Community Node.js SDK](https://www.npmjs.com/package/@langchain/community) `0.2.25`
- [LangChain OpenAI Node.js SDK](https://www.npmjs.com/package/@langchain/openai) `0.2.6`
- [LangGraph Node.js SDK](https://www.npmjs.com/package/@langchain/langgraph) `0.0.33`
- [Terminal Kit](https://www.npmjs.com/package/terminal-kit) `3.1.1`

<br>

## 📽️ Demonstration 📽️

An example where the agent doesn't need to use the Tavily tool (the goal is for the agent to remember what's the user's name—the answer is Bob):

Coming soon... ✨

An example where the agent does need to use the Tavily tool (the goal is for the agent to remember what we want to know about New York—the answer is weather):

Coming soon... ✨
