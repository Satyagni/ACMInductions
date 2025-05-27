from langchain_groq import ChatGroq
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from config import GROQ_API_KEY

memory_store = {}

def create_conversation_chain(model_name):
    llm = ChatGroq(
        api_key=GROQ_API_KEY,
        model_name=model_name,
        temperature=0.7,
        streaming=True,
    )

    memory = ConversationBufferMemory()
    chain = ConversationChain(llm=llm, memory=memory, verbose=False)


    memory_store[model_name] = chain
    return chain


def get_response(user_input, model_name):

    if model_name not in memory_store:
        chain = create_conversation_chain(model_name)
    else:
        chain = memory_store[model_name]

    return chain.predict(input=user_input)
