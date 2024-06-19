# #7 Terminal user interface for OpenAI assistants with response streaming using the OpenAI Assistants API `v2` beta

## Short description

Python and Node.js TUIs for the personal math tutor and customer support chatbot with response streaming. Both assistants were built in previous tutorials (see [#2 Build a personal math tutor](https://github.com/rokbenko/ai-playground/tree/main/openai-tutorials/2-Build_personal_math_tutor) and [#4 Build a customer support chatbot](https://github.com/rokbenko/ai-playground/tree/main/openai-tutorials/4-Build_customer_support_chatbot)). The personal math tutor is using the Code Interpreter tool, while the customer support chatbot is using the File Search tool.

There are four examples:

- Python TUI for the Code Interpreter tool (see [`tui_personal_math_tutor_v2_beta.py`](https://github.com/rokbenko/ai-playground/blob/main/openai-tutorials/7-TUI_assistants_streaming_Assistants_API_v2_beta/tui_personal_math_tutor_v2_beta.py))
- Node.js TUI for the Code Interpreter tool (see [`tui_personal_math_tutor_v2_beta.js`](https://github.com/rokbenko/ai-playground/blob/main/openai-tutorials/7-TUI_assistants_streaming_Assistants_API_v2_beta/tui_personal_math_tutor_v2_beta.js))
- Python TUI for the File Search tool (see [`tui_customer_support_chatbot_v2_beta.py`](https://github.com/rokbenko/ai-playground/blob/main/openai-tutorials/7-TUI_assistants_streaming_Assistants_API_v2_beta/tui_customer_support_chatbot_v2_beta.py))
- Node.js TUI for the File Search tool (see [`tui_customer_support_chatbot_v2_beta.js`](https://github.com/rokbenko/ai-playground/blob/main/openai-tutorials/7-TUI_assistants_streaming_Assistants_API_v2_beta/tui_customer_support_chatbot_v2_beta.js))

> [!IMPORTANT]
> Before you run any scripts, create an `.env` file to set up your environment variables. Your `.env` file should contain the following three environment variables:
>
> ```bash
> OPENAI_CUSTOMER_SUPPORT_CHATBOT_ASSISTANT_ID=asst_xxxxx
> OPENAI_CUSTOMER_SUPPORT_CHATBOT_FILE_ID=file-xxxxx
> OPENAI_PERSONAL_MATH_TUTOR_ASSISTANT_ID=asst_xxxxx
> ```

> [!NOTE]
> The code in this tutorial works with the [OpenAI Assistants API `v2` beta](https://platform.openai.com/docs/api-reference/assistants).

<br>

## Python TUI working examples

### Code Interpreter tool

If you run [`tui_personal_math_tutor_v2_beta.py`](https://github.com/rokbenko/ai-playground/blob/main/openai-tutorials/7-TUI_assistants_streaming_Assistants_API_v2_beta/tui_personal_math_tutor_v2_beta.py), you should be able to chat with the personal math tutor assistant:

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

### File Search tool

If you run [`tui_customer_support_chatbot_v2_beta.py`](https://github.com/rokbenko/ai-playground/blob/main/openai-tutorials/7-TUI_assistants_streaming_Assistants_API_v2_beta/tui_customer_support_chatbot_v2_beta.py), you should be able to chat with the customer support chatbot assistant:

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

Both Python examples were tested and worked in the following environment:

- Windows `10`
- Python `3.11.8`
- OpenAI Python SDK `1.26.0`

<br>

## Node.js TUI working examples

### Code Interpreter tool

If you run [`tui_personal_math_tutor_v2_beta.js`](https://github.com/rokbenko/ai-playground/blob/main/openai-tutorials/7-TUI_assistants_streaming_Assistants_API_v2_beta/tui_personal_math_tutor_v2_beta.js), you should be able to chat with the personal math tutor assistant:

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

### File Search tool

If you run [`tui_customer_support_chatbot_v2_beta.js`](https://github.com/rokbenko/ai-playground/blob/main/openai-tutorials/7-TUI_assistants_streaming_Assistants_API_v2_beta/tui_customer_support_chatbot_v2_beta.js), you should be able to chat with the customer support chatbot assistant:

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

Both Node.js examples were tested and worked in the following environment:

- Windows `10`
- Node.js `21.2.0`
- OpenAI Node.js SDK `4.42.0`
