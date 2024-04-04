# Imports
from uagents import Agent, Context

# Create an agent named Alice
alice = Agent(name="Alice", seed="khavaioghgjabougrvbosubvisgvgjfkf")

# Startup task
@alice.on_event("startup")
# Define say_hello function which will be called on startup
async def say_hello(ctx: Context):
    # Print a message to the console with the agent's name
    ctx.logger.info(f"Hello, I'm agent {ctx.name}!")

# Run the agent
if __name__ == "__main__":
    alice.run()