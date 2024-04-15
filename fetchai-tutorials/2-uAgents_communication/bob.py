# Imports
from uagents import Agent, Context, Model

# Alice's address
ALICE_ADDRESS = "agent1qtkp83xdzjn6pupps8jj309mu5km6h58cgcwzl3afw9frrnmqhk9kwrur80"

# Class for the message
class Message(Model):
    message: str

# Create an agent named Bob
bob = Agent(name="Bob", seed="kjbgfsipzwvgpifdsfncoerubcgbjbgfj", port=8001)

# Interval task
@bob.on_interval(period=2.0)
# Define send_message function which will be called every 2 seconds
async def send_message(ctx: Context):
    # Create a message for Alice
    msg = Message(message="Hello, Alice! I'm agent Bob.")
    # Send the message to Alice every 2 seconds
    await ctx.send(ALICE_ADDRESS, msg)

# Run the agent
if __name__ == "__main__":
    bob.run()