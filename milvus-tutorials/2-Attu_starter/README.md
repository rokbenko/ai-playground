# #2 Attu (GUI for Milvus) starter

<br>

## 📖 Description 📖

Instructions on how to run Attu, a GUI for Milvus, using Docker.

<br>

## 🔥 How to run Attu 🔥

First, run the following command to get your `IPv4 Address`:

```bash
ipconfig
```

Second, run the following command to start a container for running Attu:

```bash
docker run --name attu -p 8000:3000 -e HOST_URL=http://xxx.xxx.x.x:8000 -e MILVUS_URL=http://xxx.xxx.x.x:19530 zilliz/attu:v2.3.6
```

Where `xxx.xxx.x.x` is your `IPv4 Address`.

<br>

## 🔥 How to get embeddings 🔥

If you run `get_embeddings.py`, you will get a JSON file with key-value pairs matching collection fields in Attu.

See the <a href="https://github.com/rokbenko/ai-playground/blob/main/milvus-tutorials/2-Attu_starter/dummy_data.json">JSON file</a> generated in the tutorial.

### ⚒️ Tech stack ⚒️

OS:

- Windows `10`

Dependencies:

- [Python](https://www.python.org/) `3.12.1`
- [spaCy Python SDK](https://pypi.org/project/spacy/) `3.7.2`
