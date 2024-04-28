# Imports
from uagents import Model, Agent, Context, Bureau

# Class for the message
class Message(Model):
    message: str

# Create agents named Alice and Bob
alice = Agent(
    name = "alice",
    seed = "igfdba9pub4590bgdbgdfjbgdlkhbkdhbdhkd89ht"
)
bob = Agent(
    name = "bob",
    seed = "ldsjbg9bqw7bt390bsbdgjfsbgkdfgiseht8h0agh"
)

# Alice's on message task
@alice.on_message(model = Message)
# Define alice_message_handler function which will be called when Alice receives a message
async def alice_message_handler(ctx: Context, sender: str, msg: Message):
    # Print Bob's message to the console
    ctx.logger.info(f"I've received a message from {sender}: '{msg.message}'")

    # Create a message for Bob
    msg = Message(message = "Hello, Bob! I'm agent Alice.")
    # Send the message to Bob
    await ctx.send(bob.address, msg)

# Bob's on interval task
@bob.on_interval(period = 4.0)
# Define start_conversation function which will be called every 2 seconds
async def start_conversation(ctx: Context):
    # Create a message for Alice
    msg = Message(message = "Hello, Alice! I'm agent Bob.")
    # Send the message to Alice
    await ctx.send(alice.address, msg)

# Bob's on message task
@bob.on_message(model = Message)
# Define bob_message_handler function which will be called when Bob receives a message
async def bob_message_handler(ctx: Context, sender: str, msg: Message):
    # Print Alice's message to the console
    ctx.logger.info(f"I've received a message from {sender}: '{msg.message}'")

# Add Alice and Bob to the Bureau
bureau = Bureau()
bureau.add(alice)
bureau.add(bob)

# Run all the agents in the Bureau
if __name__ == "__main__":
    bureau.run()