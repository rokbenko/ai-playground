# #8 Next.js graphical user interface for OpenAI assistants with response streaming using the OpenAI Assistants API `v2` beta

## Short description

Next.js GUI for the personal math tutor and customer support chatbot with response streaming. Both assistants were built in previous tutorials (see [#2 Build a personal math tutor](https://github.com/rokbenko/ai-playground/tree/main/openai-tutorials/2-Build_personal_math_tutor) and [#4 Build a customer support chatbot](https://github.com/rokbenko/ai-playground/tree/main/openai-tutorials/4-Build_customer_support_chatbot)). The personal math tutor is using the Code Interpreter tool, while the customer support chatbot is using the File Search tool.

> [!NOTE]
> The code in this tutorial works with the [OpenAI Assistants API `v2` beta](https://platform.openai.com/docs/api-reference/assistants).

<br>

## Installation

To start using the Next.js app, follow these steps:

1. Clone the repository: `git clone https://github.com/rokbenko/ai-playground.git`
2. Change the directory: `cd ai-playground/openai-tutorials/8-GUI_Nextjs_assistants_streaming_Assistants_API_v2_beta`
3. Install the dependencies: `npm i`
4. Create an `.env` file to set up your environment variables
5. Run the development server: `npm run dev`
6. To view the app, navigate to [http://localhost:3000](http://localhost:3000)

> [!NOTE]
> Your `.env` file should contain the following three environment variables:
>
> ```bash
> OPENAI_CUSTOMER_SUPPORT_CHATBOT_ASSISTANT_ID=asst_xxxxx
> OPENAI_CUSTOMER_SUPPORT_CHATBOT_FILE_ID=file-xxxxx
> OPENAI_PERSONAL_MATH_TUTOR_ASSISTANT_ID=asst_xxxxx
> ```

<br>

## Environment

The app was tested and worked in the following environment:

- Windows `10`
- Node.js `21.2.0`

<br>

## Tech stack

| Technology              | Version    |
| ----------------------- | ---------- |
| OpenAI Node.js SDK      | `4.47.1`   |
| Next.js                 | `14.2.3`   |
| React                   | `^18`      |
| TypeScript              | `^5`       |
| ESLint                  | `^8`       |
| Material UI for Next.js | `^5.15.11` |
| SASS                    | `^1.77.2`  |
| Tailwind CSS            | `^3.4.1`   |
| React icons             | `^5.2.1`   |
| Dotenv                  | `16.4.5`   |

<br>

## Screenshot

Coming soon... ✨
