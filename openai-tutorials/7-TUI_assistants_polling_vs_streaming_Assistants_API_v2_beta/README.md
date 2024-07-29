# #7 Python and Node.js TUIs for assistants: response polling vs. streaming

<br>

## 📖 Description 📖

Python and Node.js TUIs for assistants to show the difference between response polling (manual or with helpers) and streaming (with helpers).

This directory has the following structure:

```
│   README.md
│
├───polling
│   ├───helpers
│   │       .env
│   │       .gitignore
│   │       tui_assistants_polling_helper.js
│   │       tui_assistants_polling_helper.py
│   │
│   └───manual
│           .env
│           .gitignore
│           tui_assistants_polling_manual.js
│           tui_assistants_polling_manual.py
│
└───streaming
        .env
        .gitignore
        tui_assistants_streaming_helper.js
        tui_assistants_streaming_helper.py
```

> [!NOTE]
> The code in this directory works with the [OpenAI Assistants API `v2` beta](https://platform.openai.com/docs/api-reference/assistants).

<br>

## 🧠 Learning goals 🧠

1. **Understanding assistant response handling:** We'll cover the difference between response polling and streaming in the OpenAI Assistants API. Response polling involves periodically checking for the availability of a response after a request is made. On the other hand, response streaming allows response to be transmitted in real-time as it becomes available after a request is made, providing a better UX.
3. **Implementing response polling and streaming:** We'll show how response polling and streaming can be implemented manually or using SDK helpers. For response polling, in Python, the `create_and_poll` method is an SDK helper that allows us to poll a response after a request is made, while in Node.js, the `createAndPoll` method is an SDK helper that provides the same functionality. For response streaming, both Python and Node.js offer the `stream` method as an SDK helper, that allows us to stream a response after a request is made.

<br>

## 🚀 Installation 🚀

Before running any of the Python or Node.js scripts, follow the instructions below.

1. Clone the repository: `git clone https://github.com/rokbenko/ai-playground.git`
2. Change the directory: *See the note below. It depends on which Python or Node.js script you want to run.*
3. Run any of the Python or Node.js scripts.

> [!IMPORTANT]
> Before you run any of the Python or Node.js scripts, create an `.env` file to set up your environment variables.
>
> Your `.env` file should contain at least the following environment variables:
>
> ```
> OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxx
> OPENAI_ASSISTANT_ID=asst_xxxxxxxxxxxxxxxxxxxxxxxxx
> ```
>
> If you want to attach a file to your assistant, your `.env` file must also contain the file ID as an environment variable, starting with *OPENAI_FILE_ID_*:
>
> ```
> OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxx
> OPENAI_ASSISTANT_ID=asst_xxxxxxxxxxxxxxxxxxxxxxxxx
> OPENAI_FILE_ID_1=file-xxxxxxxxxxxxxxxxxxxxxxxxx
> ```
>
> If you want to attach multiple files to your assistant, your `.env` file must also contain multiple file IDs as environment variables, all starting with *OPENAI_FILE_ID_* and followed by distinct identifiers:
>
> ```
> OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxx
> OPENAI_ASSISTANT_ID=asst_xxxxxxxxxxxxxxxxxxxxxxxxx
> OPENAI_FILE_ID_1=file-xxxxxxxxxxxxxxxxxxxxxxxxx
> OPENAI_FILE_ID_2=file-xxxxxxxxxxxxxxxxxxxxxxxxx
> OPENAI_FILE_ID_3=file-xxxxxxxxxxxxxxxxxxxxxxxxx
> ```
>
> Ensure that each file ID environment variable has a unique identifier following *OPENAI_FILE_ID_*. Do not use the same identifier for multiple file IDs (e.g., avoid using `OPENAI_FILE_ID_1` and `OPENAI_FILE_ID_1`). The suffixes (e.g., `1`, `2`, `3`) can be letters or numbers, as long as each is distinct.

> [!NOTE]
>  - If you want to run the Python or Node.js script on manual response polling, change the directory as follows: `cd ai-playground/openai-tutorials/7-TUI_assistants_polling_vs_streaming_Assistants_API_v2_beta/polling/manual`
>  - If you want to run the Python or Node.js script on response polling with helpers, change the directory as follows: `cd ai-playground/openai-tutorials/7-TUI_assistants_polling_vs_streaming_Assistants_API_v2_beta/polling/helpers`
>  - If you want to run the Python or Node.js script on response streaming with helpers, change the directory as follows: `cd ai-playground/openai-tutorials/7-TUI_assistants_polling_vs_streaming_Assistants_API_v2_beta/streaming`

<br>

## 🔥 Working examples in Python 🔥

- **Manual response polling:** If you run [`tui_assistants_polling_manual.py`](https://github.com/rokbenko/ai-playground/blob/main/openai-tutorials/7-TUI_assistants_polling_vs_streaming_Assistants_API_v2_beta/polling/manual/tui_assistants_polling_manual.py), you should be able to chat with an assistant and the assistant's answers should display in a polling manner.
- **Response polling with helpers:** If you run [`tui_assistants_polling_helper.py`](https://github.com/rokbenko/ai-playground/blob/main/openai-tutorials/7-TUI_assistants_polling_vs_streaming_Assistants_API_v2_beta/polling/helpers/tui_assistants_polling_helper.py), you should be able to chat with an assistant and the assistant's answers should display in a polling manner.
- **Response streaming with helpers:** Coming soon... ✨

### ⚒️ Tech stack ⚒️

OS:

- Windows `10`

Dependencies:

- [Python](https://www.python.org/) `3.11.8`
- [OpenAI Python API SDK](https://pypi.org/project/openai/) `1.37.0`
- [Rich](https://pypi.org/project/rich/) `13.7.1`
- [Dotenv](https://pypi.org/project/python-dotenv/) `1.0.1`

<br>

## 🔥 Working examples in Node.js 🔥

- **Manual response polling:** If you run [`tui_assistants_polling_manual.js`](https://github.com/rokbenko/ai-playground/blob/main/openai-tutorials/7-TUI_assistants_polling_vs_streaming_Assistants_API_v2_beta/polling/manual/tui_assistants_polling_manual.js), you should be able to chat with an assistant and the assistant's answers should display in a polling manner.
- **Response polling with helpers:** If you run [`tui_assistants_polling_helper.js`](https://github.com/rokbenko/ai-playground/blob/main/openai-tutorials/7-TUI_assistants_polling_vs_streaming_Assistants_API_v2_beta/polling/helpers/tui_assistants_polling_helper.js), you should be able to chat with an assistant and the assistant's answers should display in a polling manner.
- **Response streaming with helpers:** Coming soon... ✨

### ⚒️ Tech stack ⚒️

OS:

- Windows `10`

Dependencies:

- [Node.js](https://nodejs.org/en) `21.2.0`
- [OpenAI Node.js API SDK](https://www.npmjs.com/package/openai) `4.53.0`
- [Terminal Kit](https://www.npmjs.com/package/terminal-kit) `3.1.1`
- [Dotenv](https://www.npmjs.com/package/dotenv) `16.4.5`

<br>

## 📽️ Demonstration 📽️

Python response polling example:

Coming soon... ✨

Python response streaming example:

Coming soon... ✨

<br>

Node.js response polling example:

Coming soon... ✨

Node.js response streaming example:

Coming soon... ✨
