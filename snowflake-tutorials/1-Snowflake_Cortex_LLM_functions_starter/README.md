# #1 Snowflake Cortex LLM functions starter

<br>

## 📖 Description 📖

Python example on how to use the Snowflake Cortex LLM functions.

> [!IMPORTANT]
> Before you run [`snowflake_cortex_llm.py`](https://github.com/rokbenko/ai-playground/blob/main/snowflake-tutorials/1-Snowflake_Cortex_LLM_functions_starter/snowflake_cortex_llm.py), create an `.env` file to set up your environment variables.
>
> Your `.env` file should contain the following environment variables:
>
> ```bash
> SNOWFLAKE_ACCOUNT="xxxxxxx-xxxxxxx"
> SNOWFLAKE_USER="xxxxx"
> SNOWFLAKE_USER_PASSWORD="xxxxx"
> ```

<br>

## 🔥 Working example in Python 🔥

If you run [`snowflake_cortex_llm.py`](https://github.com/rokbenko/ai-playground/blob/main/snowflake-tutorials/1-Snowflake_Cortex_LLM_functions_starter/snowflake_cortex_llm.py), you should get an output:

> Summarize() is experimental since 1.0.12. Do not use it in production.<br>
> Summarize() Snowflake Cortex LLM function result:<br>
> Recent advancements in artificial intelligence are revolutionizing industries like healthcare and finance, enhancing efficiency and accuracy. However, ethical concerns such as data privacy, bias, and job displacement arise. Global competition in AI research and development is intensifying, requiring international cooperation and regulation. It's crucial to foster ethical AI practices and collaboration for maximum benefits.
> 
> Complete() is experimental since 1.0.12. Do not use it in production.<br>
> Complete() Snowflake Cortex LLM function result:<br>
> 1. Artificial Intelligence
> 2. Advancements
> 3. Revolutionized
> 4. Industries
> 5. Ethical Concerns
> 
> ExtractAnswer() is experimental since 1.0.12. Do not use it in production.<br>
> ExtractAnswer() Snowflake Cortex LLM function result:<br>
> [<br>
> &nbsp;&nbsp;&nbsp;&nbsp;{<br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"answer": "data privacy, algorithmic bias, and the potential for job displacement",<br>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"score": 0.9978588<br>
> &nbsp;&nbsp;&nbsp;&nbsp;}<br>
> ]
> 
> Sentiment() is experimental since 1.0.12. Do not use it in production.<br>
> Sentiment() Snowflake Cortex LLM function result:<br>
> 0.5044461
> 
> Translate() is experimental since 1.0.12. Do not use it in production.<br>
> Translate() Snowflake Cortex LLM function result:<br>
> Die jüngsten Fortschritte in der Zusammenarbeit mit KI können verschiedene Branchen revolutionieren. Von der Gesundheitsversorgung bis hin zu Finanzmitteln steihen revolutioniegern KI-gestützte Lösungen die Effizienz und Genauigkeit. Im Gesundheitswesen wie Lösungen die Erd KI verwendet, um den vollständigen Ausgang von Patienten vorherzusagen, Behandigen Ausgang vodlungspläne zu personalisieren und sogar bei Operationen zu helfen. Finanzielle rationen zu helf
> Institutionen nutzen KI, um betrügerische Aktivitäten aufzuzeugen und verantwortn und verantwortungsvoll einzurichten, bieten persönliche Banking

<br>

## ⚒️ Tech stack ⚒️

OS:

- Windows `10`

Dependencies:

- [Python](https://www.python.org/) `3.11.8`
- [Snowflake Python SDK](https://pypi.org/project/snowflake/) `0.8.0`
- [Dotenv](https://pypi.org/project/python-dotenv/) `1.0.1`
