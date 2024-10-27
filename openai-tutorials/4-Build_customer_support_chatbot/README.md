# #4 Customer Support Chatbot

## 📖 Description 📖

Python and Node.js examples on how to build a Customer Support Chatbot using the OpenAI Assistants API `v1` beta with the Knowledge Retrieval tool.

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

## 🧠 Learning goals 🧠

- **Understanding the flow of the OpenAI Assistants API `v1` beta:** We will explore the complete process of building an assistant using the OpenAI Assistants API `v1` beta. The steps include:

1. Creating an assistant
2. Creating a thread
3. Adding a user message to the thread
4. Running the assistant
5. Periodically checking the run status to see if it has moved to completed
6. Retrieving the assistant answer

- **Building a customer support chatbot:** We will apply these steps to build a customer support chatbot using the OpenAI Assistants API `v1` beta with the Knowledge Retrieval tool.

<br>

## 🔥 Working example in Python 🔥

If you run [`customer_support_chatbot.py`](https://github.com/rokbenko/ai-playground/blob/main/openai-tutorials/4-Build_customer_support_chatbot/customer_support_chatbot.py), you should get the following response:

> This is the file object: FileObject(xxxxx)
>
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
> Run status: completed
>
> \------------------------------------------------------------
>
> User: What can I buy in your online store? <br>
> Assistant: In your online store, you sell books. You offer standard and expedited shipping, with a standard warranty that covers products for 1 week from the date of purchase.
> There is also a special offer available now - customers can use the DISCOUNT20 coupon to get a 20% discount. If you have any further questions or need assistance, you can reach out to the customer support through the chatbot.

### ⚒️ Tech stack ⚒️

OS:

- Windows `10`

Dependencies:

- [Python](https://www.python.org/) `3.12.1`
- [OpenAI Python SDK](https://pypi.org/project/openai/) `1.7.2`

<br>

## 🔥 Working example in Node.js 🔥

If you run [`customer_support_chatbot.js`](https://github.com/rokbenko/ai-playground/blob/main/openai-tutorials/4-Build_customer_support_chatbot/customer_support_chatbot.js), you should get the following response:

> This is the file object: {xxxxx}
>
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
> Run status: completed
>
> \------------------------------------------------------------
>
> User: What can I buy in your online store? <br>
> Assistant: In our online store, we sell books. We offer standard and expedited shipping options and
> provide a standard warranty that covers products for 1 week from the date of purchase. Currently, we
> have a special offer - customers can use the "DISCOUNT20" coupon code to get a 20% discount. If you have any further questions or need assistance, our customer support is available through the chatbot
> you're currently using.

### ⚒️ Tech stack ⚒️

OS:

- Windows `10`

Dependencies:

- [Node.js](https://nodejs.org/en) `21.2.0`
- [OpenAI Node.js SDK](https://www.npmjs.com/package/openai) `4.24.7`
