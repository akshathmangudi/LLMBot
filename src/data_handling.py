import streamlit as st
from langchain.embeddings import OpenAIEmbeddings, HuggingFaceInstructEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationalBufferMemory
from langchain.chains import ConversationalRetrievalChain
from html_templates import user_template, bot_template


def get_vector_embed(text_chunks, device):
    # embeddings = OpenAIEmbeddings()
    embeddings = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-xl").to(device)
    vec_store = FAISS.from_texts(texts=text_chunks,
                                 embedding=embeddings)
    return vec_store


def create_chain(vec_store):
    llm_model = OpenAI()
    memory = ConversationalBufferMemory(memory_key='chat_history',
                                        return_messages=True)

    convo_chain = ConversationalRetrievalChain.from_llm(
        llm = llm_model,
        retriever=vec_store.as_retriever(),
        memory=memory
    )

    return convo_chain


def handle_userinput(question):
    response = st.session_state.conversation({'question': question})
    st.session_state.chat_history = response['chat_history']

    for i, message in enumerate(st.session_state.chat_history):
        if i % 2 == 0:
            st.write(user_template.replace("{{MSG}}", message.content),
                     unsafe_allow_html=True)
        else:
            st.write(bot_template.replace("{{MSG}}", message.content),
                     unsafe_allow_html=True)
    st.write(response)
