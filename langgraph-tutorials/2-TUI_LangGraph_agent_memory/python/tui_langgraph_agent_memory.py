# Imports
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import HumanMessage, AIMessage
from rich.console import Console

# Initialize dotenv to load environment variables
load_dotenv()

# Initialize Rich for better output formatting and visualization
rich = Console()

# Initialize OpenAI LLM
llm = ChatOpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    model="gpt-4o-mini",
)

# Initialize Tavily
tavily = TavilySearchResults(max_results=3)

# Initialize chat memory (Note: This is in-memory only, not persistent)
memory = MemorySaver()

# Create a LangGraph agent
langgraph_agent = create_react_agent(model=llm, tools=[tavily], checkpointer=memory)


# Define a function to process chunks from the agent
def process_chunks(chunk):
    """
    Processes a chunk from the agent and displays information about tool calls or the agent's answer.

    Parameters:
        chunk (dict): A dictionary containing information about the agent's messages.

    Returns:
        None

    This function processes a chunk of data to check for agent messages.
    It iterates over the messages and checks for tool calls.
    If a tool call is found, it extracts the tool name and query, then prints a formatted message using the Rich library.
    If no tool call is found, it extracts and prints the agent's answer using the Rich library.
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

                # Display the agent's answer
                rich.print(f"\nAgent:\n{agent_answer}", style="black on white")


# Define a function to process checkpoints
def process_checkpoints(checkpoints):
    """
    Processes a list of checkpoints and displays relevant information.

    Parameters:
        checkpoints (list): A list of checkpoint tuples to process.

    Returns:
        None

    This function processes a list of checkpoints.
    It iterates over the checkpoints and displays the following information for each checkpoint:
    - Timestamp
    - Checkpoint ID
    - Messages associated with the checkpoint
    """

    rich.print("\n==========================================================\n")

    for idx, checkpoint_tuple in enumerate(checkpoints):
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


# Loop until the user chooses to quit the chat
while True:
    # Get the user's question and display it in the terminal
    user_question = input("\nUser:\n")

    # Check if the user wants to quit the chat
    if user_question.lower() == "quit":
        rich.print("\nAgent:\nHave a nice day! :wave:\n", style="black on white")
        break

    # Use the stream method of the LangGraph agent to get the agent's answer
    for chunk in langgraph_agent.stream(
        {"messages": [HumanMessage(content=user_question)]},
        {"configurable": {"thread_id": "1"}},
    ):
        # Process the chunks from the agent
        process_chunks(chunk)

        # List all checkpoints that match a given configuration
        checkpoints = memory.list({"configurable": {"thread_id": "1"}})
        # Process the checkpoints
        process_checkpoints(checkpoints)
