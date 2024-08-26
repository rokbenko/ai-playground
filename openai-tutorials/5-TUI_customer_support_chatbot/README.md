# #5 Python and Node.js TUIs for a customer support chatbot

<br>

## 📖 Description 📖

Python and Node.js TUIs for the <a href="https://github.com/rokbenko/ai-playground/tree/main/openai-tutorials/4-Build_customer_support_chatbot">#4 Build a customer support chatbot</a> tutorial.

> [!WARNING]
> The assistant might sometimes behave strangely. The Assistants API is still in beta, and it seems that OpenAI has trouble keeping it realiable, as discussed on the official <a href="https://community.openai.com/t/assistant-not-able-to-access-uploaded-file/524495/1">OpenAI forum</a>.
> <br><br>
> The assistant might sometimes answer that it cannot access the files you uploaded. You might think you did something wrong, but if you run identical code later or the next day, the assistant will successfully access all files and give you an answer.
> <br><br>
> The weird responses I got were the following:
>
> - _Assistant: I currently do not have access to the file you uploaded. Could you provide some details or any specific questions you have in mind?_
> - _Assistant: I currently don't have the ability to directly access the contents of the file you uploaded. However, if you can provide some details or specific questions, I would be happy to assist you in finding the information you need._
> - _Assistant: I currently don't have visibility into the specific contents of the file you've uploaded. Could you provide more details about the file or its contents so that I can assist you further?_

> [!NOTE]
> The code in this directory works with the [OpenAI Assistants API `v1` beta](https://platform.openai.com/docs/api-reference/assistants-v1). In April 2024, the [OpenAI Assistants API `v2` beta](https://platform.openai.com/docs/api-reference/assistants) was released. See the [migration guide](https://platform.openai.com/docs/assistants/migration/agents).

<br>

## 🧠 Learning goal 🧠

- **Building Python and Node.js TUIs for the OpenAI Assistants API `v1` beta:** We will build a terminal user interface (i.e., TUI) using Python and Node.js, designed to interact with the OpenAI Assistants API `v1` beta. These TUIs are specifically tailored to chat with the customer support chatbot built in the [previous](https://github.com/rokbenko/ai-playground/tree/main/openai-tutorials/4-Build_customer_support_chatbot) tutorial.

<br>

## 🔥 Working example in Python 🔥

If you run [`tui_customer_support_chatbot.py`](https://github.com/rokbenko/ai-playground/blob/main/openai-tutorials/5-TUI_customer_support_chatbot/tui_customer_support_chatbot.py), you should be able to chat with a customer support chatbot in a terminal:

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

- [Python](https://www.python.org/) `3.12.1`
- [OpenAI Python API SDK](https://pypi.org/project/openai/) `1.12.0`
- [Rich](https://pypi.org/project/rich/) `13.7.0`
- [Dotenv](https://pypi.org/project/python-dotenv/) `1.0.1`

<br>

## 🔥 Working example in Node.js 🔥

If you run [`tui_customer_support_chatbot.js`](https://github.com/rokbenko/ai-playground/blob/main/openai-tutorials/5-TUI_customer_support_chatbot/tui_customer_support_chatbot.js), you should be able to chat with a customer support chatbot in a terminal:

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
- [OpenAI Node.js API SDK](https://www.npmjs.com/package/openai) `4.28.0`
- [Terminal Kit](https://www.npmjs.com/package/terminal-kit) `3.0.1`
- [Dotenv](https://www.npmjs.com/package/dotenv) `16.4.3`
