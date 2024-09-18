from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder


behavior = """
Responde las preguntas que te hagan basandote en el contexto, 
eres un asistente que responde preguntas sobre la consitutcion politica de colombia.
Solo debes responder información de la constitucion politica.
{context}
"""

contextualize_q_system_prompt = (
    "Dado un historial de chat y la última pregunta del usuario,"
    "que podría hacer referencia al contexto en el historial de chat,"
    "formule una pregunta independiente que pueda entenderse,"
    "sin el historial de chat. NO responda la pregunta,"
    "solo reformúlela si es necesario y, de lo contrario, devuélvala tal como está"
)

contextualize_q_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", contextualize_q_system_prompt),
        MessagesPlaceholder("chat_history"),
        ("human", "{input}"),
    ]
)


def fill_prompt_memory():
    """
        This function is for chat_history generations
    """
    contextualize_q_prompt = ChatPromptTemplate.from_messages(
        [
            ("system", contextualize_q_system_prompt),
            MessagesPlaceholder("chat_history"),
            ("human", "{input}"),
        ]
    )
    return contextualize_q_prompt


def fill_prompt():
    """
        This function is for retrieval query
    """

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", behavior),
            MessagesPlaceholder("chat_history"),
            ("human", "{input}"),
        ]
    )
    return prompt

