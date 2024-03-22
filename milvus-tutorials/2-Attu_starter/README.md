# #2 Attu (GUI for Milvus) starter

## Short description

Instructions on how to run Attu, a GUI for Milvus, using Docker.

<br>

## Run Attu

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

## Python script to get embeddings

If you run `get_embeddings.py`, you will get a JSON file with key-value pairs matching collection fields in Attu.

See the <a href="https://github.com/rokbenko/ai-playground/blob/main/milvus-tutorials/2-Attu_starter/dummy_data.json">JSON file</a> generated in the tutorial.

Environment:

- Windows `10`
- Python `3.12.1`
- spaCy Python SDK `3.7.2`
