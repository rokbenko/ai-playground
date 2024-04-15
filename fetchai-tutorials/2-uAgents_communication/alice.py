# Imports
from uagents import Agent, Context, Model

# Class for the message
class Message(Model):
    message: str

# Create an agent named Alice
alice = Agent(name="Alice", seed="khavaioghgjabougrvbosubvisgvgjfkf", port=8000)

# On message
@alice.on_message(model=Message)
async def on_message(ctx: Context, sender: str, msg: Message):
    # Print Bob's message to the console
    ctx.logger.info(f"I've received a message from Bob: '{msg.message}'")

# Run the agent
if __name__ == "__main__":
    alice.run()