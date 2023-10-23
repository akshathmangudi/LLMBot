import streamlit as st
from src.data_extraction import get_pdf_text, get_chunks
from src.data_handling import get_vector_embed, create_chain, handle_userinput
from dotenv import load_dotenv
from src.html_templates import css, user_template, bot_template


def setup_webpage():
    """
    This function sets the root page of our streamlit application.
    This has been linked to our LangChain + InstructorEmbeddings model
    in order to perform pdf querying as well as a chatbot-like
    interaction.
    """

    load_dotenv()
    st.set_page_config(page_title="PDFChat", page_icon=":books:")

    st.write(css, unsafe_allow_html=True)

    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None

    st.header("What do you want to know? :books:")
    st.text_input("Ask me anything from your PDFs")

    st.write(user_template.replace("{{MSG}}", "Hello there!"), unsafe_allow_html=True)
    st.write(bot_template.replace("{{MSG}}", "Hello"), unsafe_allow_html=True)

    with st.sidebar:
        st.subheader("Attach your PDFs")
        pdf_docs = st.file_uploader("Upload them here",
                                    accept_multiple_files=True)
        if st.button("Process"):
            with st.spinner("Processing..."):
                raw_text = get_pdf_text(pdf_docs)
                st.write(raw_text)

                text_chunks = get_chunks(raw_text)
                st.write(text_chunks)

                vec_store = get_vector_embed(text_chunks, 'cuda')
                st.session_state.conversation = create_chain(vec_store)
    st.session_state.conversation


if __name__ == "__main__":
    setup_webpage()
