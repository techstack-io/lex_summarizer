import streamlit as st
import stats

# ------------------------------- Main Function ------------------------------ #

def main():
    """Text Summarizer with Streamlit"""


def home_page():
    col1, mid, col2 = st.columns([1, 1, 20])
    with col1:
        st.image(
            "https://lh3.googleusercontent.com/z1SMpo9HHBl0yHXUrjDUCafhIxjVJ9wTBCwzvRQRq7iT-OUS7iVAfbp3PJ9qvlDWdaxIuwM3DOkyvCRFVzaVgUK9dXn9XhBsWR0zZJ5pz90U5duzCFRlcPgBoJHTJrIwtnG2xCHykQ=w2400",
            width=420,
        )
    """
    ---
    """
    st.markdown(
        "<div align='center'><br>"
        "<img src='https://img.shields.io/badge/MADE WITH-PYTHON -red?style=for-the-badge'"
        "alt='API stability' height='25'/>"
        "<img src='https://img.shields.io/badge/SERVED WITH-Heroku-blue?style=for-the-badge'"
        "alt='API stability' height='25'/>"
        "<img src='https://img.shields.io/badge/DASHBOARDING WITH-Streamlit-green?style=for-the-badge'"
        "alt='API stability' height='25'/></div>",
        unsafe_allow_html=True,
        )
    """
    ---
    """
    st.markdown(
        """ **LEX** is a text summarization tool which allows the user to copy and paste text and summarize its contents. Futhermore, LEX 
    can scrape a webpage (website security options may prevent scraping certain websites), or accept an uploaded file and summarize its contents. 
    This product is currently in development and it is strictly a *proof of concept* and *not optimized for any real time commercial application or insights*. If you encounter any
    any inconsistency or error during the runtime, please get back to us with the error and the dataset so that it can be reproduced and solved.
    Submit the error message to **support@stackmetric.com** for anything more.
    This app is not optimized to summarize less tha 1,000 words and other limitations apply.
    Let's start analyzing with LEX!."""
    )

    row2_spacer1, row2_1, row2_spacer2 = st.columns((0.1, 3.2, 0.1))
    with row2_1:
        user_input = st.text_input(
            "Input your own Goodreads Link (e.g. https://www.goodreads.com/user/show/89659767-tyler-richards)"
        )
        need_help = st.expander("Need help? 👉")

home_page()

# ------------------------------------ END ----------------------------------- #

st.sidebar.subheader("About LEX")
nav = st.sidebar.selectbox(
     'Choose a Page',
     ('Home', 'Summarizer', 'Article Link'))

st.sidebar.info("Contact us at support@stackmetric.io")
st.sidebar.text("The Stackmetric Team")


if nav == 'Homepage':
    home_page()
elif nav == 'Summarizer':
    stats


    if __name__ == '__main__':
        main()
