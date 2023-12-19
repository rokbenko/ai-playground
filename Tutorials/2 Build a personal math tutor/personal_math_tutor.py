import os
from openai import OpenAI
client = OpenAI()
OpenAI.api_key = os.getenv('OPENAI_API_KEY')

# Step 1: Create an Assistant
my_assistant = client.beta.assistants.create(
    model="gpt-4",
    instructions="You are a personal math tutor. When asked a question, write and run Python code to answer the question.",
    name="Math Tutor",
    tools=[{"type": "code_interpreter"}],
)
print(f"This is the assistant object: {my_assistant} \n")

# Step 2: Create a Thread
my_thread = client.beta.threads.create()
print(f"This is the thread object: {my_thread} \n")

# Step 3: Add a Message to a Thread
my_thread_message = client.beta.threads.messages.create(
  thread_id=my_thread.id,
  role="user",
  content="I need to solve the equation `3x + 11 = 14`. Can you help me?",
)
print(f"This is the message object: {my_thread_message} \n")

# Step 4: Run the Assistant
my_run = client.beta.threads.runs.create(
  thread_id=my_thread.id,
  assistant_id=my_assistant.id,
  instructions="Please address the user as Rok Benko."
)
print(f"This is the run object: {my_run} \n")

# Step 5: Periodically retrieve the Run to check on its status to see if it has moved to completed
while my_run.status == "in_progress":
    keep_retrieving_run = client.beta.threads.runs.retrieve(
        thread_id=my_thread.id,
        run_id=my_run.id
    )
    print(f"Run status: {keep_retrieving_run.status}")

    if keep_retrieving_run.status == "completed":
        print("\n")
        break
    else:
        print(f"Run status: {keep_retrieving_run.status}")
        break

# Step 6: Retrieve the Messages added by the Assistant to the Thread
all_messages = client.beta.threads.messages.list(
  thread_id=my_thread.id
)

print("------------------------------------------------------------ \n")

print(f"User: {my_thread_message.content[0].text.value}")
print(f"Assistant: {all_messages.data[0].content[0].text.value}")
