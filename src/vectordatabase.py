from langchain_openai import OpenAIEmbeddings
from langchain_postgres.vectorstores import PGVector
from sqlalchemy import  URL ,create_engine
from langchain.text_splitter import CharacterTextSplitter

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-large",
)
connection_string = URL.create( drivername="postgresql", database="postgres", username="postgres", password="julian1234", host="localhost", port="5432", )
COLLECTION_NAME = "Constitucion"

def postgres_connection():
    """Connection with our vector database"""
    pgvector_docsearch = PGVector(
    collection_name=COLLECTION_NAME,
    connection= create_engine(connection_string),
    embeddings=embeddings,
    use_jsonb=True,
    )
    return pgvector_docsearch

# initialize our connection
pgvector_docsearch = postgres_connection()

def vector_query_setup():
    retriever = pgvector_docsearch.as_retriever()
    return retriever
    
def save_embeddings(documents,collection:str=COLLECTION_NAME):
    text_splitter = CharacterTextSplitter(chunk_size=2500, chunk_overlap=100)
    docs = text_splitter.split_documents(documents)
    try:
        pgvector_docsearch.from_documents(
            embedding=embeddings,
            documents=docs,
            collection_name=collection,
            connection= create_engine(connection_string),
            pre_delete_collection=False,)
    except Exception as e:
        raise KeyError(f"Error during save embeddings {str(e)}")


