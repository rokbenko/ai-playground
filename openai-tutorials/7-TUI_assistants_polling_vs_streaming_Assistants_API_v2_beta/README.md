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
│   │       tui_assistants_polling_helpers.js
│   │       tui_assistants_polling_helpers.py
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
        tui_assistants_streaming.js
        tui_assistants_streaming.py
```

> [!NOTE]
> The code in this directory works with the [OpenAI Assistants API `v2` beta](https://platform.openai.com/docs/api-reference/assistants).

<br>

## 🚀 Installation 🚀

Coming soon... ✨

> [!IMPORTANT]
> Before you run any scripts, create an `.env` file to set up your environment variables.
>
> Your `.env` file should contain at least the following environment variables:
>
> ```
> OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxx
> OPENAI_ASSISTANT_ID=asst_xxxxxxxxxxxxxxxxxxxxxxxxx
> ```
>
> If you want to attach a file to your assistant, your `.env` file should also contain the file ID as an environment variable, starting with *OPENAI_FILE_ID_*:
>
> ```
> OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxx
> OPENAI_ASSISTANT_ID=asst_xxxxxxxxxxxxxxxxxxxxxxxxx
> OPENAI_FILE_ID_1=file-xxxxxxxxxxxxxxxxxxxxxxxxx
> ```
>
> If you want to attach multiple files to your assistant, your `.env` file should also contain file IDs as environment variables, all starting with *OPENAI_FILE_ID_*:
>
> ```
> OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxx
> OPENAI_ASSISTANT_ID=asst_xxxxxxxxxxxxxxxxxxxxxxxxx
> OPENAI_FILE_ID_1=file-xxxxxxxxxxxxxxxxxxxxxxxxx
> OPENAI_FILE_ID_2=file-xxxxxxxxxxxxxxxxxxxxxxxxx
> OPENAI_FILE_ID_3=file-xxxxxxxxxxxxxxxxxxxxxxxxx
> ```

<br>

## Response polling

### Manual

#### 🔥 Working example in Python 🔥

Coming soon... ✨

##### ⚒️ Tech stack ⚒️

OS:

- Windows `10`

Dependencies:

- [Python](https://www.python.org/) `3.11.8`
- [OpenAI Python API SDK](https://pypi.org/project/openai/) `1.35.4`
- [Rich](https://pypi.org/project/rich/) `13.7.1`
- [Dotenv](https://pypi.org/project/python-dotenv/) `1.0.1`

<br>

#### 🔥 Working example in Node.js 🔥

Coming soon... ✨

##### ⚒️ Tech stack ⚒️

OS:

- Windows `10`

Dependencies:

- [Node.js](https://nodejs.org/en) `21.2.0`
- [OpenAI Node.js API SDK](https://www.npmjs.com/package/openai) `4.52.1`
- [Terminal Kit](https://www.npmjs.com/package/terminal-kit) `3.1.1`
- [Dotenv](https://www.npmjs.com/package/dotenv) `16.4.5`

<br>

### With helpers

#### 🔥 Working example in Python 🔥

Coming soon... ✨

##### ⚒️ Tech stack ⚒️

OS:

- Windows `10`

Dependencies:

- [Python](https://www.python.org/) `3.11.8`
- [OpenAI Python API SDK](https://pypi.org/project/openai/) `1.35.4`
- [Rich](https://pypi.org/project/rich/) `13.7.1`
- [Dotenv](https://pypi.org/project/python-dotenv/) `1.0.1`

<br>

#### 🔥 Working example in Node.js 🔥

Coming soon... ✨

##### ⚒️ Tech stack ⚒️

OS:

- Windows `10`

Dependencies:

- [Node.js](https://nodejs.org/en) `21.2.0`
- [OpenAI Node.js API SDK](https://www.npmjs.com/package/openai) `4.52.1`
- [Terminal Kit](https://www.npmjs.com/package/terminal-kit) `3.1.1`
- [Dotenv](https://www.npmjs.com/package/dotenv) `16.4.5`

<br>

## Response streaming

### With helpers

#### 🔥 Working example in Python 🔥

Coming soon... ✨

##### ⚒️ Tech stack ⚒️

OS:

- Windows `10`

Dependencies:

- [Python](https://www.python.org/) `3.11.8`
- [OpenAI Python API SDK](https://pypi.org/project/openai/) `1.35.4`
- [Rich](https://pypi.org/project/rich/) `13.7.1`
- [Dotenv](https://pypi.org/project/python-dotenv/) `1.0.1`

<br>

#### 🔥 Working example in Node.js 🔥

Coming soon... ✨

##### ⚒️ Tech stack ⚒️

OS:

- Windows `10`

Dependencies:

- [Node.js](https://nodejs.org/en) `21.2.0`
- [OpenAI Node.js API SDK](https://www.npmjs.com/package/openai) `4.52.1`
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
