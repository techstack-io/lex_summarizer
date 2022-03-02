def run():
    
    # ---------------------------------- Sidebar --------------------------------- #

    import streamlit as st
    
    st.sidebar.header('Built on and with:')
        # Badges
    with st.sidebar:
        st.image("https://img.shields.io/pypi/pyversions/django?style=for-the-badge")
        st.image("https://img.shields.io/conda/vn/conda-forge/python?color=green&style=for-the-badge")
        st.image("https://img.shields.io/badge/DASHBOARDING WITH-Streamlit-green?style=for-the-badge")
    with st.sidebar.expander("NLTK"):
        st.write("""Natural Language Toolkit is an open source Python library for Natural Language Processing.""")
    with st.sidebar.expander("Sumy"):
        st.write("""Sumy - Simple library and command line utility for extracting summary from HTML pages or plain texts.""")
    with st.sidebar.expander("BERT"):
        st.write("""BERT (Bidirectional tranformer) is a transformer used to overcome the limitations of RNN and other neural networks as Long term dependencies. It is a pre-trained model that is naturally bidirectional. This pre-trained model can be tuned to easily to perform the NLP tasks as specified, Summarization in our case..""")
    
 

    # --------------------------------- Homepage --------------------------------- #

    col1, col2, col3 = st.columns([.25,.50,.25])

    with col2:
        st.image("https://lh3.googleusercontent.com/mztJpuCGLVw1qnlFWJZfUDFtPq0xZ37NnviJEG2Yi-ivLq3rAF-cFyZycyRZpa7-e2x86p6AD8twK0Dd5JquIf8F6gf7wXoSaxhe3-IC6Vp4LqhaZnBsRcLXuqP_XU-mc8eqTwyoIg=w2400")



    # st.header("LEX - TEXT SUMMARIZATION AND NLP ENGINE")

    st.write("**LEX** is a text summarization tool which allows the user to copy and paste text and summarize its contents. Futhermore, LEX can scrape a webpage (website security options may prevent scraping certain websites), or accept an uploaded file and summarize its contents. This product is currently in development and it is strictly a *proof of concept* and *not optimized for any real time commercial application or insights*. If you encounter anyany inconsistency or error during the runtime, please get back to us with the error and the dataset so that it can be reproduced and solved.Submit the error message to **support@stackmetric.com** for anything more.  This app is not optimized to summarize less tha 1,000 words and other limitations apply.Let's start analyzing with LEX!.")


if __name__ == "__main__":
    run()