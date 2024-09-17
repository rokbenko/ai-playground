# #1 Get response in JSON format

<br>

## 📖 Description 📖

Python and Node.js examples on how to get a JSON response using the OpenAI Chat Completions API.

<br>

## 🧠 Learning goal 🧠

- **Getting response in JSON format:** Previously, the only way to receive OpenAI API response in JSON format was by specifying this request in the prompt, which was not always reliable. The output was inconsistent, sometimes returning JSON and sometimes not. However, with the recent introduction of the `response_format` parameter, we can now reliably get responses in JSON format.

<br>

## 🔥 Working example in Python 🔥

If you run [`return_json.py`](https://github.com/rokbenko/ai-playground/blob/main/openai-tutorials/1-Get_response_in_JSON_format/return_json.py), you should get the following response:

> {<br> &nbsp;&nbsp;"response": "Hello! How can I assist you today?"<br>
> }<br>
> True

### ⚒️ Tech stack ⚒️

OS:

- Windows `10`

Dependencies:
  
- [Python](https://www.python.org/) `3.10.1`
- [OpenAI Python SDK](https://pypi.org/project/openai/) `1.1.1`

<br>

## 🔥 Working example in Node.js 🔥

If you run [`return_json.js`](https://github.com/rokbenko/ai-playground/blob/main/openai-tutorials/1-Get_response_in_JSON_format/return_json.js), you should get the following response:

> {<br> &nbsp;&nbsp;"response": "Hello! How can I assist you today?"<br>
> }<br>
> true

### ⚒️ Tech stack ⚒️

OS:

- Windows `10`

Dependencies:

- [Node.js](https://nodejs.org/en) `20.9.0`
- [OpenAI Node.js SDK](https://www.npmjs.com/package/openai) `4.16.1`
