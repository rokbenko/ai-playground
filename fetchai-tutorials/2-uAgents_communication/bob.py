# Imports
from uagents import Model, Agent, Context

# Alice's address
ALICE_ADDRESS = "agent1qtkp83xdzjn6pupps8jj309mu5km6h58cgcwzl3afw9frrnmqhk9kwrur80"

# Class for the message
class Message(Model):
    message: str

# Create an agent named Bob
bob = Agent(
    name = "Bob",
    seed = "kjbgfsipzwvgpifdsfncoerubcgbjbgfj",
    port = 8001,
    endpoint = ["http://127.0.0.1:8001/submit"]
)

# Bob's on interval task
@bob.on_interval(period = 2.0)
# Define send_message function which will be called every 2 seconds
async def send_message(ctx: Context):
    # Create a message for Alice
    msg = Message(message = "Hello, Alice! I'm agent Bob.")
    # Send the message to Alice
    await ctx.send(ALICE_ADDRESS, msg)

# Bob's on message task
@bob.on_message(model = Message)
# Define on_message function which will be called when Bob receives a message
async def on_message(ctx: Context, sender: str, msg: Message):
    # Print Alice's message to the console
    ctx.logger.info(f"I've received a message from {sender}: '{msg.message}'")

# Run the agent
if __name__ == "__main__":
    bob.run()