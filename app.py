import streamlit as st


def setup_webpage():
    st.set_page_config(page_title="PDFChat", page_icon=":books:")

    st.header("What do you want to know? :books:")
    st.text_input("Ask me anything from your PDFs")

    with st.sidebar:
        st.subheader("Attach your PDFs")
        pdf_docs=st.file_uploader("Upload them here",
                                  accept_multiple_files=True)
        if st.button("Process"):
            with st.spinner("Processing..."):



if __name__ == "__main__":
    setup_webpage()