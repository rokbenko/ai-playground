# #1 uAgents starter

<br>

## 📖 Description 📖

Python examples on how to:

- build a Fetch.ai agent with a startup task (see [`alice.py`](https://github.com/rokbenko/ai-playground/blob/main/fetchai-tutorials/1-uAgents_starter/alice.py)),
- build a Fetch.ai agent with an interval task (see [`alice_interval_task.py`](https://github.com/rokbenko/ai-playground/blob/main/fetchai-tutorials/1-uAgents_starter/alice_interval_task.py)),
- build a Fetch.ai agent and get its address (see [`alice_address.py`](https://github.com/rokbenko/ai-playground/blob/main/fetchai-tutorials/1-uAgents_starter/alice_address.py)), and
- build a Fetch.ai stateful agent (see [`alice_storage.py`](https://github.com/rokbenko/ai-playground/blob/main/fetchai-tutorials/1-uAgents_starter/alice_storage.py)).

<br>

## 🧠 Learning goals 🧠

- **Build a Fetch.ai agent with a startup task:** We will build a Fetch.ai agent and define a startup task that executes when the agent starts. The agent will log a greeting message with its name when we start the agent. This demonstrates how to initialize tasks and set up basic event handling in agent-based systems.
- **Build a Fetch.ai agent with an interval task:** We will build a Fetch.ai agent and define an interval task that executes periodically. The agent will log its name every 2 seconds. This demonstrates how to initialize recurring tasks in agent-based systems.
- **Build a Fetch.ai agent and get its address:** We will build a Fetch.ai agent and get its address. By using an interval task, the agent will log its name and address every 2 seconds. This demonstrates how to get agent addresses in agent-based systems. Knowing agent addresses is necessary for agents to be able to communicate between themselves.
- **Build a Fetch.ai stateful agent:** We will build a Fetch.ai agent and give it a state. By using an interval task, the agent will manage a counter value that increments every 2 seconds and logs its current count. This demonstrates how to make an agent stateful. Agents being stateful is necessary for more complex agent-based systems where managing data persistently over time is a must.

<br>

## 🔥 Working examples in Python 🔥

If you run [`alice.py`](https://github.com/rokbenko/ai-playground/blob/main/fetchai-tutorials/1-uAgents_starter/alice.py), you should get the following response:

> INFO:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [Alice]: Hello, I'm agent Alice!<br>
> INFO:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [Alice]: Starting server on http://0.0.0.0:8000 (Press CTRL+C to quit)

If you run [`alice_interval_task.py`](https://github.com/rokbenko/ai-playground/blob/main/fetchai-tutorials/1-uAgents_starter/alice_interval_task.py), you should get the following response:

> INFO:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [Alice]: Hello, I'm agent Alice!<br>
> INFO:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [Alice]: Starting server on http://0.0.0.0:8000 (Press CTRL+C to quit)<br>
> INFO:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [Alice]: Hello, I'm agent Alice!<br>
> INFO:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [Alice]: Hello, I'm agent Alice!<br>
> INFO:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [Alice]: Hello, I'm agent Alice!<br>
> INFO:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [Alice]: Hello, I'm agent Alice!<br>
> INFO:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [Alice]: Hello, I'm agent Alice!

If you run [`alice_address.py`](https://github.com/rokbenko/ai-playground/blob/main/fetchai-tutorials/1-uAgents_starter/alice_address.py), you should get the following response:

> INFO:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [Alice]: Hello, I'm agent Alice and my address is agent1qtkp83xdzjn6pupps8jj309mu5km6h58cgcwzl3afw9frrnmqhk9kwrur80.<br>
> INFO:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [Alice]: Starting server on http://0.0.0.0:8000 (Press CTRL+C to quit)<br>
> INFO:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [Alice]: Hello, I'm agent Alice and my address is agent1qtkp83xdzjn6pupps8jj309mu5km6h58cgcwzl3afw9frrnmqhk9kwrur80.<br>
> INFO:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [Alice]: Hello, I'm agent Alice and my address is agent1qtkp83xdzjn6pupps8jj309mu5km6h58cgcwzl3afw9frrnmqhk9kwrur80.<br>
> INFO:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [Alice]: Hello, I'm agent Alice and my address is agent1qtkp83xdzjn6pupps8jj309mu5km6h58cgcwzl3afw9frrnmqhk9kwrur80.<br>
> INFO:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [Alice]: Hello, I'm agent Alice and my address is agent1qtkp83xdzjn6pupps8jj309mu5km6h58cgcwzl3afw9frrnmqhk9kwrur80.<br>
> INFO:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [Alice]: Hello, I'm agent Alice and my address is agent1qtkp83xdzjn6pupps8jj309mu5km6h58cgcwzl3afw9frrnmqhk9kwrur80.

If you run [`alice_storage.py`](https://github.com/rokbenko/ai-playground/blob/main/fetchai-tutorials/1-uAgents_starter/alice_storage.py), you should get the following response:

> INFO:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [Alice]: My count is: 0<br>
> INFO:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [Alice]: My count is: 1<br>
> INFO:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [Alice]: My count is: 2<br>
> INFO:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [Alice]: My count is: 3<br>
> INFO:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [Alice]: My count is: 4<br>
> INFO:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [Alice]: My count is: 5

<br>

## ⚒️ Tech stack ⚒️

OS:

- Windows `10`

Dependencies:

- [Python](https://www.python.org/) `3.11.8`
- [uAgents Python SDK](https://pypi.org/project/uagents/) `0.11.0`
