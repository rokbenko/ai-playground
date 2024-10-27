# #1 Streamlit GUI for a Personal Recipe Assistant

## 📖 Description 📖

Streamlit GUI for a Personal Recipe Assistant that generates recipes based on the available ingredients recognized from the uploaded photo and selected preferences by the user.

<br>

## 🧠 Learning goal 🧠

- **Understanding [JigsawStack](https://jigsawstack.com/):** JigsawStack is an SDK designed to streamline the integration of AI functionalities into various tech stacks. It offers a comprehensive suite of APIs that provide capabilities such as an advanced prompt engine, web scraping, image generation, vision OCR, TTS, and STT, among others. Its user-friendly design allows developers to quickly implement features without extensive configuration, ensuring a smooth developer experience. Built on a globally distributed serverless edge network, JigsawStack guarantees low latency, high availability, and seamless scalability.

<br>

## 🚀 Getting started 🚀

To start using the app, follow these steps:

1. Clone the repository: `git clone https://github.com/rokbenko/ai-playground.git`
2. Change the directory: `cd ai-playground/jigsawstack-tutorials/1-GUI_personal_recipe_assistant`
3. Create a `secrets.toml` file inside the `.streamlit` folder to set up your environment variables
4. Run the app: `streamlit run 1_Upload_photo.py`
5. To view the app, navigate to [http://localhost:8501](http://localhost:8501)

> [!IMPORTANT]
> Your `secrets.toml` file should contain the following environment variables:
>
> ```bash
> JIGSAWSTACK_PRIVATE_API_KEY = "sk_xxxxxxxxxxxxxxxxxxxxxxxxx"
> JIGSAWSTACK_PUBLIC_API_KEY = "pk_xxxxxxxxxxxxxxxxxxxxxxxxx"
> ```

<br>

## ⚒️ Tech stack ⚒️

OS:

- Windows `10`

Dependencies:

- [Python](https://www.python.org/) `3.11.8`
- [Streamlit](https://pypi.org/project/streamlit/) `1.38.0`
- [JigsawStack Python SDK](https://pypi.org/project/jigsawstack/) `0.1.11`

<br>

## 📽️ Demonstration 📽️

![Demonstration of the app](https://github.com/rokbenko/ai-playground/blob/main/jigsawstack-tutorials/1-GUI_personal_recipe_assistant/demonstration.gif)
