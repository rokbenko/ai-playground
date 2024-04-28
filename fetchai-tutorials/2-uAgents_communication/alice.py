# Imports
from uagents import Model, Agent, Context

# Class for the message
class Message(Model):
    message: str

# Create an agent named Alice
alice = Agent(
    name = "Alice",
    seed = "khavaioghgjabougrvbosubvisgvgjfkf",
    port = 8000,
    endpoint = ["http://127.0.0.1:8000/submit"]
)

# Alice's on message task
@alice.on_message(model = Message)
# Define on_message function which will be called when Alice receives a message
async def on_message(ctx: Context, sender: str, msg: Message):
    # Print Bob's message to the console
    ctx.logger.info(f"I've received a message from {sender}: '{msg.message}'")

    # Create a message for Bob
    msg = Message(message = "Hello, Bob! I'm agent Alice.")
    # Send the message to Bob
    await ctx.send(sender, msg)

# Run the agent
if __name__ == "__main__":
    alice.run()