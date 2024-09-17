# Import dependencies
from langchain_core.output_parsers import StrOutputParser
from langchain_openai.chat_models import ChatOpenAI
from vectordatabase import vector_query_setup
import streamlit as st
from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain.memory import ConversationBufferMemory

load_dotenv()

@st.cache_resource
def load_llm():
    '''
        This function load in server memory the information of the bruno PDF, and transform to use in our LLM model
    '''
    parser = StrOutputParser()
    memory = ConversationBufferMemory(return_messages=True) # will be implemente later
    llm = ChatOpenAI(model='gpt-4o-mini-2024-07-18')
    template = """
    Responde las preguntas que te hagan basandote en el contexto, 
    eres un asistente que responde preguntas sobre la consitutcion politica de colombia
    Context: {context}
    Question: {question}
    """
    setup =vector_query_setup()

    prompt = ChatPromptTemplate.from_template(template)
    chain = setup | prompt | llm | parser
    return chain 

# Load the chain and memory
chain = load_llm()

st.title("Ask about Colombian Constitucion")

if 'messages' not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    st.chat_message(message['role']).markdown(message['content'])

question = st.chat_input('Enter your questions here')

if question:
    st.chat_message('user').markdown(question)
    st.session_state.messages.append({'role': 'user', 'content': question})
    try:
        result = chain.invoke(question)
        st.chat_message('assistant').markdown(result)
        st.session_state.messages.append({'role': 'assistant', 'content': result})
    except Exception as e:
        st.error(f"Error: {e}")