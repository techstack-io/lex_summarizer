def run():
    
    # ---------------------------------- Sidebar --------------------------------- #

    import streamlit as st
    
    # with st.sidebar:
    #     st.image("https://lh3.googleusercontent.com/nDOoz4Jb1mkEZWxLOgCoZ2LXmeaL1rmBfJRAKftffgwUSNKaqe-a9_3WzMLaPkB2Qt-k71zaqG14icbC5Pg0DcZ2voKZsWd5uKiwaspyjhqqIv0b_38amdEVJMUTASC7oBZ8JnAnjw=w300")  

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

    col1, col2, col3 = st.columns([12.5,75,12.5])

    with col2:
        st.image("https://lh3.googleusercontent.com/5XLeASxlnhN_3iYtrVf2Z8Dhw7QyoRKqJbVI832d8ZWM26PYM3WUb6GR_9tqw3yV_9b2YsN2vgtRqef3vEA5Aem7Gfmi-DDPkKyif-E_2fF2HjXUX3rrorB3kEcFT6C5NhBsbls=w2000")



    st.header("TEXT SUMMARIZATION AND NLP ENGINE")

    st.write("**LEX** is a text summarization tool which allows the user to copy and paste text and summarize its contents. Futhermore, LEX can scrape a webpage (website security options may prevent scraping certain websites), or accept an uploaded file and summarize its contents. This product is currently in development and it is strictly a *proof of concept* and *not optimized for any real time commercial application or insights*. If you encounter anyany inconsistency or error during the runtime, please get back to us with the error and the dataset so that it can be reproduced and solved.Submit the error message to **support@stackmetric.com** for anything more.  This app is not optimized to summarize less tha 1,000 words and other limitations apply.Let's start analyzing with LEX!.")


if __name__ == "__main__":
    run()