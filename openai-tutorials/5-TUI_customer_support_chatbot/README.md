# #5 Terminal user interface for a customer support chatbot

## Short description

Python and Node.js TUIs for the <a href="https://github.com/rokbenko/ai-playground/tree/main/openai-tutorials/4-Build_customer_support_chatbot">#4 Build a customer support chatbot</a> tutorial.

> [!WARNING]
> The assistant might sometimes behave strangely. The Assistants API is still in beta, and it seems that OpenAI has trouble keeping it realiable, as discussed on the official <a href="https://community.openai.com/t/assistant-not-able-to-access-uploaded-file/524495/1">OpenAI forum</a>.
> <br><br>
> The assistant might sometimes answer that it cannot access the files you uploaded. You might think you did something wrong, but if you run identical code later or the next day, the assistant will successfully access all files and give you an answer.
> <br><br>
> The weird responses I got were the following:
>
> - _Assistant: I currently do not have access to the file you uploaded. Could you provide some details about what you're selling or any specific questions you have in mind?_
> - _Assistant: I currently don't have the ability to directly access the contents of the file you uploaded. However, if you can provide some details or specific questions about the
>   than happy to assist you in finding the information you need._
> - _Assistant: I currently don't have visibility into the specific contents of the file you've uploaded. Could you provide more details about the file or its contents so that I can assist you further?_
> - _Assistant: I see you've uploaded a file. How can I assist you with it?_

<br>

## Working example in Python

If you run `tui_customer_support_chatbot.py`, you should be able to chat with a customer support chatbot in a terminal:

> User: What can I buy in your online store?
> <br><br>
> Assistant: In our online store, we sell books. We offer standard and expedited shipping options, and our standard warranty covers products for 1 week from the date of purchase. Additionally, we have a current special offer where customers can use the code DISCOUNT20 to get a 20% discount. If you have any further questions or need assistance, you can reach out to our customer support through the chatbot.
> <br><br>
> User: quit
> <br><br>
> Assistant: Have a nice day! 👋

Environment:

- Windows `10`
- Python `3.12.1`
- OpenAI Python SDK `1.12.0`
- Rich `13.7.0`
- Dotenv `0.21.1`

<br>

## Working example in Node.js

If you run `tui_customer_support_chatbot.js`, you should be able to chat with a customer support chatbot in a terminal:

> User: What can I buy in your online store?
> <br><br>
> Assistant: In our online store, we sell books. We offer standard and expedited shipping options, and our standard warranty covers products for 1 week from the date of purchase. Additionally, we have a current special offer where customers can use the code DISCOUNT20 to get a 20% discount. If you have any further questions or need assistance, you can reach out to our customer support through the chatbot.
> <br><br>
> User: quit
> <br><br>
> Assistant: Have a nice day!

Environment:

- Windows `10`
- Node.js `21.2.0`
- OpenAI Node.js SDK `4.28.0`
- Terminal Kit `3.0.1`
- Dotenv `16.4.3`
