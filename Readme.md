# RAG (retrieval augmented generation) with Colombian political constitution 🦜️

[![PyPI - License](https://img.shields.io/pypi/l/langchain-core?style=flat-square)](https://opensource.org/licenses/MIT)



### [Version en Español](Readme_es.md)


This repository demonstrates how to set up a Retrieval-Augmented Generation (RAG) application focused on answering questions about the Colombian political constitution. The project utilizes several cutting-edge technologies, including vector databases, language models, and containerization for deployment.

## Technologies Used
- __Langchain__: A framework for developing applications powered by large language models (LLMs) that simplifies prompt management and model chaining.
- __Streamlit__: A web framework for creating data-driven applications with a simple Python interface.
- __PGVector__: A PostgreSQL extension that provides vector storage and similarity search, enabling efficient retrieval of embeddings.
- __PostgreSQL__: A robust, open-source relational database system used for storing metadata and vector embeddings.
- __Docker__: A platform for developing, shipping, and running applications in isolated containers, ensuring consistent environments.
- __LLM (OpenAI)__: Language models, such as OpenAI's GPT-4, are used to process and answer natural language queries related to the Colombian constitution.

## Project Overview
The purpose of this project is to demonstrate a practical implementation of RAG, where we enhance the language model’s ability to retrieve relevant information from a vector database (PGVector) before generating an answer. This approach increases accuracy and ensures the responses are grounded in relevant, retrieved data.

The project uses Streamlit to build a simple user interface where users can ask questions about the Colombian constitution. The questions are processed using Langchain, which manages the interactions between the LLM and the vector database built with PGVector and PostgreSQL. The system then retrieves relevant information, augments the query with this context, and generates an accurate answer.

In the app file, there is a FastAPI web service endpoint that handles the uploading of new documents to our database. We can implement additional validations and use JWT to authenticate requests, ensuring that invalid or unwanted data is not saved.

### Key Features
- __RAG Architecture__: Combines retrieval and generation steps for more informed and accurate responses.
- __Scalable Vector Search__: Uses PGVector in PostgreSQL for efficient embedding-based searches.
- __LLM Integration__: Uses OpenAI's LLM to generate answers based on retrieved data.
- __User-friendly Interface__: Built with Streamlit for an interactive Q&A experience.
- __Containerized Deployment__: Deployable via Docker for consistent, isolated environments.
- __New Docs__ : WebServices to upload new docs in our vectore database

## Setup

firts clone the repository

```bash
git clone https://github.com/CrasCris/ColombianConstitution-RAG-API.git
cd ColombianConstitution-RAG-API
```

Create a virtual env and active it.

```bash
python -m venv RAGCol

RAGCol\Scripts\activate
```

Install dependencies
```bash
pip install -r requirements.txt
```

Now you can run either the streamlit chat or the fastapi endpoint
```bash
streamlit run src/main.py --server.enableXsrfProtection false
```

```bash
python src/app.py
```

You can also run with Docker, using the DockerFile, just be sure you have docker desktop install and rememer create the __.env__ file to load your OPEN_API_KEY