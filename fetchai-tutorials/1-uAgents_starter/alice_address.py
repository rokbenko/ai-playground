# Imports
from uagents import Agent, Context

# Create an agent named Alice
alice = Agent(name="Alice", seed="khavaioghgjabougrvbosubvisgvgjfkf")

# Interval task
@alice.on_interval(period=2.0)
# Define get_address function which will be called every 2 seconds
async def get_address(ctx: Context):
    # Print a message to the console with the agent's name and address
    ctx.logger.info(f"Hello, I'm agent {ctx.name} and my address is {ctx.address}.")

# Run the agent
if __name__ == "__main__":
    alice.run()