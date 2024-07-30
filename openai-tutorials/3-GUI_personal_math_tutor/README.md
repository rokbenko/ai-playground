# #3 Next.js GUI for a personal math tutor

<br>

## 📖 Description 📖

Next.js GUI for the <a href="https://github.com/rokbenko/ai-playground/tree/main/openai-tutorials/2-Build_personal_math_tutor">#2 Build a personal math tutor</a> tutorial. The main focus is on advanced chat functionalities, with no attention given to non-relevant aspects. Therefore, the sidebar is completely removed.

> [!NOTE]
> The code in this directory works with the [OpenAI Assistants API `v1` beta](https://platform.openai.com/docs/api-reference/assistants-v1). In April 2024, the [OpenAI Assistants API `v2` beta](https://platform.openai.com/docs/api-reference/assistants) was released. See the [migration guide](https://platform.openai.com/docs/assistants/migration/agents).

<br>

## 🧠 Learning goal 🧠

- **Building a Next.js GUI for the OpenAI Assistants API `v1` beta:** We will build a user-friendly graphical user interface (i.e., GUI) using Next.js, designed to interact with the OpenAI Assistants API `v1` beta. This GUI will offer a ChatGPT-like experience, specifically tailored to chat with the personal math tutor built in the previous tutorial.

<br>

## 🚀 Installation 🚀

To start using the app, follow these steps:

1. Clone the repository: `git clone https://github.com/rokbenko/ai-playground.git`
2. Change the directory: `cd ai-playground/openai-tutorials/3-GUI_personal_math_tutor`
3. Install the dependencies: `npm i`
4. Create an `.env` file to set up your environment variables
5. Run the development server: `npm run dev`
6. To view the app, navigate to [http://localhost:3000](http://localhost:3000)

> [!IMPORTANT]
> Your `.env` file should contain the following environment variables:
>
> ```bash
> OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxx
> OPENAI_ASSISTANT_ID=asst_xxxxxxxxxxxxxxxxxxxxxxxxx
> OPENAI_THREAD_ID=thread_xxxxxxxxxxxxxxxxxxxxxxxxx
> ```

<br>

## ⚒️ Tech stack ⚒️

OS:

- Windows `10`

Dependencies:

- [OpenAI Node.js API SDK](https://www.npmjs.com/package/openai) `4.20.0`
- [Next.js](https://www.npmjs.com/package/next) `14.0.3`
- [React](https://www.npmjs.com/package/react) `18.2.0`
- [TypeScript](https://www.npmjs.com/package/typescript) `5.0.4`
- [Tailwind CSS](https://www.npmjs.com/package/tailwindcss) `3.3.1`
- [Material UI](https://www.npmjs.com/package/@mui/material) `5.14.18`
- [ESLint](https://www.npmjs.com/package/eslint) `8.38.0`
- [Dotenv](https://www.npmjs.com/package/dotenv) `16.3.1`

<br>

## 📽️ Demonstration 📽️

Get environment variables:

![Demonstration of how to get environment variables](https://github.com/rokbenko/ai-playground/blob/main/openai-tutorials/3-GUI_personal_math_tutor/demonstration_env.gif)

Chat with a personal math tutor:

![Demonstration of how to chat with a personal math tutor](https://github.com/rokbenko/ai-playground/blob/main/openai-tutorials/3-GUI_personal_math_tutor/demonstration_chat.gif)
