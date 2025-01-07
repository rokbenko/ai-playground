# #4 LangSmith observability starter

## 📖 Description 📖

Add observability using LangSmith to the [#3 TUI for a LangGraph agent with persistent memory using PostgreSQL](https://github.com/rokbenko/ai-playground/tree/main/langchain-tutorials/3-TUI_LangGraph_agent_PostgreSQL_memory) tutorial.

In the previous tutorial, we demonstrated how to implement persistent memory for a LangGraph agent using PostgreSQL. However, after sharing the tutorial on social media, I received feedback pointing out that this approach consumes more tokens. This observation is valid. In this tutorial, we’ll use LangSmith for observability to confirm this and provide deeper insights into token usage.

This directory will have the following structure after completing the steps in the [*Getting started*](https://github.com/rokbenko/ai-playground/tree/main/langchain-tutorials/4-LangSmith_observability_starter#-getting-started-) section:

```
│   README.md
│
└───python
        my-venv
        .env
        .gitignore
        langsmith_test.png
        langsmith_tui_run_1.png
        langsmith_tui_run_2.png
        langsmith_tui_run_3.png
        requirements.txt
        test_langsmith_observability.py
        tui_langsmith_observability.py
```

<br>

## 🧠 Learning goal 🧠

- **Getting to know [LangSmith](https://docs.smith.langchain.com/) for observability:** LangSmith is a platform for building production-grade LLM apps. It allows you to closely monitor and evaluate your LLM app, so you can ship quickly and with confidence. We'll show how to start using LangSmith and observe LLM apps.

<br>

## 🚀 Getting started 🚀

Before running [`test_langsmith_observability.py`](https://github.com/rokbenko/ai-playground/blob/main/langchain-tutorials/4-LangSmith_observability_starter/python/test_langsmith_observability.py) or [`tui_langsmith_observability.py`](https://github.com/rokbenko/ai-playground/blob/main/langchain-tutorials/4-LangSmith_observability_starter/python/tui_langsmith_observability.py), follow the instructions below.

> [!NOTE]
> The instructions are specific to Windows. For macOS or Linux, please use the corresponding commands for your operating system.

### Python

1. Clone the repository: `git clone https://github.com/rokbenko/ai-playground.git`
2. Change the directory: `cd ai-playground/langchain-tutorials/4-LangSmith_observability_starter/python`
3. Create a virtual environment named `my-venv`: `python -m venv my-venv`
4. Activate the virtual environment `my-venv`: `my-venv/scripts/activate`
5. Install the dependencies: `python -m pip install -r requirements.txt`
6. Create an `.env` file to set up your environment variables
7. Run the Python script: `python tui_langsmith_observability.py`
8. Chat with the agent in the terminal
9. Visit [LangSmith](https://smith.langchain.com/) and navigate to the *Tracing projects* to view a detailed report of your LangGraph agent's activity, including token usage

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
> MISTRAL_API_KEY="xxxxxxxxxxxxxxxxxxxxxxxxx"
>
> TAVILY_API_KEY = "tvly-xxxxxxxxxxxxxxxxxxxxxxxxx"
>
> PSQL_USERNAME = "postgres"
> PSQL_PASSWORD = "xxxxx"
> PSQL_HOST = "localhost"
> PSQL_PORT = "5432"
> PSQL_DATABASE = "agent_chat"
> PSQL_SSLMODE = "disable"
> 
> LANGCHAIN_TRACING_V2=true
> LANGCHAIN_ENDPOINT="https://api.smith.langchain.com"
> LANGCHAIN_API_KEY="lsv2_pt_xxxxxxxxxxxxxxxxxxxxxxxxx"
> LANGCHAIN_PROJECT="YouTube LangSmith tutorial"
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
>         langsmith_test.png
>         langsmith_tui_run_1.png
>         langsmith_tui_run_2.png
>         langsmith_tui_run_3.png
>         requirements.txt
>         test_langsmith_observability.py
>         tui_langsmith_observability.py
> ```
>
> You can verify that the virtual environment is _activated_ successfully if you see `(my-venv)` at the beginning of your terminal prompt, like this:
>
> ```
> (my-venv) C:\your\path\to\ai-playground\langchain-tutorials\4-LangSmith_observability_starter\python
> ```
>
> You can verify that the virtual environment is _deactivated_ successfully if you don't see `(my-venv)` anymore at the beginning of your terminal prompt, like this:
>
> ```
> C:\your\path\to\ai-playground\langchain-tutorials\4-LangSmith_observability_starter\python
> ```

> [!NOTE]
> `venv` is a built-in Python module that allows you to create and manage virtual environments. If you have Python `3.3` or higher installed, you can start using `venv` right away.

<br>

## 🔥 Working example in Python 🔥

If you’ve set up the `.env` file correctly, you should see a report in the LangSmith dashboard after running [`test_langsmith_observability.py`](https://github.com/rokbenko/ai-playground/blob/main/langchain-tutorials/4-LangSmith_observability_starter/python/test_langsmith_observability.py):

![LangSmith test run dashboard screenshot](https://github.com/rokbenko/ai-playground/blob/main/langchain-tutorials/4-LangSmith_observability_starter/python/langsmith_test.png)

In the screenshot above, the `LANGCHAIN_PROJECT` environment variable in the `.env` file was set to `test`, which is why the traced project's name appeared as *test* in LangSmith. To test LangSmith, I ran [`test_langsmith_observability.py`](https://github.com/rokbenko/ai-playground/blob/main/langchain-tutorials/4-LangSmith_observability_starter/python/test_langsmith_observability.py), greeted the LangGraph agent with *Hello, world!*, and received the agent's response *Hello! How can I assist you today? Let's chat about anything you'd like.* 😊 After that, I typed *Quit* to exit the chat. Both the input and output combined consumed a total of 28 tokens.

> [!NOTE]
> If you notice three runs in the screenshot above, please ignore them. I ran the Python script three times while exploring LangSmith for the first time, just to test how it works. Two of those runs are duplicates. The conversation described above with *Hello, world!* should result in just one run.

After confirming that LangSmith was working, I ran [`tui_langsmith_observability.py`](https://github.com/rokbenko/ai-playground/blob/main/langchain-tutorials/4-LangSmith_observability_starter/python/tui_langsmith_observability.py) three times, as detailed below:

#### Chat #1

> User:<br>
> Hi, I'm Bob!
> <br><br>
> Agent:<br>
> Hello Bob, how can I assist you today?
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
> Your name is Bob.
> <br><br>
> User:<br>
> Quit
> <br><br>
> Agent:<br>
> Have a nice day! 👋

*The Python script was reran...*

#### Chat #3

> User:<br>
> Hi!
> <br><br>
> Agent:<br>
> Hello! How can I help you today?
> <br><br>
> User:<br>
> Quit
> <br><br>
> Agent:<br>
> Have a nice day! 👋

Each chat session resulted in a separate run, and LangSmith generated a report for each one.

**LangSmith report for the first chat session:**

![LangSmith TUI first run dashboard screenshot](https://github.com/rokbenko/ai-playground/blob/main/langchain-tutorials/4-LangSmith_observability_starter/python/langsmith_tui_run_1.png)

**LangSmith report for the second chat session:**

![LangSmith TUI second run dashboard screenshot](https://github.com/rokbenko/ai-playground/blob/main/langchain-tutorials/4-LangSmith_observability_starter/python/langsmith_tui_run_2.png)

**LangSmith report for the third chat session:**

![LangSmith TUI third run dashboard screenshot](https://github.com/rokbenko/ai-playground/blob/main/langchain-tutorials/4-LangSmith_observability_starter/python/langsmith_tui_run_3.png)

> [!NOTE]
> The screenshots were taken after the third chat session was completed, which is why all three screenshots show all three runs. In reality, after the first chat session, LangSmith displayed one run. After the second, it displayed two runs. And after the third, it displayed three runs.

In the screenshot above, the `LANGCHAIN_PROJECT` environment variable in the `.env` file was set to `YouTube LangSmith tutorial`, which is why the traced project's name appeared as *YouTube LangSmith tutorial* in LangSmith.

As you can see, the first chat consumed 118 tokens, the second consumed 133 tokens, and the third consumed 147 tokens. By closely examining the inputs passed to the Mistral LLM, we can see how persistent memory using PostgreSQL works: all previous messages are passed to the LLM, even when they’re not directly needed by the LangGraph agent. For example, in the third chat, I simply greeted the agent with *Hi!*, yet all previous messages were still included in the input to Mistral LLM, which was totally unnecessary. This highlights a key inefficiency: more tokens are consumed than necessary, as the persistent memory mechanism sends all prior conversations to the LLM, even when earlier messages aren’t relevant to the latest message. As a result, token consumption increases, leading to higher costs and unnecessary computational overhead.

<br>

## ⚒️ Tech stack ⚒️

OS:

- Windows `10`

Dependencies:

- [Python](https://www.python.org/) `3.11.8`
- [Dotenv](https://pypi.org/project/python-dotenv/) `1.0.1`
- [LangChain Python SDK](https://pypi.org/project/langchain/) `0.3.14`
- [LangChain Core Python SDK](https://pypi.org/project/langchain-core/) `0.3.29`
- [LangChain Community Python SDK](https://pypi.org/project/langchain-community/) `0.3.14`
- [LangChain Mistral Python SDK](https://pypi.org/project/langchain-mistralai/) `0.2.4`
- [LangGraph Python SDK](https://pypi.org/project/langgraph/) `0.2.61`
- [LangGraph PostgreSQL Checkpointer](https://pypi.org/project/langgraph-checkpoint-postgres/) `2.0.9`
- [PostgreSQL Python Adapter](https://pypi.org/project/psycopg/) `3.2.3`
- [PostgreSQL Python Connection Pool](https://pypi.org/project/psycopg-pool/) `3.2.3`
- [Rich](https://pypi.org/project/rich/) `13.9.4`

<br>

## 📽️ Demonstration 📽️

Take a look at the following screenshots that demonstrate the LangSmith integration in action as described in the [*Working example in Python*](https://github.com/rokbenko/ai-playground/blob/main/langchain-tutorials/4-LangSmith_observability_starter/README.md#-getting-started-) section:

- [Test LangSmith run report](https://github.com/rokbenko/ai-playground/blob/main/langchain-tutorials/4-LangSmith_observability_starter/python/langsmith_test.png)
- [First LangSmith TUI run report](https://github.com/rokbenko/ai-playground/blob/main/langchain-tutorials/4-LangSmith_observability_starter/python/langsmith_tui_run_1.png)
- [Second LangSmith TUI run report](https://github.com/rokbenko/ai-playground/blob/main/langchain-tutorials/4-LangSmith_observability_starter/python/langsmith_tui_run_2.png)
- [Third LangSmith TUI run report](https://github.com/rokbenko/ai-playground/blob/main/langchain-tutorials/4-LangSmith_observability_starter/python/langsmith_tui_run_3.png)
