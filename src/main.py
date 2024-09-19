# Import dependencies
from langchain_openai.chat_models import ChatOpenAI
from vectordatabase import vector_query_setup
from langchain_core.messages import AIMessage, HumanMessage
import streamlit as st
from prompt import fill_prompt_memory,fill_prompt
from dotenv import load_dotenv
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_history_aware_retriever
from langchain.chains import create_retrieval_chain

load_dotenv()
@st.cache_resource
def load_llm():
    '''
        This function load in server memory the information of the bruno PDF, and transform to use in our LLM model
    '''

    llm = ChatOpenAI(model='gpt-4o-mini-2024-07-18')
    db = vector_query_setup()
    prompt_memory = fill_prompt_memory()
    prompt_chat = fill_prompt()
    history_aware_retriever = create_history_aware_retriever(llm, db, prompt_memory) 
    question_answer_chain = create_stuff_documents_chain(llm, prompt_chat)
    rag_chain = create_retrieval_chain(history_aware_retriever, question_answer_chain)

    return rag_chain 

# Load the chain
chain = load_llm()

if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

st.title("Chat Constitucion Colombiana")

if 'messages' not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    st.chat_message(message['role']).markdown(message['content'])

question = st.chat_input('Enter your questions here')

if question:
    st.chat_message('user').markdown(question)
    st.session_state.messages.append({'role': 'user', 'content': question})
    try:
        result = chain.invoke({"input": question, "chat_history": st.session_state.chat_history})
        final_result= result["answer"]
        # Add memory history
        st.session_state.chat_history.extend([
            HumanMessage(content=question),
            AIMessage(content=final_result),
        ])
        st.chat_message('assistant').markdown(final_result)
        st.session_state.messages.append({'role': 'assistant', 'content': final_result})

    except Exception as e:
        st.error(f"Error: {e}")