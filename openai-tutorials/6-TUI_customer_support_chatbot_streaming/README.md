# #6 Python and Node.js TUIs for the Customer Support Chatbot with response streaming

## 📖 Description 📖

Python and Node.js TUIs for the <a href="https://github.com/rokbenko/ai-playground/tree/main/openai-tutorials/4-Build_customer_support_chatbot">#4 Customer Support Chatbot</a> tutorial with response streaming.

> [!NOTE]
> The code in this directory works with the [OpenAI Assistants API `v1` beta](https://platform.openai.com/docs/api-reference/assistants-v1). In April 2024, the [OpenAI Assistants API `v2` beta](https://platform.openai.com/docs/api-reference/assistants) was released. See the [migration guide](https://platform.openai.com/docs/assistants/migration/agents).

<br>

## 🧠 Learning goal 🧠

- **Adding response streaming functionality in the OpenAI Assistants API `v1` beta:** We will add response streaming to our TUIs built in the [previous](https://github.com/rokbenko/ai-playground/tree/main/openai-tutorials/5-TUI_customer_support_chatbot) tutorial. Response streaming allows for partial results to be delivered in real-time as they are generated, rather than waiting for the entire response to be ready. This feature enhances the user experience by providing faster feedback and making interactions feel more dynamic and engaging. It's particularly useful for applications where quick, responsive communication is critical, such as in chatbots.

<br>

## 🔥 Working example in Python 🔥

If you run [`tui_customer_support_chatbot_streaming.py`](https://github.com/rokbenko/ai-playground/blob/main/openai-tutorials/6-TUI_customer_support_chatbot_streaming/tui_customer_support_chatbot_streaming.py), you should be able to chat with the customer support chatbot in a terminal and receive its responses in a **streaming(!)** way:

> User: What can I buy in your online store?
> <br><br>
> Assistant: In our online store, we sell books. We offer standard and expedited shipping options, and our standard warranty covers products for 1 week from the date of purchase. Additionally, we have a current special offer where customers can use the code DISCOUNT20 to get a 20% discount. If you have any further questions or need assistance, you can reach out to our customer support through the chatbot.
> <br><br>
> User: quit
> <br><br>
> Assistant: Have a nice day! 👋

### ⚒️ Tech stack ⚒️

OS:

- Windows `10`

Dependencies:

- [Python](https://www.python.org/) `3.11.8`
- [OpenAI Python SDK](https://pypi.org/project/openai/) `1.14.2`
- [Rich](https://pypi.org/project/rich/) `13.7.0`
- [Dotenv](https://pypi.org/project/python-dotenv/) `1.0.1`

<br>

## 🔥 Working example in Node.js 🔥

If you run [`tui_customer_support_chatbot_streaming.js`](https://github.com/rokbenko/ai-playground/blob/main/openai-tutorials/6-TUI_customer_support_chatbot_streaming/tui_customer_support_chatbot_streaming.js), you should be able to chat with the customer support chatbot in a terminal and receive its responses in a **streaming(!)** way:

> User: What can I buy in your online store?
> <br><br>
> Assistant: In our online store, we sell books. We offer standard and expedited shipping options, and our standard warranty covers products for 1 week from the date of purchase. Additionally, we have a current special offer where customers can use the code DISCOUNT20 to get a 20% discount. If you have any further questions or need assistance, you can reach out to our customer support through the chatbot.
> <br><br>
> User: quit
> <br><br>
> Assistant: Have a nice day!

### ⚒️ Tech stack ⚒️

OS:

- Windows `10`

Dependencies:

- [Node.js](https://nodejs.org/en) `21.2.0`
- [OpenAI Node.js SDK](https://www.npmjs.com/package/openai) `4.29.2`
- [Terminal Kit](https://www.npmjs.com/package/terminal-kit) `3.0.1`
- [Dotenv](https://www.npmjs.com/package/dotenv) `16.4.3`

<br>

## 📽️ Demonstration 📽️

![Demonstration of how to chat with a customer support chatbot in a terminal and receive its responses in a streaming way](https://github.com/rokbenko/ai-playground/blob/main/openai-tutorials/6-TUI_customer_support_chatbot_streaming/demonstration.gif)
