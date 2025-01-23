# Imports
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import HumanMessage
from rich.console import Console

# Initialize dotenv to load environment variables
load_dotenv()

# Initialize Rich for better output formatting and visualization
rich = Console()

# Initialize OpenAI LLM
llm = ChatOpenAI(api_key=os.getenv("OPENAI_API_KEY"), model="gpt-3.5-turbo")

# Initialize Tavily
tavily = TavilySearchResults(max_results=3)

# Create a LangGraph agent
langgraph_agent = create_react_agent(model=llm, tools=[tavily])


# Define a function to process chunks from the agent
def process_chunks(chunk):
    """
    Process a chunk of data and extract information about tool calls made by the agent.

    Parameters:
        chunk (dict): A dictionary containing information about the agent's messages.

    Returns:
        None

    This function processes a chunk of data and checks if it contains information about an agent. If the chunk contains
    an agent's message, it iterates over the messages in the agent's messages. For each message, it checks if the
    message contains tool calls. If a tool call is found, the function extracts the tool name and query from the
    message and prints a formatted message using the Rich library. If no tool call is found, the function extracts
    the agent's answer from the message and prints it using the Rich library.

    The function uses the Rich library for formatting and printing the messages.
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
        {"messages": [HumanMessage(content=user_question)]}
    ):
        # Process the chunks from the agent
        process_chunks(chunk)
