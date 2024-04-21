# #1 uAgents starter

## Short description

Python examples on how to:

- create an agent with a startup task (see `alice.py`),
- create an agent with an interval task (see `alice_interval_task.py`),
- create an agent and get its address (see `alice_address.py`), and
- create a stateful agent (see `alice_storage.py`).

<br>

## Working examples in Python

If you run `alice.py`, you should get the following response:

> INFO:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [Alice]: Hello, I'm agent Alice!<br>
> INFO:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [Alice]: Starting server on http://0.0.0.0:8000 (Press CTRL+C to quit)

If you run `alice_interval_task.py`, you should get the following response:

> INFO:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [Alice]: Hello, I'm agent Alice!<br>
> INFO:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [Alice]: Starting server on http://0.0.0.0:8000 (Press CTRL+C to quit)<br>
> INFO:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [Alice]: Hello, I'm agent Alice!<br>
> INFO:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [Alice]: Hello, I'm agent Alice!<br>
> INFO:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [Alice]: Hello, I'm agent Alice!<br>
> INFO:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [Alice]: Hello, I'm agent Alice!<br>
> INFO:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [Alice]: Hello, I'm agent Alice!

If you run `alice_address.py`, you should get the following response:

> INFO:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [Alice]: Hello, I'm agent Alice and my address is agent1qtkp83xdzjn6pupps8jj309mu5km6h58cgcwzl3afw9frrnmqhk9kwrur80.<br>
> INFO:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [Alice]: Starting server on http://0.0.0.0:8000 (Press CTRL+C to quit)<br>
> INFO:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [Alice]: Hello, I'm agent Alice and my address is agent1qtkp83xdzjn6pupps8jj309mu5km6h58cgcwzl3afw9frrnmqhk9kwrur80.<br>
> INFO:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [Alice]: Hello, I'm agent Alice and my address is agent1qtkp83xdzjn6pupps8jj309mu5km6h58cgcwzl3afw9frrnmqhk9kwrur80.<br>
> INFO:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [Alice]: Hello, I'm agent Alice and my address is agent1qtkp83xdzjn6pupps8jj309mu5km6h58cgcwzl3afw9frrnmqhk9kwrur80.<br>
> INFO:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [Alice]: Hello, I'm agent Alice and my address is agent1qtkp83xdzjn6pupps8jj309mu5km6h58cgcwzl3afw9frrnmqhk9kwrur80.<br>
> INFO:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [Alice]: Hello, I'm agent Alice and my address is agent1qtkp83xdzjn6pupps8jj309mu5km6h58cgcwzl3afw9frrnmqhk9kwrur80.

If you run `alice_storage.py`, you should get the following response:

> INFO:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [Alice]: My count is: 0<br>
> INFO:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [Alice]: My count is: 1<br>
> INFO:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [Alice]: My count is: 2<br>
> INFO:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [Alice]: My count is: 3<br>
> INFO:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [Alice]: My count is: 4<br>
> INFO:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [Alice]: My count is: 5

<br>

Environment:

- Windows `10`
- Python `3.11.8`
- uAgents Python SDK `0.11.0`
