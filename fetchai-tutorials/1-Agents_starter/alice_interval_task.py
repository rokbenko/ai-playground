# Imports
from uagents import Agent, Context

# Create an agent named Alice
alice = Agent(name="Alice", seed="khavaioghgjabougrvbosubvisgvgjfkf")

# Interval task
@alice.on_interval(period=2.0)
# Define say_hello_interval function which will be called every 2 seconds
async def say_hello_interval(ctx: Context):
    # Print a message to the console with the agent's name
    ctx.logger.info(f"Hello, I'm agent {ctx.name}!")

# Run the agent
if __name__ == "__main__":
    alice.run()