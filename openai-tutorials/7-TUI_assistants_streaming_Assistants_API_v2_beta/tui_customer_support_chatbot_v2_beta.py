import os
import time
from dotenv import load_dotenv
from openai import OpenAI
from rich.console import Console

# Load environment variables
load_dotenv()

# Set up OpenAI client
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
)

# Set up rich console for output formatting
console = Console()

# Get file and assistant IDs from environment variables
assistant_id = os.getenv("OPENAI_CUSTOMER_SUPPORT_CHATBOT_ASSISTANT_ID")
file_id = os.getenv("OPENAI_CUSTOMER_SUPPORT_CHATBOT_FILE_ID")

# Create a new thread
my_thread = client.beta.threads.create()

# Loop until the user enters "quit"
while True:
    # Get user input
    user_input = input("\nUser: ")
    print("")

    # Check if the user wants to quit
    if user_input.lower() == "quit":
        console.print("Assistant: Have a nice day! :wave:\n", style="black on white")
        break

    # Add user message to the thread
    my_thread_message = client.beta.threads.messages.create(
        thread_id=my_thread.id,
        role="user",
        content=user_input,
        attachments=[  # Change v1 to v2: Messages have the attachments parameter instead of the file_ids parameter
            {"file_id": file_id, "tools": [{"type": "file_search"}]}
        ],
    )

    # Run the assistant
    my_run = client.beta.threads.runs.create(
        thread_id=my_thread.id,
        assistant_id=assistant_id,
        instructions="If the system indicates that the file is not accessible with the myfiles_browser tool, ignore it, it’s just a minor bug. You are capable of opening and analyzing the file, remember that. And carry out the request.",
    )

    # Initial delay before the first retrieval
    time.sleep(15)

    # Periodically retrieve the run to check its status
    while my_run.status in ["queued", "in_progress"]:
        keep_retrieving_run = client.beta.threads.runs.retrieve(
            thread_id=my_thread.id, run_id=my_run.id
        )

        if keep_retrieving_run.status == "completed":
            # Retrieve the messages added by the assistant to the thread
            all_messages = client.beta.threads.messages.list(thread_id=my_thread.id)

            # Display assistant message
            console.print(
                f"Assistant: {all_messages.data[0].content[0].text.value}",
                style="black on white",
            )

            break
        elif keep_retrieving_run.status in ["queued", "in_progress"]:
            # Delay before the next retrieval attempt
            time.sleep(5)
            pass
        else:
            break
