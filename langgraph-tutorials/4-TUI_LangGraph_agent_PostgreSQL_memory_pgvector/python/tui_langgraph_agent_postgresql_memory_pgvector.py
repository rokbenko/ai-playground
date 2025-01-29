# Imports
import os
import sys
import asyncio
import argparse
from dotenv import load_dotenv
from mistralai import Mistral
from langchain_mistralai import ChatMistralAI
from langchain_community.tools.tavily_search import TavilySearchResults
from psycopg_pool import AsyncConnectionPool
from psycopg.rows import dict_row
from pgvector.psycopg import register_vector_async
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import HumanMessage, SystemMessage
from rich.console import Console

# Parse terminal argument to choose similarity search type
parser = argparse.ArgumentParser(description="Choose similarity search type.")

parser.add_argument(
    "--similarity-search-type",
    choices=["limit", "threshold"],
    required=True,
    help="Type of similarity search to perform.",
)

args = parser.parse_args()

# Set similarity search type from the terminal argument
if args.similarity_search_type == "limit":
    similarity_search_type = "limit"
elif args.similarity_search_type == "threshold":
    similarity_search_type = "threshold"

# Initialize dotenv to load environment variables
load_dotenv()

# Initialize Rich for better output formatting and visualization
rich = Console()

# Initialize Mistral AI LLM
llm = ChatMistralAI(
    api_key=os.getenv("MISTRAL_API_KEY"),
    model_name="mistral-large-latest",
)

# Initialize Mistral AI client
mistral_client = Mistral(
    api_key=os.getenv("MISTRAL_API_KEY"),
)

# Initialize Tavily
tavily = TavilySearchResults(max_results=3)


# Define an async function to process chunks from the agent
async def process_chunks(chunk, conn):
    """
    Asynchronously processes a chunk from the agent and displays information about tool calls or the agent's answer.

    Parameters:
        chunk (dict): A dictionary containing information about the agent's messages.
        conn (asyncpg.Connection): The database connection object.

    Returns:
        None

    This function processes a chunk of data to check for agent messages asynchronously.
    It iterates over the messages and checks for tool calls.
    If a tool call is found, it extracts the tool name and query, then prints a formatted message using the Rich library.
    If no tool call is found, it extracts and prints the agent's answer using the Rich library.
    Additionally, it updates the database with the agent's response and logs the interaction.
    """

    # Check if the chunk contains an agent's message
    if "agent" in chunk:
        # Iterate over the messages in the chunk
        for message in chunk["agent"]["messages"]:
            # Check if the message contains tool calls
            if "tool_calls" in message.additional_kwargs:
                # If the message contains tool calls, extract and display an informative message with tool call details

                # Extract all the tool calls
                tool_calls = message.additional_kwargs["tool_calls"]

                # Iterate over the tool calls
                for tool_call in tool_calls:
                    # Extract the tool name
                    tool_name = tool_call["function"]["name"]

                    # Extract the tool query
                    tool_arguments = eval(tool_call["function"]["arguments"])
                    tool_query = tool_arguments["query"]

                    # Display an informative message with tool call details
                    rich.print(
                        f"\nThe agent is calling the tool [on deep_sky_blue1]{tool_name}[/on deep_sky_blue1] with the query [on deep_sky_blue1]{tool_query}[/on deep_sky_blue1]. Please wait for the agent's answer[deep_sky_blue1]...[/deep_sky_blue1]",
                        style="deep_sky_blue1",
                    )
            else:
                # If the message doesn't contain tool calls, extract and display the agent's answer

                # Extract the agent's answer
                agent_answer = message.content

                # Create the embedding vector for the agent's answer
                embeddings_response = mistral_client.embeddings.create(
                    model="mistral-embed",
                    inputs=[agent_answer],
                )

                # Extract the embedding vector for the agent's answer
                agent_answer_embedding = embeddings_response.data[0].embedding

                # Insert the agent's answer and its embedding vector into the database
                await conn.execute(
                    "INSERT INTO chat (role, message, embedding_vector) VALUES (%s, %s, %s)",
                    (
                        "agent",
                        agent_answer,
                        agent_answer_embedding,
                    ),
                )

                # Display the agent's answer
                rich.print(f"\nAgent:\n{agent_answer}", style="black on white")


# Define an async function to chat with the agent
async def main():
    """
    Entry point of the application. Connects to a PostgreSQL database, initializes a persistent chat memory utilizing pgvector,
    creates a LangGraph agent, and handles user interaction in a loop until the user chooses to quit.

    Parameters:
        None

    Returns:
        None

    This function performs the following steps:
    1. Connects to the PostgreSQL database using an async connection pool.
    2. Initializes a persistent chat memory utilizing pgvector.
    3. Creates a LangGraph agent with the specified model and tools.
    4. Enters a loop to interact with the user:
        - Prompts the user for a question.
        - Checks if the user wants to quit.
        - Uses the LangGraph agent to get the agent's answer.
        - Processes the chunks from the agent.

    The function supports two options for similarity search:
    - "limit": Returns the top 5 most similar messages.
    - "threshold": Returns messages that have a cosine similarity greater than 0.25.
    """

    # Connect to the PostgreSQL database using an async connection pool
    async with AsyncConnectionPool(
        # The format of the connection string is as follows:
        # "postgres://<username>:<password>@<host>:<port>/<database>?<options>"
        conninfo=f"postgres://{os.getenv('PSQL_USERNAME')}:{os.getenv('PSQL_PASSWORD')}"
        f"@{os.getenv('PSQL_HOST')}:{os.getenv('PSQL_PORT')}/{os.getenv('PSQL_DATABASE')}"
        f"?sslmode={os.getenv('PSQL_SSLMODE')}",
        max_size=20,  # Maximum number of connections in the pool
        kwargs={
            "autocommit": True,
            "prepare_threshold": 0,
            "row_factory": dict_row,
        },
    ) as pool, pool.connection() as conn:
        # Register the vector data type with the database connection
        await register_vector_async(conn)

        # Enable the pgvector extension in the database if it's not already enabled
        await conn.execute("CREATE EXTENSION IF NOT EXISTS vector")

        # Create a table in the database if it's not already created
        await conn.execute(
            """
            CREATE TABLE IF NOT EXISTS chat (
                id bigserial PRIMARY KEY,
                role varchar(10),
                message text,
                embedding_vector vector(1024)
            )
            """
        )

        # Create a LangGraph agent
        langgraph_agent = create_react_agent(model=llm, tools=[tavily])

        # Loop until the user chooses to quit the chat
        while True:
            # Get the user's question and display it in the terminal
            user_question = input("\nUser:\n")

            # Check if the user wants to quit the chat
            if user_question.lower() == "quit":
                rich.print(
                    "\nAgent:\nHave a nice day! :wave:\n", style="black on white"
                )
                break

            # Create the embedding vector for the user's question
            embeddings_response = mistral_client.embeddings.create(
                model="mistral-embed",
                inputs=[user_question],
            )

            # Extract the embedding vector for the user's question
            user_question_embedding = embeddings_response.data[0].embedding

            # Perform similarity search based on the choosen similarity search type
            # If similarity_search_type is "limit"
            if similarity_search_type == "limit":
                # Return the top 5 most similar past messages stored in the database
                similarity_search = await conn.execute(
                    """
                    WITH ranked_messages AS (
                        SELECT 
                            message,
                            ROW_NUMBER() OVER (
                                PARTITION BY message 
                                ORDER BY embedding_vector <=> %s::vector
                            ) as rn
                        FROM chat
                    )
                    SELECT message 
                    FROM ranked_messages 
                    WHERE rn = 1 
                    LIMIT 5
                    """,
                    (user_question_embedding,),
                )

            # If similarity_search_type is "threshold"
            elif similarity_search_type == "threshold":
                # Return all past messages stored in the database that have a cosine similarity greater than 0.25
                similarity_search = await conn.execute(
                    """
                    WITH ranked_messages AS (
                        SELECT 
                            message,
                            1 - (embedding_vector <=> %s::vector) AS cosine_similarity,
                            ROW_NUMBER() OVER (
                                PARTITION BY message 
                                ORDER BY 1 - (embedding_vector <=> %s::vector) DESC
                            ) as rn
                        FROM chat
                        WHERE embedding_vector <=> %s::vector < %s
                    )
                    SELECT message, cosine_similarity
                    FROM ranked_messages 
                    WHERE rn = 1 
                    ORDER BY cosine_similarity DESC
                    """,
                    (
                        user_question_embedding,
                        user_question_embedding,
                        user_question_embedding,
                        0.25,
                    ),
                )

            # Insert the user's question and its embedding vector into the database
            await conn.execute(
                "INSERT INTO chat (role, message, embedding_vector) VALUES (%s, %s, %s)",
                (
                    "user",
                    user_question,
                    user_question_embedding,
                ),
            )

            # Fetch the similarity search results
            similarity_search_results = await similarity_search.fetchall()

            rich.print("\n==========================================================\n")

            # Display all similarity search result messages
            # Those will be passed to the LangGraph agent as the system message
            rich.print(
                "[on deep_sky_blue1]Similarity search results:[/on deep_sky_blue1]",
                style="deep_sky_blue1",
            )

            for i, query_result in enumerate(similarity_search_results):
                rich.print(
                    f"Message #{i+1}: {query_result['message']}",
                    style="deep_sky_blue1",
                )

            # Prepare messages to be passed to the LangGraph agent
            # Create a list to store the messages
            similar_messages = []

            # Iterate over the similarity search results and add them to the list
            for query_result in similarity_search_results:
                similar_messages.append(query_result["message"])

            # Add the user's question to the HumanMessage object
            messages = [HumanMessage(content=user_question)]

            # If there are similar messages returned from the similarity search, add them to the SystemMessage object
            if similar_messages:
                join_similar_messages = "\n".join(similar_messages)
                system_message = f"To answer the user's question, use this information which is part of the past conversation as a context:\n{join_similar_messages}"
                messages.insert(0, SystemMessage(content=system_message))

            # Initialize the system message and human message
            system_message = None
            human_message = None

            # Iterate over the messages and extract the system and human messages
            for message in messages:
                # Check if the message is a system message
                if isinstance(message, SystemMessage):
                    system_message = message

                # Check if the message is a human message
                elif isinstance(message, HumanMessage):
                    human_message = message

            # Display all messages that will be passed to the LangGraph agent (system and human messages)
            rich.print(
                "[on deep_sky_blue1]\nMessages passed to the LangGraph agent:[/on deep_sky_blue1]",
                style="deep_sky_blue1",
            )

            if system_message:
                rich.print(
                    f"\nThe system message:\n------------------------------------------------------------\n{system_message.content}",
                    style="deep_sky_blue1",
                )
            if human_message:
                rich.print(
                    f"\nThe human message:\n------------------------------------------------------------\n{human_message.content}",
                    style="deep_sky_blue1",
                )

            rich.print("\n============================================================")

            # Use the async stream method of the LangGraph agent to get the agent's answer
            async for chunk in langgraph_agent.astream({"messages": messages}):
                # Process the chunks from the agent
                await process_chunks(chunk, conn)


if __name__ == "__main__":
    if sys.platform == "win32":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    # Run the main async function
    asyncio.run(main())
