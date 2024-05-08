# #7 Assistants API `v1` to `v2` beta migration

## Short description

Examples on how to migrate the OpenAI Assistants API `v1` to `v2` beta:

- Python TUI for the File Search tool (see [`tui_customer_support_chatbot_v2_beta.py`](https://github.com/rokbenko/ai-playground/tree/main/openai-tutorials/7-Assistants_API_v1_to_v2_beta_migration/TUI/tui_customer_support_chatbot_v2_beta.py))
- Node.js TUI for the File Search tool (see [`tui_customer_support_chatbot_v2_beta.js`](https://github.com/rokbenko/ai-playground/tree/main/openai-tutorials/7-Assistants_API_v1_to_v2_beta_migration/TUI/tui_customer_support_chatbot_v2_beta.js))
- Python TUI for the Code Interpreter tool (see [`tui_personal_math_tutor_v2_beta.py`](https://github.com/rokbenko/ai-playground/tree/main/openai-tutorials/7-Assistants_API_v1_to_v2_beta_migration/TUI/tui_personal_math_tutor_v2_beta.py))
- Node.js TUI for the Code Interpreter tool (see [`tui_personal_math_tutor_v2_beta.js`](https://github.com/rokbenko/ai-playground/tree/main/openai-tutorials/7-Assistants_API_v1_to_v2_beta_migration/TUI/tui_personal_math_tutor_v2_beta.js))
- Next.js GUI for the File Search tool and Code Interpreter tool (Coming soon... ✨)
- Streamlit GUI for the File Search tool and Code Interpreter tool (Coming soon... ✨)

> [!NOTE]
> For those unfamiliar with the terms "TUI" and "GUI":
>
> - TUI stands for _Text User Interface_
> - GUI stands for _Graphical User Interface_

<a href="https://github.com/Textualize/rich">rich</a> is used as a Python terminal formatter.

```bash
pip install rich
```

<a href="https://github.com/cronvel/terminal-kit">terminal-kit<a> is used as a Node.js terminal formatter.

```bash
npm install terminal-kit
```

<br>

## Python TUI working examples

### File Search tool

If you run `tui_customer_support_chatbot_v2_beta.py`, you should be able to chat with the customer support chatbot assistant:

> ai-playground\openai-tutorials\7-Assistants_API_v1_to_v2_beta_migration> python tui_customer_support_chatbot_v2_beta.py<br> > <br>
> User: What can I buy in your online store?<br> > <br>
> Assistant: Assistant: In our online store, we currently sell books. We offer standard and expedited shipping options, and our standard warranty covers products for 1 week from the date of purchase. Additionally, we have a special offer available where you can use the DISCOUNT20 coupon to get a 20% discount on your purchase. If you have any further questions or need assistance, you can contact our customer support through the chatbot. Feel free browse our selection and take advantage of the discount offer!<br> > <br>
> User: quit<br> > <br>
> Assistant: Have a nice day! 👋<br> > <br>
> ai-playground\openai-tutorials\7-Assistants_API_v1_to_v2_beta_migration>

### Code Interpreter tool

If you run `tui_personal_math_tutor_v2_beta.py`, you should be able to chat with the personal math tutor assistant:

> ai-playground\openai-tutorials\7-Assistants_API_v1_to_v2_beta_migration> python tui_personal_math_tutor_v2_beta.py<br> > <br>
> User: I need to solve the equation 3x + 11 = 14. Can you help me?<br> > <br>
> Assistant: The solution to the equation 3x + 11 = 14 is x = 1.<br> > <br>
> User: quit<br> > <br>
> Assistant: Have a nice day! 👋<br> > <br>
> ai-playground\openai-tutorials\7-Assistants_API_v1_to_v2_beta_migration>

## Node.js TUI working examples

### File Search tool

If you run `tui_customer_support_chatbot_v2_beta.js`, you should be able to chat with the customer support chatbot assistant:

> ai-playground\openai-tutorials\7-Assistants_API_v1_to_v2_beta_migration> python tui_customer_support_chatbot_v2_beta.js<br> > <br>
> User: What can I buy in your online store?<br> > <br>
> Assistant: Assistant: In our online store, we currently sell books. We offer standard and expedited shipping options, and our standard warranty covers products for 1 week from the date of purchase. Additionally, we have a special offer available where you can use the DISCOUNT20 coupon to get a 20% discount on your purchase. If you have any further questions or need assistance, you can contact our customer support through the chatbot. Feel free browse our selection and take advantage of the discount offer!<br> > <br>
> User: quit<br> > <br>
> Assistant: Have a nice day!<br> > <br>
> ai-playground\openai-tutorials\7-Assistants_API_v1_to_v2_beta_migration>

### Code Interpreter tool

If you run `tui_personal_math_tutor_v2_beta.js`, you should be able to chat with the personal math tutor assistant:

> ai-playground\openai-tutorials\7-Assistants_API_v1_to_v2_beta_migration> python tui_personal_math_tutor_v2_beta.js<br> > <br>
> User: I need to solve the equation 3x + 11 = 14. Can you help me?<br> > <br>
> Assistant: The solution to the equation 3x + 11 = 14 is x = 1.<br> > <br>
> User: quit<br> > <br>
> Assistant: Have a nice day!<br> > <br>
> ai-playground\openai-tutorials\7-Assistants_API_v1_to_v2_beta_migration>

## Next.js GUI example

Coming soon... ✨

## Streamlit GUI example

Coming soon... ✨
