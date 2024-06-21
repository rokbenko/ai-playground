# #2 Build a personal math tutor

<br>

## 📖 Description 📖

Python and Node.js examples on how to build a personal math tutor with the OpenAI Assistants API `v1` beta using the Code Interpreter tool.

> [!NOTE]
> The code in this tutorial works with the [OpenAI Assistants API `v1` beta](https://platform.openai.com/docs/api-reference/assistants-v1). In April 2024, the [OpenAI Assistants API `v2` beta](https://platform.openai.com/docs/api-reference/assistants) was released. See the [migration guide](https://platform.openai.com/docs/assistants/migration/agents).

<br>

## 🔥 Working example in Python 🔥

If you run `personal_math_tutor.py`, you should get the following response:

> This is the assistant object: Assistant(xxxxx)
>
> This is the thread object: Thread(xxxxx)
>
> This is the message object: ThreadMessage(xxxxx)
>
> This is the run object: Run(xxxxx)
>
> Run status: in_progress <br>
> Run status: in_progress <br>
> Run status: in_progress <br>
> Run status: in_progress <br>
> Run status: in_progress <br>
> Run status: in_progress <br>
> Run status: in_progress <br>
> Run status: in_progress <br>
> Run status: in_progress <br>
> Run status: in_progress <br>
> Run status: in_progress <br>
> Run status: in_progress <br>
> Run status: in_progress <br>
> Run status: in_progress <br>
> Run status: in_progress <br>
> Run status: in_progress <br>
> Run status: in_progress <br>
> Run status: in_progress <br>
> Run status: in_progress <br>
> Run status: in_progress <br>
> Run status: in_progress <br>
> Run status: in_progress <br>
> Run status: in_progress <br>
> Run status: in_progress <br>
> Run status: in_progress <br>
> Run status: in_progress <br>
> Run status: in_progress <br>
> Run status: in_progress <br>
> Run status: in_progress <br>
> Run status: in_progress <br>
> Run status: in_progress <br>
> Run status: in_progress <br>
> Run status: in_progress <br>
> Run status: in_progress <br>
> Run status: in_progress <br>
> Run status: in_progress <br>
> Run status: in_progress <br>
> Run status: in_progress <br>
> Run status: completed
>
> \------------------------------------------------------------
>
> User: I need to solve the equation `3x + 11 = 14`. Can you help me? <br>
> Assistant: The solution to the equation `3x + 11 = 14` is `x = 1`, Rok Benko.

### ⚒️ Tech stack ⚒️

OS:

- Windows `10`

Dependencies:

- [Python](https://www.python.org/) `3.10.1`
- [OpenAI Python API SDK](https://pypi.org/project/openai/) `1.1.1`

<br>

## 🔥 Working example in Node.js 🔥

If you run `personal_math_tutor.js`, you should get the following response:

> This is the assistant object: {xxxxx}
>
> This is the thread object: {xxxxx}
>
> This is the message object: {xxxxx}
>
> This is the run object: {xxxxx}
>
> Run status: in_progress <br>
> Run status: in_progress <br>
> Run status: in_progress <br>
> Run status: in_progress <br>
> Run status: in_progress <br>
> Run status: in_progress <br>
> Run status: in_progress <br>
> Run status: in_progress <br>
> Run status: in_progress <br>
> Run status: in_progress <br>
> Run status: in_progress <br>
> Run status: in_progress <br>
> Run status: in_progress <br>
> Run status: in_progress <br>
> Run status: in_progress <br>
> Run status: in_progress <br>
> Run status: in_progress <br>
> Run status: in_progress <br>
> Run status: in_progress <br>
> Run status: in_progress <br>
> Run status: in_progress <br>
> Run status: in_progress <br>
> Run status: in_progress <br>
> Run status: in_progress <br>
> Run status: in_progress <br>
> Run status: in_progress <br>
> Run status: in_progress <br>
> Run status: in_progress <br>
> Run status: in_progress <br>
> Run status: in_progress <br>
> Run status: in_progress <br>
> Run status: in_progress <br>
> Run status: in_progress <br>
> Run status: in_progress <br>
> Run status: in_progress <br>
> Run status: in_progress <br>
> Run status: in_progress <br>
> Run status: in_progress <br>
> Run status: in_progress <br>
> Run status: in_progress <br>
> Run status: in_progress <br>
> Run status: in_progress <br>
> Run status: in_progress <br>
> Run status: in_progress <br>
> Run status: in_progress <br>
> Run status: in_progress <br>
> Run status: in_progress <br>
> Run status: in_progress <br>
> Run status: in_progress <br>
> Run status: in_progress <br>
> Run status: in_progress <br>
> Run status: in_progress <br>
> Run status: in_progress <br>
> Run status: in_progress <br>
> Run status: in_progress <br>
> Run status: in_progress <br>
> Run status: in_progress <br>
> Run status: in_progress <br>
> Run status: in_progress <br>
> Run status: in_progress <br>
> Run status: completed
>
> Run status: completed
>
> \------------------------------------------------------------
>
> User: I need to solve the equation `3x + 11 = 14`. Can you help me? <br>
> Assistant: Sure, Rok Benko. To solve the equation for `x`, you need to isolate `x` on one side of the equation. Here is how to do it:
>
> 1. Subtract 11 from both sides of the equation: `3x + 11 - 11 = 14 - 11`, which simplifies to `3x = 3`
> 2. Then divide both sides by 3: `(3x) / 3 = 3 / 3`, which simplifies to `x = 1`
>
> So, the solution to your equation `3x + 11 = 14` is `x = 1`.

### ⚒️ Tech stack ⚒️

OS:

- Windows `10`

Dependencies:

- [Node.js](https://nodejs.org/en) `20.9.0`
- [OpenAI Node.js API SDK](https://www.npmjs.com/package/openai) `4.17.0`
