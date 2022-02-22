def run():
    
    # ---------------------------------- Sidebar --------------------------------- #

    import streamlit as st
    
    st.sidebar.header('Libraries:')
    with st.sidebar.expander("NLTK"):
        st.write("""Natural Language Toolkit is an open source Python library for Natural Language Processing.""")
    with st.sidebar.expander("Sumy"):
        st.write("""Sumy - Simple library and command line utility for extracting summary from HTML pages or plain texts.""")
    with st.sidebar.expander("BERT"):
        st.write("""BERT (Bidirectional tranformer) is a transformer used to overcome the limitations of RNN and other neural networks as Long term dependencies. It is a pre-trained model that is naturally bidirectional. This pre-trained model can be tuned to easily to perform the NLP tasks as specified, Summarization in our case..""")
    
 

    # --------------------------------- Homepage --------------------------------- #
    
    st.header("LEX - TEXT SUMMARIZATION AND NLP ENGINE")
    st.markdown(""" **LEX** is a text summarization tool which allows the user to copy and paste text and summarize its contents. Futhermore, LEX 
    can scrape a webpage (website security options may prevent scraping certain websites), or accept an uploaded file and summarize its contents. 
    This product is currently in development and it is strictly a *proof of concept* and *not optimized for any real time commercial application or insights*. If you encounter any
    any inconsistency or error during the runtime, please get back to us with the error and the dataset so that it can be reproduced and solved.
    Submit the error message to **support@stackmetric.com** for anything more.
    This app is not optimized to summarize less tha 1,000 words and other limitations apply.
    Let's start analyzing with LEX!."""
    )

    # Badges
    st.markdown(
    "<div align='left'><br>"
    "<img src='https://img.shields.io/badge/MADE WITH-PYTHON -red?style=for-the-badge'"
    "alt='API stability' height='25'/>"
    "<img src='https://img.shields.io/badge/SERVED WITH-Heroku-blue?style=for-the-badge'"
    "alt='API stability' height='25'/>"
    "<img src='https://img.shields.io/badge/DASHBOARDING WITH-Streamlit-green?style=for-the-badge'"
    "alt='API stability' height='25'/></div>"
    "<br/>",
    unsafe_allow_html=True,
    )

    row2_spacer1, row2_1, row2_spacer2 = st.columns((0.1, 3.2, 0.1))
    with row2_1:
        user_input = st.text_input(
            "Input your own Goodreads Link (e.g. https://www.goodreads.com/user/show/89659767-tyler-richards)"
        )
        need_help = st.expander("Need help? 👉")

if __name__ == "__main__":
    run()