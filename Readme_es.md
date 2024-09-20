# RAG (retrieval augmented generation) Constitución politica de Colombia 🦜️

[![PyPI - License](https://img.shields.io/pypi/l/langchain-core?style=flat-square)](https://opensource.org/licenses/MIT)



### [English Version](Readme.md)


Este repositorio demuestra cómo configurar una aplicación de Generación Aumentada de Recuperación (RAG) enfocada en responder preguntas sobre la constitución política colombiana. El proyecto utiliza varias tecnologías de vanguardia, incluidas bases de datos vectoriales, modelos de lenguaje y contenedorización para la implementación.

## Tecnologias usadas
- __Langchain__: Un framework para desarrollar aplicaciones impulsadas por modelos de lenguaje grandes (LLM) que simplifica la gestión rápida y el encadenamiento de modelos.
- __Streamlit__: Un framework para crear aplicaciones basadas en datos con una interfaz Python sencilla.
- __PGVector__: Una extensión de PostgreSQL que proporciona almacenamiento vectorial y búsqueda de similitud, lo que permite una recuperación eficiente de incrustaciones.
- __PostgreSQL__: Un sistema de base de datos relacional robusto y de código abierto utilizado para almacenar metadatos e incrustaciones vectoriales.
- __Docker__: Una plataforma para desarrollar, enviar y ejecutar aplicaciones en contenedores aislados, garantizando entornos consistentes.
- __LLM (OpenAI)__: Se utilizan modelos de lenguaje, como GPT-4 de OpenAI, para procesar y responder consultas en lenguaje natural relacionadas con la constitución colombiana.

## Descripción general del proyecto
El propósito de este proyecto es demostrar una implementación práctica de RAG, donde mejoramos la capacidad del modelo de lenguaje para recuperar información relevante de una base de datos vectorial (PGVector) antes de generar una respuesta. Este enfoque aumenta la precisión y garantiza que las respuestas se basen en datos recuperados relevantes.

El proyecto utiliza Streamlit para crear una interfaz de usuario simple donde los usuarios pueden hacer preguntas sobre la constitución colombiana. Las preguntas se procesan utilizando Langchain, que administra las interacciones entre el LLM y la base de datos vectorial creada con PGVector y PostgreSQL. Luego, el sistema recupera la información relevante, amplía la consulta con este contexto y genera una respuesta precisa.

En el archivo de la aplicación, hay un punto final del servicio web FastAPI que maneja la carga de nuevos documentos a nuestra base de datos. Podemos implementar validaciones adicionales y utilizar JWT para autenticar solicitudes, lo que garantiza que no se guarden datos no válidos o no deseados.

### Key Features
- __Arquitectura RAG__
- __Busqueda vectorial__
- __LLM__
- __Interfaz de usuario__
- __Contenedor listo para el despliegue__
- __Añadir nuevos documentos__ 

## Configuración

Clonar el repositorio

```bash
git clone https://github.com/CrasCris/ColombianConstitution-RAG-API.git
cd ColombianConstitution-RAG-API
```

Crear un entorno virtual

```bash
python -m venv RAGCol

RAGCol\Scripts\activate
```

Instalar las dependencias
```bash
pip install -r requirements.txt
```

Ejecutar en local la aplicacion de streamlit o fastapi
```bash
streamlit run src/main.py --server.enableXsrfProtection false
```

```bash
python src/app.py
```

También puedes ejecutar con Docker, usando DockerFile, solo asegúrate de tener instalado Docker Desktop y recuerda crear el archivo __.env__ para cargar tu OPEN_API_KEY