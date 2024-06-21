# #7 Python and Node.js TUIs for assistants with response streaming using the OpenAI Assistants API `v2` beta

<br>

## 📖 Description 📖

Python and Node.js TUIs for the personal math tutor and customer support chatbot with response streaming. Both assistants were built in previous tutorials (see [#2 Build a personal math tutor](https://github.com/rokbenko/ai-playground/tree/main/openai-tutorials/2-Build_personal_math_tutor) and [#4 Build a customer support chatbot](https://github.com/rokbenko/ai-playground/tree/main/openai-tutorials/4-Build_customer_support_chatbot)). The personal math tutor is using the Code Interpreter tool, while the customer support chatbot is using the File Search tool.

There are four examples:

- Python TUI for the Code Interpreter tool (see [`tui_personal_math_tutor_v2_beta.py`](https://github.com/rokbenko/ai-playground/blob/main/openai-tutorials/7-TUI_assistants_streaming_Assistants_API_v2_beta/tui_personal_math_tutor_v2_beta.py)),
- Node.js TUI for the Code Interpreter tool (see [`tui_personal_math_tutor_v2_beta.js`](https://github.com/rokbenko/ai-playground/blob/main/openai-tutorials/7-TUI_assistants_streaming_Assistants_API_v2_beta/tui_personal_math_tutor_v2_beta.js)),
- Python TUI for the File Search tool (see [`tui_customer_support_chatbot_v2_beta.py`](https://github.com/rokbenko/ai-playground/blob/main/openai-tutorials/7-TUI_assistants_streaming_Assistants_API_v2_beta/tui_customer_support_chatbot_v2_beta.py)), and
- Node.js TUI for the File Search tool (see [`tui_customer_support_chatbot_v2_beta.js`](https://github.com/rokbenko/ai-playground/blob/main/openai-tutorials/7-TUI_assistants_streaming_Assistants_API_v2_beta/tui_customer_support_chatbot_v2_beta.js)).

> [!IMPORTANT]
> Before you run any scripts, create an `.env` file to set up your environment variables.
>
> Your `.env` file should contain the following environment variables:
>
> ```bash
> OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxx
> OPENAI_CUSTOMER_SUPPORT_CHATBOT_ASSISTANT_ID=asst_xxxxxxxxxxxxxxxxxxxxxxxxx
> OPENAI_CUSTOMER_SUPPORT_CHATBOT_FILE_ID=file-xxxxxxxxxxxxxxxxxxxxxxxxx
> OPENAI_PERSONAL_MATH_TUTOR_ASSISTANT_ID=asst_xxxxxxxxxxxxxxxxxxxxxxxxx
> ```

> [!NOTE]
> The code in this tutorial works with the [OpenAI Assistants API `v2` beta](https://platform.openai.com/docs/api-reference/assistants).

<br>

## 🔥 Working examples in Python 🔥

### Code Interpreter tool example

If you run [`tui_personal_math_tutor_v2_beta.py`](https://github.com/rokbenko/ai-playground/blob/main/openai-tutorials/7-TUI_assistants_streaming_Assistants_API_v2_beta/tui_personal_math_tutor_v2_beta.py), you should be able to chat with the personal math tutor in a terminal and receive its responses in a **streaming(!)** way:

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

### ⚒️ Tech stack ⚒️

OS:

- Windows `10`

Dependencies:

- [Python](https://www.python.org/) `3.11.8`
- [OpenAI Python API SDK](https://pypi.org/project/openai/) `1.34.0`
- [Rich](https://pypi.org/project/rich/) `13.7.0`
- [Dotenv](https://pypi.org/project/python-dotenv/) `1.0.1`

### File Search tool example

If you run [`tui_customer_support_chatbot_v2_beta.py`](https://github.com/rokbenko/ai-playground/blob/main/openai-tutorials/7-TUI_assistants_streaming_Assistants_API_v2_beta/tui_customer_support_chatbot_v2_beta.py), you should be able to chat with the customer support chatbot in a terminal and receive its responses in a **streaming(!)** way:

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

### ⚒️ Tech stack ⚒️

OS:

- Windows `10`

Dependencies:

- [Python](https://www.python.org/) `3.11.8`
- [OpenAI Python API SDK](https://pypi.org/project/openai/) `1.34.0`
- [Rich](https://pypi.org/project/rich/) `13.7.0`
- [Dotenv](https://pypi.org/project/python-dotenv/) `1.0.1`

<br>

## 🔥 Working examples in Node.js 🔥

### Code Interpreter tool example

If you run [`tui_personal_math_tutor_v2_beta.js`](https://github.com/rokbenko/ai-playground/blob/main/openai-tutorials/7-TUI_assistants_streaming_Assistants_API_v2_beta/tui_personal_math_tutor_v2_beta.js), you should be able to chat with the personal math tutor in a terminal and receive its responses in a **streaming(!)** way:

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

### ⚒️ Tech stack ⚒️

OS:

- Windows `10`

Dependencies:

- [Node.js](https://nodejs.org/en) `21.2.0`
- [OpenAI Node.js API SDK](https://www.npmjs.com/package/openai) `4.47.1`
- [Terminal Kit](https://www.npmjs.com/package/terminal-kit) `3.0.1`
- [Dotenv](https://www.npmjs.com/package/dotenv) `16.4.3`

### File Search tool example

If you run [`tui_customer_support_chatbot_v2_beta.js`](https://github.com/rokbenko/ai-playground/blob/main/openai-tutorials/7-TUI_assistants_streaming_Assistants_API_v2_beta/tui_customer_support_chatbot_v2_beta.js), you should be able to chat with the customer support chatbot in a terminal and receive its responses in a **streaming(!)** way:

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

### ⚒️ Tech stack ⚒️

OS:

- Windows `10`

Dependencies:

- [Node.js](https://nodejs.org/en) `21.2.0`
- [OpenAI Node.js API SDK](https://www.npmjs.com/package/openai) `4.47.1`
- [Terminal Kit](https://www.npmjs.com/package/terminal-kit) `3.0.1`
- [Dotenv](https://www.npmjs.com/package/dotenv) `16.4.3`

<br>

## 📽️ Demonstration 📽️

Python Code Interpreter tool example:

Coming soon... ✨

Python File Search tool example:

Coming soon... ✨

Node.js Code Interpreter tool example:

Coming soon... ✨

Node.js File Search tool example:

Coming soon... ✨
