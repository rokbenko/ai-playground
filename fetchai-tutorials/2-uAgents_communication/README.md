# #2 uAgents communication

## 📖 Description 📖

Python examples on how to make Fetch.ai agents communicate with each other locally or remotely using Almanac contracts.

<br>

## 🧠 Learning goal 🧠

- **Understanding local and remote communication between Fetch.ai agents:** We will explore how Fetch.ai agents can communicate both locally and remotely. We will set up two agents, Alice and Bob, to greet each other in both scenarios. For local communication, Alice and Bob will exchange greetings within the same environment. Remote communication is achieved through [Almanac contracts](https://fetch.ai/docs/concepts/fetch-network/almanac), leveraging Fetch.ai's decentralized framework to enable agents to interact across different environments.

<br>

## 🔥 Working examples in Python 🔥

### Local communication

If you run [`alice_and_bob.py`](https://github.com/rokbenko/ai-playground/blob/main/fetchai-tutorials/2-uAgents_communication/alice_and_bob.py), you should get the following response:

> INFO:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [bureau]: Starting server on http://0.0.0.0:8000 (Press CTRL+C to quit)<br>
> INFO:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [Alice]: I've received a message from agent1q0y5kq3h2s904zkrjtx7wz3z2mgj3j6k5w9tqs5wtpm0hryc6me0sg9gkuh: 'Hello, Alice! I'm agent Bob.'<br>
> INFO:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [&nbsp;&nbsp; Bob]: I've received a message from agent1q2x0um5u8achgq24drv5krwqm6xdz5dewyw6k0nlp0h4un350gwyz8vps4y: 'Hello, Bob! I'm agent Alice.'<br>
> INFO:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [Alice]: I've received a message from agent1q0y5kq3h2s904zkrjtx7wz3z2mgj3j6k5w9tqs5wtpm0hryc6me0sg9gkuh: 'Hello, Alice! I'm agent Bob.'<br>
> INFO:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [&nbsp;&nbsp; Bob]: I've received a message from agent1q2x0um5u8achgq24drv5krwqm6xdz5dewyw6k0nlp0h4un350gwyz8vps4y: 'Hello, Bob! I'm agent Alice.'<br>
> INFO:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [Alice]: I've received a message from agent1q0y5kq3h2s904zkrjtx7wz3z2mgj3j6k5w9tqs5wtpm0hryc6me0sg9gkuh: 'Hello, Alice! I'm agent Bob.'<br>
> INFO:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [&nbsp;&nbsp; Bob]: I've received a message from agent1q2x0um5u8achgq24drv5krwqm6xdz5dewyw6k0nlp0h4un350gwyz8vps4y: 'Hello, Bob! I'm agent Alice.'<br>
> INFO:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [Alice]: I've received a message from agent1q0y5kq3h2s904zkrjtx7wz3z2mgj3j6k5w9tqs5wtpm0hryc6me0sg9gkuh: 'Hello, Alice! I'm agent Bob.'<br>
> INFO:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [&nbsp;&nbsp; Bob]: I've received a message from agent1q2x0um5u8achgq24drv5krwqm6xdz5dewyw6k0nlp0h4un350gwyz8vps4y: 'Hello, Bob! I'm agent Alice.'

### Remote communication

#### Step 1: Run Alice

If you run [`alice.py`](https://github.com/rokbenko/ai-playground/blob/main/fetchai-tutorials/2-uAgents_communication/alice.py), you should get the following response:

> INFO:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [Alice]: Registering on almanac contract...<br>
> INFO:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [Alice]: Registering on almanac contract...complete<br>
> INFO:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [Alice]: Starting server on http://0.0.0.0:8000 (Press CTRL+C to quit)<br>
> INFO:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [Alice]: I've received a message from agent1qwr3c63ayxz87xcvkhxw98qq2mc885r60gk4krfqsq4zhszmntar5j7nnpn: 'Hello, Alice! I'm agent Bob.'<br>
> INFO:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [Alice]: I've received a message from agent1qwr3c63ayxz87xcvkhxw98qq2mc885r60gk4krfqsq4zhszmntar5j7nnpn: 'Hello, Alice! I'm agent Bob.'<br>
> INFO:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [Alice]: I've received a message from agent1qwr3c63ayxz87xcvkhxw98qq2mc885r60gk4krfqsq4zhszmntar5j7nnpn: 'Hello, Alice! I'm agent Bob.'<br>
> INFO:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [Alice]: I've received a message from agent1qwr3c63ayxz87xcvkhxw98qq2mc885r60gk4krfqsq4zhszmntar5j7nnpn: 'Hello, Alice! I'm agent Bob.'<br>
> INFO:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [Alice]: I've received a message from agent1qwr3c63ayxz87xcvkhxw98qq2mc885r60gk4krfqsq4zhszmntar5j7nnpn: 'Hello, Alice! I'm agent Bob.'

#### Step 2: Run Bob

If you run [`bob.py`](https://github.com/rokbenko/ai-playground/blob/main/fetchai-tutorials/2-uAgents_communication/bob.py), you should get the following response:

> INFO:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [&nbsp;&nbsp; Bob]: Registering on almanac contract...<br>
> INFO:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [&nbsp;&nbsp; Bob]: Registering on almanac contract...complete<br>
> INFO:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [&nbsp;&nbsp; Bob]: Starting server on http://0.0.0.0:8001 (Press CTRL+C to quit)<br>
> INFO:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [&nbsp;&nbsp; Bob]: I've received a message from agent1qtkp83xdzjn6pupps8jj309mu5km6h58cgcwzl3afw9frrnmqhk9kwrur80: 'Hello, Bob! I'm agent Alice.'<br>
> INFO:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [&nbsp;&nbsp; Bob]: I've received a message from agent1qtkp83xdzjn6pupps8jj309mu5km6h58cgcwzl3afw9frrnmqhk9kwrur80: 'Hello, Bob! I'm agent Alice.'<br>
> INFO:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [&nbsp;&nbsp; Bob]: I've received a message from agent1qtkp83xdzjn6pupps8jj309mu5km6h58cgcwzl3afw9frrnmqhk9kwrur80: 'Hello, Bob! I'm agent Alice.'<br>
> INFO:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [&nbsp;&nbsp; Bob]: I've received a message from agent1qtkp83xdzjn6pupps8jj309mu5km6h58cgcwzl3afw9frrnmqhk9kwrur80: 'Hello, Bob! I'm agent Alice.'<br>
> INFO:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [&nbsp;&nbsp; Bob]: I've received a message from agent1qtkp83xdzjn6pupps8jj309mu5km6h58cgcwzl3afw9frrnmqhk9kwrur80: 'Hello, Bob! I'm agent Alice.'

<br>

## ⚒️ Tech stack ⚒️

OS:

- Windows `10`

Dependencies:

- [Python](https://www.python.org/) `3.11.8`
- [uAgents Python SDK](https://pypi.org/project/uagents/) `0.11.0`
