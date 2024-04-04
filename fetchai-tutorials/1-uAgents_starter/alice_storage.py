# Imports
from uagents import Agent, Context

# Create an agent named Alice
alice = Agent(name="Alice", seed="khavaioghgjabougrvbosubvisgvgjfkf")

# Interval task
@alice.on_interval(period=2.0)
# Define my_counter function which will be called every 2 seconds
async def my_counter(ctx: Context):
    # Get the current value of the counter
    current_count = ctx.storage.get("count") or 0

    # Print a message to the console with the current value of the counter
    ctx.logger.info(f"My count is: {current_count}")

    # Update the value of the counter by 1
    ctx.storage.set("count", current_count + 1)

# Run the agent
if __name__ == "__main__":
    alice.run()