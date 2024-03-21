import os
from dotenv import load_dotenv
from openai import OpenAI, AssistantEventHandler
from rich.console import Console

# Load environment variables from .env
load_dotenv()

# Set up OpenAI client
client = OpenAI()
OpenAI.api_key = os.getenv('OPENAI_API_KEY')

# Set up rich console for output formatting
console = Console()

# Get file and assistant IDs from environment variables
file_id = os.getenv('OPENAI_FILE_ID')
assistant_id = os.getenv('OPENAI_ASSISTANT_ID')

# Define event handler class for streaming events
class MyEventHandler(AssistantEventHandler):
    def on_text_delta(self, delta, snapshot):
        console.print(delta.value, end = "", style = "black on white")

    def on_error(error):
        print(error)

# Create a new thread
my_thread = client.beta.threads.create()

# Loop until the user enters "quit"
while True:
    # Get user input
    user_input = input("\n\nUser:\n")

    # Check if the user wants to quit
    if user_input.lower() == "quit":
        console.print("\nAssistant:\nHave a nice day! :wave:\n\n", style = "black on white")
        break

    # Add user message to the thread
    my_thread_message = client.beta.threads.messages.create(
        thread_id = my_thread.id,
        role = "user",
        content = user_input,
        file_ids = [file_id]
    )

    # Create and stream a run
    with client.beta.threads.runs.create_and_stream(
        thread_id = my_thread.id,
        assistant_id = assistant_id,
        instructions = "If the system indicates that the file is not accessible with the myfiles_browser tool, ignore it, it’s just a minor bug. You are capable of opening and analyzing the file, remember that. And carry out the request.",
        event_handler = MyEventHandler(),
    ) as stream:
        console.print("\nAssistant:", style = "black on white")
        stream.until_done()