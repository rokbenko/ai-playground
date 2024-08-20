# Imports
import os
import sys
import asyncio
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults
from psycopg_pool import AsyncConnectionPool
from psycopg.rows import dict_row
from langgraph.checkpoint.postgres.aio import AsyncPostgresSaver
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import HumanMessage, AIMessage
from rich.console import Console

# Initialize dotenv to load environment variables
load_dotenv()

# Initialize Rich for better output formatting and visualization
rich = Console()

# Initialize OpenAI LLM
llm = ChatOpenAI(api_key=os.getenv("OPENAI_API_KEY"), model="gpt-4o-mini")

# Initialize Tavily
tavily = TavilySearchResults(max_results=3)


# Define a function to process chunks from the agent
def process_chunks(chunk):
    """
    Process a chunk of data and extract information about tool calls made by the agent.

    This function processes a chunk of data and checks if it contains information about an agent. If the chunk contains
    an agent's message, it iterates over the messages in the agent's messages. For each message, it checks if the
    message contains tool calls. If a tool call is found, the function extracts the tool name and query from the
    message and prints a formatted message using the Rich library. If no tool call is found, the function extracts
    the agent's answer from the message and prints it using the Rich library, allowing for a visually appealing output.

    Parameters:
        chunk (dict): A dictionary containing information about the agent's messages.

    Returns:
        None
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
                agent_anser = message.content

                # Display the agent's answer
                rich.print(f"\nAgent:\n{agent_anser}", style="black on white")


# Define an async function to process checkpoints from the memory
async def process_checkpoints(checkpoints):
    """
    Asynchronously process a list of checkpoints, extracting and displaying key information about each checkpoint,
    including timestamp, checkpoint ID, and messages exchanged between the user and the agent.

    This function iterates over an asynchronous generator of checkpoints, collecting relevant details for each
    checkpoint, such as the timestamp of the checkpoint, its unique ID, and any associated messages. It formats
    and prints this information using the Rich library, allowing for a visually appealing output.

    Each checkpoint consists of a tuple where the first element is the index and the second element is an object
    containing various details about the checkpoint. The function distinguishes between messages from the user
    and the agent, displaying them accordingly.

    Parameters:
        checkpoints (list): A list of checkpoint tuples to be processed.

    Returns:
        None
    """

    rich.print("\n==========================================================\n")

    # Initialize an empty list to store the checkpoints
    checkpoints_list = []

    # Iterate over the checkpoints and add them to the list in an async way
    async for checkpoint_tuple in checkpoints:
        checkpoints_list.append(checkpoint_tuple)

    # Iterate over the list of checkpoints
    for idx, checkpoint_tuple in enumerate(checkpoints_list):
        # Extract key information about the checkpoint
        checkpoint = checkpoint_tuple.checkpoint
        messages = checkpoint["channel_values"].get("messages", [])

        # Display checkpoint information
        rich.print(f"[white]Checkpoint:[/white]")
        rich.print(f"[black]Timestamp: {checkpoint['ts']}[/black]")
        rich.print(f"[black]Checkpoint ID: {checkpoint['id']}[/black]")

        # Display checkpoint messages
        for message in messages:
            if isinstance(message, HumanMessage):
                rich.print(
                    f"[bright_magenta]User: {message.content}[/bright_magenta] [bright_cyan](Message ID: {message.id})[/bright_cyan]"
                )
            elif isinstance(message, AIMessage):
                rich.print(
                    f"[bright_magenta]Agent: {message.content}[/bright_magenta] [bright_cyan](Message ID: {message.id})[/bright_cyan]"
                )

        rich.print("")

    rich.print("==========================================================")


# Define an async function to chat with the agent
async def main():
    """
    The main function is the entry point of the program. It connects to a PostgreSQL database using an async connection pool,
    initializes a persistent chat memory, creates a LangGraph agent, and loops until the user chooses to quit the chat.
    In each iteration, it gets the user's question, checks if the user wants to quit, and uses the LangGraph agent to get the agent's answer.
    It then processes the chunks from the agent and lists all checkpoints that match a given configuration.

    Parameters:
        None

    Returns:
        None
    """

    # Connect to the PostgreSQL database using an async connection pool
    async with AsyncConnectionPool(
        # The format of the connection string is as follows:
        # "postgres://<username>:<password>@<host>:<port>/<database>?<options>"
        # In this case:
        # - Username: postgres
        # - Password: postgres
        # - Host: localhost (indicating the database is hosted on the local machine)
        # - Port: 5432 (the default port for PostgreSQL)
        # - Database: postgres (the name of the database to connect to)
        # - Options: sslmode=disable (disables SSL for the connection)
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
        # Initialize persistent chat memory
        memory = AsyncPostgresSaver(conn)

        # IMPORTANT: You need to call .setup() the first time you're using your memory
        # await memory.setup()

        # Create a LangGraph agent
        langgraph_agent = create_react_agent(
            model=llm, tools=[tavily], checkpointer=memory
        )

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

            # Use the async stream method of the LangGraph agent to get the agent's answer
            async for chunk in langgraph_agent.astream(
                {"messages": [HumanMessage(content=user_question)]},
                {"configurable": {"thread_id": "1"}},
            ):
                # Process the chunks from the agent
                process_chunks(chunk)

                # Use the async list method of the memory to list all checkpoints that match a given configuration
                checkpoints = memory.alist({"configurable": {"thread_id": "1"}})
                # Process the checkpoints from the memory in an async way
                await process_checkpoints(checkpoints)


if __name__ == "__main__":
    if sys.platform == "win32":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    # Run the main async function
    asyncio.run(main())
