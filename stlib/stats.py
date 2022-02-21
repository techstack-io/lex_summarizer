import streamlit as st

def run():
 
    import streamlit as st

    st.header("Example app 1")
    st.write("Insert your own Streamlit code here")

# end of app

# This code allows you to run the app standalone
# as well as part of a library of apps
if __name__ == "__main__":
    run()


def load_page():
    """
    ---
    """
    st.header("SUMMARIZER")
    st.write(
    """**LEX** is a text summarization tool which allows the user to copy and paste text and summarize its contents. In this section LEX
    can accept copied text or an uploaded file and summarize its contents. 
    This product is currently in development and it is strictly a *proof of concept* and *not optimized for any real time commercial application or insights*. If you encounter any
    any inconsistency or error during the runtime, please get back to us with the error and the dataset so that it can be reproduced and solved.
    Submit the error message to **support@stackmetric.com** for anything more.
    This app is not optimized to summarize less tha 1,000 words and other limitations apply."""
    )