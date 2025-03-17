# #4 Python TUI for a LangGraph agent with persistent memory using PostgreSQL with pgvector

## 📖 Description 📖

Add persistent memory using PostgreSQL with pgvector to the [#1 TUI for a LangGraph agent with a web connection](https://github.com/rokbenko/ai-playground/tree/main/langgraph-tutorials/1-TUI_LangGraph_agent_Tavily) tutorial.

![Flow diagram](https://github.com/rokbenko/ai-playground/blob/main/langgraph-tutorials/4-TUI_LangGraph_agent_PostgreSQL_memory_pgvector/assets/images/flow.png)

This directory will have the following structure after completing the steps in the [_Getting started_](https://github.com/rokbenko/ai-playground/tree/main/langgraph-tutorials/4-TUI_LangGraph_agent_PostgreSQL_memory_pgvector#-getting-started-) section:

```
├── README.md
│
├── assets
│   └── images
|       ├── docker_desktop_pgvector_container.png
|       ├── pgAdmin_create_database_general.png
|       ├── pgAdmin_create_database.png
|       ├── pgAdmin_database_query_tool_command.png
|       ├── pgAdmin_database_query_tool.png
|       ├── pgAdmin_register_server_connection.png
|       ├── pgAdmin_register_server_general.png
|       ├── pgAdmin_register_server.png
|       ├── demonstration_threshold.gif
│       └── demonstration_limit.gif
│
└── python
    ├── my-venv
    ├── .env
    ├── .gitignore
    ├── requirements.txt
    └── tui_langgraph_agent_postgresql_memory_pgvector.py
```

<br>

## 🧠 Learning goals 🧠

- **Understanding [pgvector](https://github.com/pgvector/pgvector)**: pgvector is an extension for PostgreSQL designed to facilitate the storage, querying, and indexing of high-dimensional embedding vector data. This extension addresses the growing need for managing embedding vector data, particularly in applications related to AI and ML, where embedding vectors are used to represent complex data types such as text, images, and other multi-dimensional datasets.
- **Exploring limit and threshold [similarity search types](https://github.com/pgvector/pgvector?tab=readme-ov-file#querying) with pgvector:** The project provides two options for similarity search: "limit" and "threshold". The "limit" option retrieves the top N most similar messages, while the "threshold" option retrieves messages that meet a specified similarity threshold. This flexibility allows you to tailor the agent's behavior based on your specific requirements.
- **Implementing persistent storage using pgvector:** We'll show how to enhance a LangGraph ReAct agent by adding persistent storage capabilities using PostgreSQL and the pgvector extension. This feature allows your agent to store conversation embeddings persistently, ensuring that the context is maintained even if the script exits or the program is terminated. The implementation leverages an async connection pool to manage connections to the PostgreSQL database. Async connections allow non-blocking database operations, enabling other parts of your application to continue running while waiting for database tasks to complete.

> [!NOTE]
> In this tutorial, we'll measure embedding vector similarities using **Cosine similarity**, which we'll derive from pgvector's `<=>` operator used for calculating **Cosine distance**. It's important to distinguish between **Cosine distance** and **Cosine similarity**.
>
> **Cosine distance** is calculated as follows:
>
> Cosine distance $$= 1 - \cos(\theta) = 1 - \frac{a \cdot b}{||a|| \cdot ||b||}$$
> 
> While **Cosine similarity** is simply derived from **Cosine distance**, and is calculated as follows:
>
> Cosine similarity $$= 1 -$$ Cosine distance
> 
> **Cosine similarity** measures the cosine of the angle between two embedding vectors, resulting in values between -1 and 1, where:
>
> - 1 means the two embedding vectors are identical in direction, forming a 0° angle, indicating perfect similarity,
> - 0 means the two embedding vectors are orthogonal, forming a 90° angle, indicating no similarity, and
> - -1 means the two embedding vectors point in opposite directions, forming a 180° angle, indicating perfect dissimilarity.
> 
> pgvector [offers](https://github.com/pgvector/pgvector?tab=readme-ov-file#querying) several other distance functions as well:
>
> - Cosine distance (using pgvector's `<=>` operator),
> - L1 distance (using pgvector's `<+>` operator),
> - L2 distance (using pgvector's `<->` operator),
> - (Negative) inner product (using pgvector's `<#>` operator),
> - Hamming distance (using pgvector's `<~>` operator), and
> - Jaccard distance (using pgvector's `<%>` operator).

<br>

## 🚀 Getting started 🚀

Before running [`tui_langgraph_agent_postgresql_memory_pgvector.py`](https://github.com/rokbenko/ai-playground/blob/main/langgraph-tutorials/4-TUI_LangGraph_agent_PostgreSQL_memory_pgvector/python/tui_langgraph_agent_postgresql_memory_pgvector.py), follow the instructions below.

> [!NOTE]
> The instructions are specific to Windows. For macOS or Linux, please use the corresponding commands for your operating system.

### Python

1. Clone the repository: `git clone https://github.com/rokbenko/ai-playground.git`
2. Change the directory: `cd ai-playground/langgraph-tutorials/4-TUI_LangGraph_agent_PostgreSQL_memory_pgvector/python`
3. Create a virtual environment named `my-venv`: `python -m venv my-venv`

> [!TIP]
> You can verify that the virtual environment is _created_ successfully if you see a folder named `my-venv` inside the `python` directory.
>
> ```
> ├── README.md
> │
> ├── assets
> │   └── images
> |       ├── docker_desktop_pgvector_container.png
> |       ├── pgAdmin_create_database_general.png
> |       ├── pgAdmin_create_database.png
> |       ├── pgAdmin_database_query_tool_command.png
> |       ├── pgAdmin_database_query_tool.png
> |       ├── pgAdmin_register_server_connection.png
> |       ├── pgAdmin_register_server_general.png
> |       ├── pgAdmin_register_server.png
> |       ├── demonstration_threshold.gif
> │       └── demonstration_limit.gif
> │
> └── python
>     ├── my-venv 👈
>     ├── .env
>     ├── .gitignore
>     ├── requirements.txt
>     └── tui_langgraph_agent_postgresql_memory_pgvector.py
> ```

> [!NOTE]
> `venv` is a built-in Python module that allows you to create and manage virtual environments. If you have Python `3.3` or higher installed, you can start using `venv` right away.

4. Activate the virtual environment `my-venv`: `my-venv/scripts/activate`

> [!TIP]
> You can verify that the virtual environment is _activated_ successfully if you see `(my-venv)` at the beginning of your terminal prompt, like this:
>
> ```
> (my-venv) C:\your\path\to\ai-playground\langgraph-tutorials\4-TUI_LangGraph_agent_PostgreSQL_memory_pgvector\python
> ```

5. Install the dependencies: `python -m pip install -r requirements.txt`
6. Create an `.env` file to set up your environment variables

> [!IMPORTANT]
> Your `.env` file should contain the following environment variables:
>
> ```bash
> MISTRAL_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxx"
> 
> TAVILY_API_KEY = "tvly-xxxxxxxxxxxxxxxxxxxxxxxxx"
>
> PSQL_USERNAME = "postgres"
> PSQL_PASSWORD = "xxxx" # As set with the Docker command in step 11
> PSQL_HOST = "localhost"
> PSQL_PORT = "5433" # As set with the Docker command in step 11
> PSQL_DATABASE = "agent_chat_pgvector"
> PSQL_SSLMODE = "disable"
> ```

7. Pull the PostgreSQL 16 Docker image with the following Docker command:

```
docker pull postgres:16
```

8. Verify the PostgreSQL 16 Docker image has been pulled successfully with the following Docker command:

```
docker images
```

You should see the following output:

```
REPOSITORY                         TAG          IMAGE ID       CREATED        SIZE
postgres                           16           xxxxxxxxxxxx   x months ago   432MB
```

9. Pull the pgvector Docker image for PostgreSQL 16 with the following Docker command:

```
docker pull pgvector/pgvector:pg16
```

10. Verify the pgvector Docker image for PostgreSQL 16 has been pulled successfully with the following Docker command:

```
docker images
```

You should see the following output:

```
REPOSITORY                         TAG          IMAGE ID       CREATED        SIZE
postgres                           16           xxxxxxxxxxxx   x months ago   432MB
pgvector/pgvector                  pg16         xxxxxxxxxxxx   x months ago   435MB
```

11. Run the PostgreSQL 16 with pgvector Docker container with the following Docker command:

```
docker run --name pgvector -e POSTGRES_PASSWORD=xxxx -p 5433:5432 -d pgvector/pgvector:pg16
```

Where:
- `xxxx` is the PostgreSQL user password. This should match the `PSQL_PASSWORD` value in your `.env` file.
- `5433` is the port on the host machine that maps to the PostgreSQL port `5432` inside the Docker container. This should match the `PSQL_PORT` value in your `.env` file.

After this is done, you should see a running container in the Docker Desktop app:

![Running pgvector container in Docker Desktop app](https://github.com/rokbenko/ai-playground/blob/main/langgraph-tutorials/4-TUI_LangGraph_agent_PostgreSQL_memory_pgvector/assets/images/docker_desktop_pgvector_container.png)

12. Register a new server in pgAdmin

- Open pgAdmin
- Right-click on "Servers" in the sidebar and select "Register" > "Server..."

Refer to the image below for guidance:

![Registering a new server in pgAdmin](https://github.com/rokbenko/ai-playground/blob/main/langgraph-tutorials/4-TUI_LangGraph_agent_PostgreSQL_memory_pgvector/assets/images/pgAdmin_register_server.png)

13. Set the name of the server

- In the "General" tab, enter a name for your server (e.g., `pgvector YouTube tutorial`)

Refer to the image below for guidance:

![Setting the server name in pgAdmin](https://github.com/rokbenko/ai-playground/blob/main/langgraph-tutorials/4-TUI_LangGraph_agent_PostgreSQL_memory_pgvector/assets/images/pgAdmin_register_server_general.png)

14. Set connection parameters of the new server

- Switch to the "Connection" tab
- Enter the following connection parameters:
  - Host name/address: `localhost`
  - Port: `5433` (as set with the Docker command in step 11)
  - Maintenance database: `postgres`
  - Username: `postgres`
  - Password: `xxxx` (as set with the Docker command in step 11)
- Click "Save" to create the server

Refer to the image below for guidance:

![Setting the server connection parameters in pgAdmin](https://github.com/rokbenko/ai-playground/blob/main/langgraph-tutorials/4-TUI_LangGraph_agent_PostgreSQL_memory_pgvector/assets/images/pgAdmin_register_server_connection.png)

15. Create a new database in the newly created server

- Expand the newly created server in the sidebar
- Right-click on "Databases" and select "Create" > "Database...".

Refer to the image below for guidance:

![Creating a new database in pgAdmin](https://github.com/rokbenko/ai-playground/blob/main/langgraph-tutorials/4-TUI_LangGraph_agent_PostgreSQL_memory_pgvector/assets/images/pgAdmin_create_database.png)

16. Set the name of the database

- In the "General" tab, enter a name for your database (e.g., `agent_chat_pgvector`)
- Click "Save" to create the database

Refer to the image below for guidance:

![Setting the database name in pgAdmin](https://github.com/rokbenko/ai-playground/blob/main/langgraph-tutorials/4-TUI_LangGraph_agent_PostgreSQL_memory_pgvector/assets/images/pgAdmin_create_database_general.png)

17. Open the query tool for the newly created database

- Right-click on the newly created database and select "Query Tool"

Refer to the image below for guidance:

![Opening the query tool in pgAdmin](https://github.com/rokbenko/ai-playground/blob/main/langgraph-tutorials/4-TUI_LangGraph_agent_PostgreSQL_memory_pgvector/assets/images/pgAdmin_database_query_tool.png)

18. Enable the pgvector extension in the newly created database

- In the Query Tool, enter the following SQL command to enable the pgvector extension:

```
CREATE EXTENSION vector;
```

> [!IMPORTANT]
> The command is `CREATE EXTENSION vector;` not `CREATE EXTENSION pgvector;`.

- Click the "Execute/Refresh" button (or press F5) to run the command
- You should see a message indicating that the extension has been created successfully

Refer to the image below for guidance:

![Enabling the pgvector extension in pgAdmin](https://github.com/rokbenko/ai-playground/blob/main/langgraph-tutorials/4-TUI_LangGraph_agent_PostgreSQL_memory_pgvector/assets/images/pgAdmin_database_query_tool_command.png)

19. Run the Python script with the `--similarity-search-type` terminal argument:<br>`python tui_langgraph_agent_postgresql_memory_pgvector.py --similarity-search-type=xxxxx`

Where:

- `xxxxx` can be either `limit` or `threshold`

> [!WARNING]
> Deactivate the virtual environment `my-venv` after you exit the chat by running the following command:
>
> ```
> deactivate
> ```

> [!TIP]
> You can verify that the virtual environment is _deactivated_ successfully if you don't see `(my-venv)` anymore at the beginning of your terminal prompt, like this:
>
> ```
> C:\your\path\to\ai-playground\langgraph-tutorials\4-TUI_LangGraph_agent_PostgreSQL_memory_pgvector\python
> ```

<br>

## 🔥 Working example in Python 🔥

> [!NOTE]
> The check mark (i.e., ✔️) and cross mark (i.e., ❌) emojis are not part of the agent's actual responses. They were added manually in this README.md file to highlight the parts of the chat that the tutorial is designed to address.

### Similarity search using limit-based approach

If you run [`tui_langgraph_agent_postgresql_memory_pgvector.py`](https://github.com/rokbenko/ai-playground/blob/main/langgraph-tutorials/4-TUI_LangGraph_agent_PostgreSQL_memory_pgvector/python/tui_langgraph_agent_postgresql_memory_pgvector.py) with the `python tui_langgraph_agent_postgresql_memory_pgvector.py --similarity-search-type=limit` command, it will perform a similarity search with a limit-based approach, and you should be able to chat with the agent in a terminal:

#### Chat #20

> [!NOTE]
> There were multiple conversations before that. It might have been chat #34 or #48, as the Python script was tested extensively before running the final version.
>
> At the time the chat below was run, there were dozens of messages stored in PostgreSQL, but PostgreSQL returned the top 5 most similar past messages with the highest cosine similarity to the latest user's question, as seen below.

> User:<br>
> What's my name?<br>
> 
> ============================================================
>
> Similarity search results:<br>
> Here are the top 5 most similar past messages with the highest cosine similarity to the latest user's question:<br>
> Message #1 (cosine similarity = 1.00): What's my name?<br>
> Message #2 (cosine similarity = 0.87): You can tell me what's my name.<br>
> Message #3 (cosine similarity = 0.87): I'm unable to determine your name from the provided conversation. The phrase "What's my name?" is repeated multiple times, but it does not provide any information about your actual name. If you would like me to know your name, please share it with me.<br>
> Message #4 (cosine similarity = 0.82): Your name is Bob.<br>
> Message #5 (cosine similarity = 0.82): You didn't mention your name in the conversation. Could you please tell me your name?
>
> Messages passed to the LangGraph agent:<br>
> The system message:<br>
> -----------------------<br>
> To answer the user's question, use this information which is part of the past conversation as a context:<br>
> - What's my name?<br>
> - You can tell me what's my name.<br>
> - I'm unable to determine your name from the provided conversation. The phrase "What's my name?" is repeated multiple times, but it does not provide any information about your actual name. If you would like me to know your name, please share it with me.<br> 
> - Your name is Bob.<br>
> - You didn't mention your name in the conversation. Could you please tell me your name?
> 
> The human message:<br>
> -----------------------<br>
> What's my name?
> 
> ============================================================
> 
> Agent:<br>
> Based on the past conversation, your name is Bob. ✔️
> 
> User:<br>
> Quit
> 
> Agent:<br>
> Have a nice day! 👋

### Similarity search using threshold-based approach

If you run [`tui_langgraph_agent_postgresql_memory_pgvector.py`](https://github.com/rokbenko/ai-playground/blob/main/langgraph-tutorials/4-TUI_LangGraph_agent_PostgreSQL_memory_pgvector/python/tui_langgraph_agent_postgresql_memory_pgvector.py) with the `python tui_langgraph_agent_postgresql_memory_pgvector.py --similarity-search-type=threshold` command, it will perform a similarity search with a threshold-based approach, and you should be able to chat with the agent in a terminal:

#### Chat #21

> [!NOTE]
> There were multiple conversations before that. It might have been chat #35 or #49, as the Python script was tested extensively before running the final version.
>
> At the time the chat below was run, there were dozens of messages stored in PostgreSQL, but PostgreSQL returned all past messages (i.e., 18) with a cosine similarity equal to or greater than 0.75 to the latest user's question, as seen below.

> User:<br>
> What's my name?<br>
> 
> ============================================================
>
> Similarity search results:<br>
> Here are the 18 past messages with a cosine similarity equal to or greater than 0.75 to the latest user's question:<br>
> Message #1 (cosine similarity = 1.00): What's my name?<br>
> Message #2 (cosine similarity = 0.90): My name is what?<br>
> Message #3 (cosine similarity = 0.87): You can tell me what's my name.<br>
> Message #4 (cosine similarity = 0.87): I'm unable to determine your name from the provided conversation. The phrase "What's my name?" is repeated multiple times, but it does not provide any information about your actual name. If you would like me to know your name, please share it with me.<br>
> Message #5 (cosine similarity = 0.83): I'm sorry, but I still don't know your name. You haven't told me yet. If you'd like me to know your name, please share it with me.<br>
> Message #6 (cosine similarity = 0.82): Your name is Bob.<br>
> Message #7 (cosine similarity = 0.82): You didn't mention your name in the conversation. Could you please tell me your name?<br>
> Message #8 (cosine similarity = 0.82): I don't have access to personal information about you, including your name. If you'd like to share your name orany other information, feel free to do so!<br>
> Message #9 (cosine similarity = 0.81): I don't have access to your name or any personal information. If you'd like to share your name, I can use it inour conversation. Otherwise, I'll continue to assist you without using a name.<br>
> Message #10 (cosine similarity = 0.81): Based on the provided conversation, your name is Bob. You stated, "Your name is Bob."<br>
> Message #11 (cosine similarity = 0.80): Hi, my name is Bob!<br>
> Message #12 (cosine similarity = 0.79): Based on the past conversation, your name is Bob. You stated, "Your name is Bob."<br>
> Message #13 (cosine similarity = 0.79): Where do I live?<br>
> Message #14 (cosine similarity = 0.79): Based on the past conversation, your name is Bob.<br>
> Message #15 (cosine similarity = 0.78): Based on our previous conversation, you mentioned that your name is Bob.<br>
> Message #16 (cosine similarity = 0.77): Based on our conversation, you mentioned earlier that your name is Bob.<br>
> Message #17 (cosine similarity = 0.77): Based on our previous conversation, you mentioned that your name is Bob. You live in San Francisco.<br>
> Message #18 (cosine similarity = 0.76): Bob, you've asked this question multiple times, and I've provided you with the same answer each time. Is there something else I can assist you with?
>
> Messages passed to the LangGraph agent:<br>
> The system message:<br>
> -----------------------<br>
> To answer the user's question, use this information which is part of the past conversation as a context:<br>
> - What's my name?<br>
> - My name is what?<br>
> - You can tell me what's my name.<br>
> - I'm unable to determine your name from the provided conversation. The phrase "What's my name?" is repeated multiple times, but it does not provide any information about your actual name. If you would like me to know your name, please share it with me.<br>
> - I'm sorry, but I still don't know your name. You haven't told me yet. If you'd like me to know your name, please share it with me.<br>
> - Your name is Bob.<br>
> - You didn't mention your name in the conversation. Could you please tell me your name?<br>
> - I don't have access to personal information about you, including your name. If you'd like to share your name or any other information, feel free to do so!<br>
> - I don't have access to your name or any personal information. If you'd like to share your name, I can use it in our conversation. Otherwise, I'll continue to assist you without using a name.<br>
> - Based on the provided conversation, your name is Bob. You stated, "Your name is Bob."<br>
> - Hi, my name is Bob!<br>
> - Based on the past conversation, your name is Bob. You stated, "Your name is Bob."<br>
> - Where do I live?<br>
> - Based on the past conversation, your name is Bob.<br>
> - Based on our previous conversation, you mentioned that your name is Bob.<br>
> - Based on our conversation, you mentioned earlier that your name is Bob.<br>
> - Based on our previous conversation, you mentioned that your name is Bob. You live in San Francisco.<br>
> - Bob, you've asked this question multiple times, and I've provided you with the same answer each time. Is there something else I can assist you with?
> 
> The human message:<br>
> -----------------------<br>
> What's my name?
> 
> ============================================================
> 
> Agent:<br>
> Based on our previous conversation, you mentioned that your name is Bob. ✔️
> 
> User:<br>
> Quit
> 
> Agent:<br>
> Have a nice day! 👋

### ⚒️ Tech stack ⚒️

OS:

- Windows `10`

Dependencies:

- [Python](https://www.python.org/) `3.11.8`
- [Dotenv](https://pypi.org/project/python-dotenv/) `1.0.1`
- [LangChain Python SDK](https://pypi.org/project/langchain/) `0.3.15`
- [LangChain Core Python SDK](https://pypi.org/project/langchain-core/) `0.3.31`
- [LangChain Community Python SDK](https://pypi.org/project/langchain-community/) `0.3.15`
- [Mistral Python SDK](https://pypi.org/project/mistralai/) `1.4.0`
- [LangChain Mistral Python SDK](https://pypi.org/project/langchain-mistralai/) `0.2.4`
- [LangGraph Python SDK](https://pypi.org/project/langgraph/) `0.2.67`
- [PostgreSQL Python Adapter](https://pypi.org/project/psycopg/) `3.2.4`
- [PostgreSQL Python Connection Pool](https://pypi.org/project/psycopg-pool/) `3.2.4`
- [pgvector Python SDK](https://pypi.org/project/pgvector/) `0.3.6`
- [Rich](https://pypi.org/project/rich/) `13.9.4`

<br>

## 📽️ Demonstration 📽️

The chat can be restarted as many times as needed, and the agent will retrieve any necessary information (e.g., user's name) from past conversations.

### Similarity search using limit-based approach

![Demonstration of the limit-based approach](https://github.com/rokbenko/ai-playground/blob/main/langgraph-tutorials/4-TUI_LangGraph_agent_PostgreSQL_memory_pgvector/assets/images/demonstration_limit.gif)

### Similarity search using threshold-based approach

![Demonstration of the threshold-based approach](https://github.com/rokbenko/ai-playground/blob/main/langgraph-tutorials/4-TUI_LangGraph_agent_PostgreSQL_memory_pgvector/assets/images/demonstration_threshold.gif)
