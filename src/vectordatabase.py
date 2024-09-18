from langchain_openai import OpenAIEmbeddings
from langchain_postgres.vectorstores import PGVector
from sqlalchemy import  URL ,create_engine

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-large",
)

def postgres_connection():
    """Connection with our vector database"""
    connection_string = URL.create( drivername="postgresql", database="postgres", username="postgres", password="julian1234", host="localhost", port="5432", )
    engine = create_engine(connection_string)
    COLLECTION_NAME = "Constitucion"
    pgvector_docsearch = PGVector(
    collection_name=COLLECTION_NAME,
    connection=engine,
    embeddings=embeddings,
    use_jsonb=True,
    )
    return pgvector_docsearch

# initialize our connection
pgvector_docsearch = postgres_connection()

def vector_query_setup():
    retriever = pgvector_docsearch.as_retriever()
    return retriever
    


