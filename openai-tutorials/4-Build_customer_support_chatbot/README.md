# #4 Build a customer support chatbot

<br>

## 📖 Description 📖

Python and Node.js examples on how to build a customer support chatbot with the OpenAI Assistants API `v1` beta using the Knowledge Retrieval tool.

> [!NOTE]
> The code in this tutorial works with the [OpenAI Assistants API `v1` beta](https://platform.openai.com/docs/api-reference/assistants-v1). In April 2024, the [OpenAI Assistants API `v2` beta](https://platform.openai.com/docs/api-reference/assistants) was released. See the [migration guide](https://platform.openai.com/docs/assistants/migration/agents).

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
- [OpenAI Python API SDK](https://pypi.org/project/openai/) `1.7.2`

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
- [OpenAI Node.js API SDK](https://www.npmjs.com/package/openai) `4.24.7`
