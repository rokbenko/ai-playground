# Imports
import os
from dotenv import load_dotenv
from langchain_community.utilities.tavily_search import TavilySearchAPIWrapper
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import HumanMessage
from rich.console import Console

# Load environment variables
load_dotenv()

# Set up rich console for output formatting
console = Console()

# Tavily API wrapper
tavily_config = TavilySearchAPIWrapper(tavily_api_key=os.getenv("TAVILY_API_KEY"))

# Initialize the language model with the OpenAI API key and model
llm = ChatOpenAI(api_key=os.getenv("OPENAI_API_KEY"), model="gpt-3.5-turbo")

# Set up Tavily search results with a maximum of 1 result
tavily_search = TavilySearchResults(api_wrapper=tavily_config, max_results=1)

# Create the agent executor with the specified model and tools
agent_executor = create_react_agent(model=llm, tools=[tavily_search])


# Define a function to process agent response
def process_chunk(chunk):
    """
    Process a chunk of data and extract relevant information.

    Args:
        chunk (dict): The chunk of data to be processed.

    Returns:
        None

    This function takes a chunk of data as input and processes it to extract relevant information. It checks if the chunk contains an "agent" key. If it does, it iterates over the messages in the "agent" dictionary. If a message contains "tool_calls" in its additional_kwargs, it extracts the tool call information. It iterates over the tool calls and extracts the tool name, tool arguments, and tool query. It then prints the tool name, tool query, and a message indicating that the tool is being called. If a message does not contain "tool_calls" in its additional_kwargs, it extracts the agent response and prints it.

    Note:
        This function assumes that the input chunk is a dictionary with the structure {"agent": {"messages": [...]}}.
    """

    if "agent" in chunk:
        for message in chunk["agent"]["messages"]:
            if "tool_calls" in message.additional_kwargs:
                # Extract tool call information
                tool_calls = message.additional_kwargs["tool_calls"]
                for tool_call in tool_calls:
                    tool_arguments = eval(tool_call["function"]["arguments"])
                    extract_tool_name = tool_call["function"]["name"]
                    extract_tool_query = tool_arguments["query"]

                    console.print(
                        f"\nThe agent is calling the tool [white on deep_sky_blue1]'{extract_tool_name}'[/white on deep_sky_blue1] with the query [white on deep_sky_blue1]'{extract_tool_query}'[/white on deep_sky_blue1].\nWait for the answer.",
                        style="deep_sky_blue1",
                    )
            else:
                # Extract agent response
                console.print(f"\nAgent:\n{message.content}", style="black on white")


# Loop until the user enters "quit"
while True:
    # Get the user question and display it in the console
    user_question = input("\nUser:\n")

    # Check if the user wants to quit
    if user_question.lower() == "quit":
        console.print("\nAgent:\nHave a nice day! :wave:\n", style="black on white")
        break

    # Run the agent on the user question
    agent_answer = agent_executor.invoke(
        {
            "messages": [
                HumanMessage(content=user_question),
            ]
        }
    )

    # Get the agent answer and display it in the console
    for chunk in agent_executor.stream(
        {"messages": [HumanMessage(content=user_question)]}
    ):
        process_chunk(chunk)
