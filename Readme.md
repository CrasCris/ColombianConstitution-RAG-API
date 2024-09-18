# RAG (retrieval augmented generation) with Colombian political constitution

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

### Key Features
- __RAG Architecture__: Combines retrieval and generation steps for more informed and accurate responses.
- __Scalable Vector Search__: Uses PGVector in PostgreSQL for efficient embedding-based searches.
- __LLM Integration__: Uses OpenAI's LLM to generate answers based on retrieved data.
- __User-friendly Interface__: Built with Streamlit for an interactive Q&A experience.
- __Containerized Deployment__: Deployable via Docker for consistent, isolated environments.

### Coming soon Setup Instructions and fastapi endpoint to manage vectordatabase and spanish version
