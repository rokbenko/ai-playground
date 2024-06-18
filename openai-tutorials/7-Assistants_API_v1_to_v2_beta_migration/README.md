# #7 Assistants API `v1` to `v2` beta migration

## Short description

Examples on how to migrate the OpenAI Assistants API `v1` to `v2` beta:

- Python TUI for the File Search tool (see [`tui_customer_support_chatbot_v2_beta.py`](https://github.com/rokbenko/ai-playground/tree/main/openai-tutorials/7-Assistants_API_v1_to_v2_beta_migration/TUI/tui_customer_support_chatbot_v2_beta.py))
- Node.js TUI for the File Search tool (see [`tui_customer_support_chatbot_v2_beta.js`](https://github.com/rokbenko/ai-playground/tree/main/openai-tutorials/7-Assistants_API_v1_to_v2_beta_migration/TUI/tui_customer_support_chatbot_v2_beta.js))
- Python TUI for the Code Interpreter tool (see [`tui_personal_math_tutor_v2_beta.py`](https://github.com/rokbenko/ai-playground/tree/main/openai-tutorials/7-Assistants_API_v1_to_v2_beta_migration/TUI/tui_personal_math_tutor_v2_beta.py))
- Node.js TUI for the Code Interpreter tool (see [`tui_personal_math_tutor_v2_beta.js`](https://github.com/rokbenko/ai-playground/tree/main/openai-tutorials/7-Assistants_API_v1_to_v2_beta_migration/TUI/tui_personal_math_tutor_v2_beta.js))
- Next.js GUI for the File Search tool and Code Interpreter tool (see [Next.js GUI](https://github.com/rokbenko/ai-playground/tree/main/openai-tutorials/7-Assistants_API_v1_to_v2_beta_migration/GUI/Next.js))
- Streamlit GUI for the File Search tool and Code Interpreter tool (see [Streamlit GUI](https://github.com/rokbenko/ai-playground/tree/main/openai-tutorials/7-Assistants_API_v1_to_v2_beta_migration/GUI/Streamlit))

> [!NOTE]
> For those unfamiliar with the terms "TUI" and "GUI":
>
> - TUI stands for _Text User Interface_
> - GUI stands for _Graphical User Interface_

<br>

## Python TUI working examples

### File Search tool

If you run [`tui_customer_support_chatbot_v2_beta.py`](https://github.com/rokbenko/ai-playground/tree/main/openai-tutorials/7-Assistants_API_v1_to_v2_beta_migration/TUI/tui_customer_support_chatbot_v2_beta.py), you should be able to chat with the customer support chatbot assistant:

> ai-playground\openai-tutorials\7-Assistants_API_v1_to_v2_beta_migration> python tui_customer_support_chatbot_v2_beta.py<br>
> <br>
> User: What can I buy in your online store?<br>
> <br>
> Assistant: In our online store, we currently sell books. We offer standard and expedited shipping options, and our standard warranty covers products for 1 week from the date of purchase. Additionally, we have a special offer available where you can use the DISCOUNT20 coupon to get a 20% discount on your purchase. If you have any further questions or need assistance, you can contact our customer support through the chatbot. Feel free browse our selection and take advantage of the discount offer!<br>
> <br>
> User: quit<br>
> <br>
> Assistant: Have a nice day! 👋<br>
> <br>
> ai-playground\openai-tutorials\7-Assistants_API_v1_to_v2_beta_migration>

### Code Interpreter tool

If you run [`tui_personal_math_tutor_v2_beta.py`](https://github.com/rokbenko/ai-playground/tree/main/openai-tutorials/7-Assistants_API_v1_to_v2_beta_migration/TUI/tui_personal_math_tutor_v2_beta.py), you should be able to chat with the personal math tutor assistant:

> ai-playground\openai-tutorials\7-Assistants_API_v1_to_v2_beta_migration> python tui_personal_math_tutor_v2_beta.py<br>
> <br>
> User: I need to solve the equation 3x + 11 = 14. Can you help me?<br>
> <br>
> Assistant: The solution to the equation 3x + 11 = 14 is x = 1.<br>
> <br>
> User: quit<br>
> <br>
> Assistant: Have a nice day! 👋<br>
> <br>
> ai-playground\openai-tutorials\7-Assistants_API_v1_to_v2_beta_migration>

Both Python examples were tested and worked in the following environment:

- Windows `10`
- Python `3.11.8`
- OpenAI Python SDK `1.26.0`

<br>

## Node.js TUI working examples

### File Search tool

If you run [`tui_customer_support_chatbot_v2_beta.js`](https://github.com/rokbenko/ai-playground/tree/main/openai-tutorials/7-Assistants_API_v1_to_v2_beta_migration/TUI/tui_customer_support_chatbot_v2_beta.js), you should be able to chat with the customer support chatbot assistant:

> ai-playground\openai-tutorials\7-Assistants_API_v1_to_v2_beta_migration> python tui_customer_support_chatbot_v2_beta.js<br>
> <br>
> User: What can I buy in your online store?<br>
> <br>
> Assistant: In our online store, we currently sell books. We offer standard and expedited shipping options, and our standard warranty covers products for 1 week from the date of purchase. Additionally, we have a special offer available where you can use the DISCOUNT20 coupon to get a 20% discount on your purchase. If you have any further questions or need assistance, you can contact our customer support through the chatbot. Feel free browse our selection and take advantage of the discount offer!<br>
> <br>
> User: quit<br>
> <br>
> Assistant: Have a nice day!<br>
> <br>
> ai-playground\openai-tutorials\7-Assistants_API_v1_to_v2_beta_migration>

### Code Interpreter tool

If you run [`tui_personal_math_tutor_v2_beta.js`](https://github.com/rokbenko/ai-playground/tree/main/openai-tutorials/7-Assistants_API_v1_to_v2_beta_migration/TUI/tui_personal_math_tutor_v2_beta.js), you should be able to chat with the personal math tutor assistant:

> ai-playground\openai-tutorials\7-Assistants_API_v1_to_v2_beta_migration> python tui_personal_math_tutor_v2_beta.js<br>
> <br>
> User: I need to solve the equation 3x + 11 = 14. Can you help me?<br>
> <br>
> Assistant: The solution to the equation 3x + 11 = 14 is x = 1.<br>
> <br>
> User: quit<br>
> <br>
> Assistant: Have a nice day!<br>
> <br>
> ai-playground\openai-tutorials\7-Assistants_API_v1_to_v2_beta_migration>

Both Node.js examples were tested and worked in the following environment:

- Windows `10`
- Node.js `21.2.0`
- OpenAI Node.js SDK `4.42.0`

<br>

## Next.js GUI example

### Short description

Next.js GUI for the File Search tool (i.e., customer support chatbot assistant) and Code Interpreter tool (i.e., personal math tutor assistant).

### Installation

To start using the Next.js GUI, follow these steps:

1. Clone the repository: `git clone https://github.com/rokbenko/ai-playground.git`
2. Change the directory: `cd ai-playground/openai-tutorials/7-Assistants_API_v1_to_v2_beta_migration/GUI/Next.js`
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

### Environment

The app was tested and worked in the following environment:

- Windows `10`
- Node.js `21.2.0`

### Tech stack

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

### Screenshot

![Screenshot](https://github.com/rokbenko/ai-playground/blob/main/openai-tutorials/7-Assistants_API_v1_to_v2_beta_migration/GUI/Next.js/screenshot.gif)

<br>

## Streamlit GUI example

### Short description

Streamlit GUI for the File Search tool (i.e., customer support chatbot assistant) and Code Interpreter tool (i.e., personal math tutor assistant).

### Installation

To start using the Streamlit GUI, follow these steps:

1. Clone the repository: `git clone https://github.com/rokbenko/ai-playground.git`
2. Change the directory: `cd ai-playground/openai-tutorials/7-Assistants_API_v1_to_v2_beta_migration/GUI/Streamlit`
3. Create a `.streamlit` folder and inside it create a `secrets.toml` file to set up your environment variables
4. Run the app: `streamlit run 1_Select_an_OpenAI_assistant_to_chat_with.py`
5. To view the app, navigate to [http://localhost:8501](http://localhost:8501)

> [!NOTE]
> Your `secrets.toml` file should contain the following four environment variables:
>
> ```bash
> OPENAI_API_KEY="sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
> OPENAI_CUSTOMER_SUPPORT_CHATBOT_ASSISTANT_ID="asst_xxxxx"
> OPENAI_CUSTOMER_SUPPORT_CHATBOT_FILE_ID="file-xxxxx"
> OPENAI_PERSONAL_MATH_TUTOR_ASSISTANT_ID="asst_xxxxx"
> ```

### Environment

The app was tested and worked in the following environment:

- Windows `10`
- Python `3.11.8`

### Tech stack

| Technology              | Version    |
| ----------------------- | ---------- |
| OpenAI Python SDK       | `1.34.0`   |
| Streamlit               | `1.35.0`   |

### Screenshot

Coming soon... ✨
