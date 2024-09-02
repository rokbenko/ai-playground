# #2 Attu starter

<br>

## 📖 Description 📖

Instructions on how to run Attu, a GUI for Milvus Standalone, using Docker.

<br>

## 🧠 Learning goals 🧠

- **Setting up [Attu](https://milvus.io/docs/v2.1.x/attu.md) with Docker:** We will learn how to set up Attu using Docker. Attu is an open-source management tool for Milvus. It features an intuitive graphical user interface (i.e., GUI), allowing you to easily interact with your databases. With just a few clicks, you can visualize your cluster status, manage metadata, perform data queries, and much more. The steps include:

1. Getting your `IPv4` address
2. Running the Docker command to start the Attu container
3. Verifying the setup by checking Docker Desktop and accessing the Attu dashboard via localhost

- **Managing Milvus Standalone database with Attu:** We will explore how to manage the Milvus Standalone database in Attu by performing the following tasks:

    - Adding a Milvus collection in Attu
    - Creating an index for the Milvus collection in Attu
    - Loading the Milvus collection in Attu
    - Using spaCy to convert text to embedding vectors (using Python)
    - Storing embedding vectors in a JSON file (using Python)
    - Importing the data via JSON file and previewing it in Attu

<br>

## 🚀 Installation 🚀

### Getting the `IPv4` address

Run the following command to get your `IPv4` address:

```bash
ipconfig
```

### Starting the Docker container

Run the following command to start the Docker container for running Attu:

```bash
docker run --name attu -p 8000:3000 -e HOST_URL=http://xxx.xxx.x.x:8000 -e MILVUS_URL=http://xxx.xxx.x.x:19530 zilliz/attu:v2.3.6
```

Where `xxx.xxx.x.x` is your `IPv4` address.

### Creating embedding vectors

If you run [`get_embeddings.py`](https://github.com/rokbenko/ai-playground/blob/main/milvus-tutorials/2-Attu_starter/get_embeddings.py), you will get a JSON file with key-value pairs matching collection fields in Attu.

See the <a href="https://github.com/rokbenko/ai-playground/blob/main/milvus-tutorials/2-Attu_starter/dummy_data.json">JSON file</a> generated in the tutorial.

#### ⚒️ Tech stack ⚒️

OS:

- Windows `10`

Dependencies:

- [Python](https://www.python.org/) `3.12.1`
- [spaCy Python SDK](https://pypi.org/project/spacy/) `3.7.2`
