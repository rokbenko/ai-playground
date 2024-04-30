# #2 uAgents communication

## Short description

Python examples on how to make agents communicate with each other locally or remotely using Almanac contracts.

<br>

## Working examples in Python

### Local communication

If you run `alice_and_bob.py`, you should get the following response:

> INFO:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [bureau]: Starting server on http://0.0.0.0:8000 (Press CTRL+C to quit)<br>
> INFO:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [Alice]: I've received a message from agent1q0y5kq3h2s904zkrjtx7wz3z2mgj3j6k5w9tqs5wtpm0hryc6me0sg9gkuh: 'Hello, Alice! I'm agent Bob.'<br>
> INFO:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [&nbsp;&nbsp; Bob]: I've received a message from agent1q2x0um5u8achgq24drv5krwqm6xdz5dewyw6k0nlp0h4un350gwyz8vps4y: 'Hello, Bob! I'm agent Alice.'<br>
> INFO:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [Alice]: I've received a message from agent1q0y5kq3h2s904zkrjtx7wz3z2mgj3j6k5w9tqs5wtpm0hryc6me0sg9gkuh: 'Hello, Alice! I'm agent Bob.'<br>
> INFO:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [&nbsp;&nbsp; Bob]: I've received a message from agent1q2x0um5u8achgq24drv5krwqm6xdz5dewyw6k0nlp0h4un350gwyz8vps4y: 'Hello, Bob! I'm agent Alice.'<br>
> INFO:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [Alice]: I've received a message from agent1q0y5kq3h2s904zkrjtx7wz3z2mgj3j6k5w9tqs5wtpm0hryc6me0sg9gkuh: 'Hello, Alice! I'm agent Bob.'<br>
> INFO:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [&nbsp;&nbsp; Bob]: I've received a message from agent1q2x0um5u8achgq24drv5krwqm6xdz5dewyw6k0nlp0h4un350gwyz8vps4y: 'Hello, Bob! I'm agent Alice.'<br>
> INFO:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [Alice]: I've received a message from agent1q0y5kq3h2s904zkrjtx7wz3z2mgj3j6k5w9tqs5wtpm0hryc6me0sg9gkuh: 'Hello, Alice! I'm agent Bob.'<br>
> INFO:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [&nbsp;&nbsp; Bob]: I've received a message from agent1q2x0um5u8achgq24drv5krwqm6xdz5dewyw6k0nlp0h4un350gwyz8vps4y: 'Hello, Bob! I'm agent Alice.'

<br>

### Remote communication

#### Step 1: Run Alice

If you run `alice.py`, you should get the following response:

> INFO:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [Alice]: Registering on almanac contract...<br>
> INFO:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [Alice]: Registering on almanac contract...complete<br>
> INFO:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [Alice]: Starting server on http://0.0.0.0:8000 (Press CTRL+C to quit)<br>
> INFO:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [Alice]: I've received a message from agent1qwr3c63ayxz87xcvkhxw98qq2mc885r60gk4krfqsq4zhszmntar5j7nnpn: 'Hello, Alice! I'm agent Bob.'<br>
> INFO:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [Alice]: I've received a message from agent1qwr3c63ayxz87xcvkhxw98qq2mc885r60gk4krfqsq4zhszmntar5j7nnpn: 'Hello, Alice! I'm agent Bob.'<br>
> INFO:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [Alice]: I've received a message from agent1qwr3c63ayxz87xcvkhxw98qq2mc885r60gk4krfqsq4zhszmntar5j7nnpn: 'Hello, Alice! I'm agent Bob.'<br>
> INFO:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [Alice]: I've received a message from agent1qwr3c63ayxz87xcvkhxw98qq2mc885r60gk4krfqsq4zhszmntar5j7nnpn: 'Hello, Alice! I'm agent Bob.'<br>
> INFO:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [Alice]: I've received a message from agent1qwr3c63ayxz87xcvkhxw98qq2mc885r60gk4krfqsq4zhszmntar5j7nnpn: 'Hello, Alice! I'm agent Bob.'

#### Step 2: Run Bob

If you run `bob.py`, you should get the following response:

> INFO:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [&nbsp;&nbsp; Bob]: Registering on almanac contract...<br>
> INFO:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [&nbsp;&nbsp; Bob]: Registering on almanac contract...complete<br>
> INFO:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [&nbsp;&nbsp; Bob]: Starting server on http://0.0.0.0:8001 (Press CTRL+C to quit)<br>
> INFO:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [&nbsp;&nbsp; Bob]: I've received a message from agent1qtkp83xdzjn6pupps8jj309mu5km6h58cgcwzl3afw9frrnmqhk9kwrur80: 'Hello, Bob! I'm agent Alice.'<br>
> INFO:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [&nbsp;&nbsp; Bob]: I've received a message from agent1qtkp83xdzjn6pupps8jj309mu5km6h58cgcwzl3afw9frrnmqhk9kwrur80: 'Hello, Bob! I'm agent Alice.'<br>
> INFO:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [&nbsp;&nbsp; Bob]: I've received a message from agent1qtkp83xdzjn6pupps8jj309mu5km6h58cgcwzl3afw9frrnmqhk9kwrur80: 'Hello, Bob! I'm agent Alice.'<br>
> INFO:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [&nbsp;&nbsp; Bob]: I've received a message from agent1qtkp83xdzjn6pupps8jj309mu5km6h58cgcwzl3afw9frrnmqhk9kwrur80: 'Hello, Bob! I'm agent Alice.'<br>
> INFO:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [&nbsp;&nbsp; Bob]: I've received a message from agent1qtkp83xdzjn6pupps8jj309mu5km6h58cgcwzl3afw9frrnmqhk9kwrur80: 'Hello, Bob! I'm agent Alice.'

<br>

Environment:

- Windows `10`
- Python `3.11.8`
- uAgents Python SDK `0.11.0`
