# #9 Streamlit graphical user interface for OpenAI assistants with response streaming using the OpenAI Assistants API `v2` beta

## Short description

Streamlit GUI for the personal math tutor and customer support chatbot with response streaming. Both assistants were built in previous tutorials (see [#2 Build a personal math tutor](https://github.com/rokbenko/ai-playground/tree/main/openai-tutorials/2-Build_personal_math_tutor) and [#4 Build a customer support chatbot](https://github.com/rokbenko/ai-playground/tree/main/openai-tutorials/4-Build_customer_support_chatbot)). The personal math tutor is using the Code Interpreter tool, while the customer support chatbot is using the File Search tool.

> [!NOTE]
> The code in this tutorial works with the [OpenAI Assistants API `v2` beta](https://platform.openai.com/docs/api-reference/assistants).

<br>

## Installation

To start using the app, follow these steps:

1. Clone the repository: `git clone https://github.com/rokbenko/ai-playground.git`
2. Change the directory: `cd ai-playground/openai-tutorials/9-GUI_Streamlit_assistants_streaming_Assistants_API_v2_beta`
3. Create a `.streamlit` folder and inside it create a `secrets.toml` file to set up your environment variables
4. Run the app: `streamlit run 1_Select_an_OpenAI_assistant_to_chat_with.py`
5. To view the app, navigate to [http://localhost:8501](http://localhost:8501)

> [!IMPORTANT]
> Your `secrets.toml` file should contain the following four environment variables:
>
> ```bash
> OPENAI_API_KEY="sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
> OPENAI_CUSTOMER_SUPPORT_CHATBOT_ASSISTANT_ID="asst_xxxxx"
> OPENAI_CUSTOMER_SUPPORT_CHATBOT_FILE_ID="file-xxxxx"
> OPENAI_PERSONAL_MATH_TUTOR_ASSISTANT_ID="asst_xxxxx"
> ```

<br>

## Environment

The app was tested and worked in the following environment:

- Windows `10`
- Python `3.11.8`

<br>

## Tech stack

| Technology        | Version  |
| ----------------- | -------- |
| OpenAI Python SDK | `1.34.0` |
| Streamlit         | `1.35.0` |

<br>

## Screenshot

Coming soon... ✨
