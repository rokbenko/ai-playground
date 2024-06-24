# #1 Python and Node.js TUIs for LangGraph agent with a web connection

<br>

## 📖 Description 📖

Python and Node.js TUIs for a LangGraph agent using the [Tavily](https://tavily.com/) tool to get a web connection and an OpenAI LLM.

<br>

## 🚀 Installation 🚀

Before running [`tui_langgraph_agent_tavily.py`](https://github.com/rokbenko/ai-playground/blob/main/langchain-tutorials/1-TUI_LangGraph_agent_Tavily/tui_langgraph_agent_tavily.py) or [`tui_langgraph_agent_tavily.js`](https://github.com/rokbenko/ai-playground/blob/main/langchain-tutorials/1-TUI_LangGraph_agent_Tavily/tui_langgraph_agent_tavily.js), follow these steps to create a virtual environment and install dependencies:

> [!NOTE]
> The following instructions are specific to Windows. For macOS or Linux, please use the corresponding commands for your operating system. See the official [`venv` documentation](https://docs.python.org/3/library/venv.html) for more information.

1. Clone the repository: `git clone https://github.com/rokbenko/ai-playground.git`
2. Change the directory: `cd ai-playground/langchain-tutorials/1-TUI_LangGraph_agent_Tavily`
3. Create an `.env` file to set up your environment variables

> [!IMPORTANT]
> Your `.env` file should contain the following environment variables:
>
> ```
> OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxx
> TAVILY_API_KEY=tvly-xxxxxxxxxxxxxxxxxxxxxxxxx
> ```

4. Set up a virtual environment

> [!NOTE]
> `venv` is a built-in Python module that allows you to create and manage virtual environments. If you have Python `v3.3` or higher installed, you can start using `venv` right away.

**Python**

4.1 Create a virtual environment named `my-venv`:

```
python -m venv my-venv
```

> [!TIP]
> After creating the virtual environment, you should see a folder named `my-venv` inside the `1-TUI_LangGraph_agent_Tavily` folder.

4.2 Activate the virtual environment `my-venv`:

```
my-venv\Scripts\activate
```

> [!TIP]
> You can verify that the virtual environment is activated successfully if you see `(my-venv)` at the beginning of your terminal prompt, like this:
> 
> ```
> (my-venv) C:\your\path\to\ai-playground\langchain-tutorials\1-TUI_LangGraph_agent_Tavily
> ```

5. Install dependencies using the [`requirements.txt`](https://github.com/rokbenko/ai-playground/blob/main/langchain-tutorials/1-TUI_LangGraph_agent_Tavily/requirements.txt) file

**Python**

```
python -m pip install -r requirements.txt
```

6. Run and use [`tui_langgraph_agent_tavily.py`](https://github.com/rokbenko/ai-playground/blob/main/langchain-tutorials/1-TUI_LangGraph_agent_Tavily/tui_langgraph_agent_tavily.py) or [`tui_langgraph_agent_tavily.js`](https://github.com/rokbenko/ai-playground/blob/main/langchain-tutorials/1-TUI_LangGraph_agent_Tavily/tui_langgraph_agent_tavily.js)

7. Deactivate the virtual environment `my-venv` after you are finished

**Python**

```
deactivate
```

> [!TIP]
> You can verify that the virtual environment is deactivated successfully if you *don't* see `(my-venv)` anymore at the beginning of your terminal prompt, like this:
>
> ```
> C:\your\path\to\ai-playground\langchain-tutorials\1-TUI_LangGraph_agent_Tavily
> ```

<br>

## 🔥 Working example in Python 🔥

If you run [`tui_langgraph_agent_tavily.py`](https://github.com/rokbenko/ai-playground/blob/main/langchain-tutorials/1-TUI_LangGraph_agent_Tavily/tui_langgraph_agent_tavily.py), you should be able to chat with the agent in a terminal:

> User:<br>
> Hi, I'm Bob.
> <br><br>
> Agent:<br>
> Hello Bob! How can I assist you today?
> <br><br>
> User:<br>
> What's the current weather in San Francisco? Give me exact data, like temperature, condition, wind, etc.
> <br><br>
> The agent is calling the tool 'tavily_search_results_json' with the query 'current weather in San Francisco'.<br>
> Wait for the answer.
> <br><br>
> Agent:<br>
> The current weather in San Francisco is as follows:<br>
>
> - Temperature: 15.6°C (60.1°F)<br>
> - Condition: Sunny<br>
> - Wind: 6.9 mph, coming from NNW direction<br>
> - Pressure: 1013.0 mb<br>
> - Humidity: 83%<br>
> - Visibility: 16.0km (9.0 miles)<br>
> - UV Index: 4.0<br>
> - Cloud Cover: 0%<br>
> - Feels Like: 15.6°C (60.1°F)<br>
> - Wind Chill: 12.3°C (54.1°F)<br>
> - Heat Index: 13.0°C (55.4°F)<br>
> - Dewpoint: 9.1°C (48.3°F)<br>
> - Gust: 8.2 mph
> <br>
> For more details, you can visit [WeatherAPI.com](https://www.weatherapi.com/)
> <br><br>
> User:<br>
> Quit
> <br><br>
> Agent:<br>
> Have a nice day! 👋

### ⚒️ Tech stack ⚒️

OS:

- Windows `10`

Dependencies:

- [Python](https://www.python.org/) `3.11.8`
- [LangChain Python SDK](https://pypi.org/project/langchain/) `0.2.5`
- [LangChain Core Python SDK](https://pypi.org/project/langchain-core/) `0.2.9`
- [LangChain Community Python SDK](https://pypi.org/project/langchain-community/) `0.2.5`
- [LangChain OpenAI Python SDK](https://pypi.org/project/langchain-openai/) `0.1.9`
- [LangGraph Python SDK](https://pypi.org/project/langgraph/) `0.1.1`
- [Rich](https://pypi.org/project/rich/) `13.7.1`

<br>

## 🔥 Working example in Node.js 🔥

If you run [`tui_langgraph_agent_tavily.js`](https://github.com/rokbenko/ai-playground/blob/main/langchain-tutorials/1-TUI_LangGraph_agent_Tavily/tui_langgraph_agent_tavily.js), you should be able to chat with the agent in a terminal:

> User:<br>
> Hi, I'm Bob.
> <br><br>
> Agent:<br>
> Hello Bob! How can I assist you today?
> <br><br>
> User:<br>
> What's the current weather in San Francisco? Give me exact data, like temperature, condition, wind, etc.
> <br><br>
> The agent is calling the tool 'tavily_search_results_json' with the query 'current weather in San Francisco'.<br>
> Wait for the answer.
> <br><br>
> Agent:<br>
> The current weather in San Francisco is as follows:<br>
>
> - Temperature: 15.6°C (60.1°F)<br>
> - Condition: Sunny<br>
> - Wind: 6.9 mph, coming from NNW direction<br>
> - Pressure: 1013.0 mb<br>
> - Humidity: 83%<br>
> - Visibility: 16.0km (9.0 miles)<br>
> - UV Index: 4.0<br>
> - Cloud Cover: 0%<br>
> - Feels Like: 15.6°C (60.1°F)<br>
> - Wind Chill: 12.3°C (54.1°F)<br>
> - Heat Index: 13.0°C (55.4°F)<br>
> - Dewpoint: 9.1°C (48.3°F)<br>
> - Gust: 8.2 mph
> <br>
> For more details, you can visit [WeatherAPI.com](https://www.weatherapi.com/)
> <br><br>
> User:<br>
> Quit
> <br><br>
> Agent:<br>
> Have a nice day!

### ⚒️ Tech stack ⚒️

OS:

- Windows `10`

Dependencies:

Coming soon... ✨

<br>

## 📽️ Demonstration 📽️

Coming soon... ✨
