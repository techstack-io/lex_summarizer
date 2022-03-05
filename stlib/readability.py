# ---------------------------------------------------------------------------- #
#          Stackmetric IO - Copyright ©️ 2022 All Rights Reserved.         #
# ---------------------------------------------------------------------------- #

def run():
 
    import streamlit as st
    import textstat
    import bs4 as bs
    import urllib.request
    import numpy as np
    import pandas as pd
    import requests
    import string
    import heapq
    import time
    import nltk
    import re


    st.sidebar.header('Readability Models:')

    # Models
    with st.sidebar.expander("Flesch Reading Ease"):
        st.write("""The Flesch Reading Ease Formula is a simple approach to assess the grade-level of the reader. It’s also one of the few accurate measures around that we can rely on without too much scrutiny. This formula is best used on school text. It has since become a standard readability formula used by many US Government Agencies, including the US Department of Defense. However, primarily, we use the formula to assess the difficulty of a reading passage written in English.""")
        st.image("https://lh3.googleusercontent.com/pnRwfUWRbgnhq9tcIhjoUFG5tnvLwEu3lpS7ecaSruTADHKaS2BjwRAwmD14G43jn89Jga5qW5HzTd8AODw5YfCnT1QWK35KP4ngvTMfUxqHJhB2H6ZUsK_gcnhRDjYheR4NRbc=w2400")
    
    with st.sidebar.expander("Flesch Kincaid Grade"):
        st.write("""The Flesch Kincaid Grade Level is a widely used readability formula which assesses the approximate reading grade level of a text. It was developed by the US Navy who worked with the Flesch Reading Ease. If a text has a Flesch Kincaid level of 8, this means the reader needs a grade 8 level of reading or above to understand it. Even if they’re an advanced reader, it means the content is less time-consuming to read. """)
    
    with st.sidebar.expander("BERT"):
        st.write("""BERT (Bidirectional tranformer) is a transformer used to overcome the limitations of RNN and other neural networks as Long term dependencies. It is a pre-trained model that is naturally bidirectional. This pre-trained model can be tuned to easily to perform the NLP tasks as specified, Summarization in our case.""")
    # select = st.radio(
    # 'Please select an option:',
    # ('URL', 'Enter or paste text'))

    st.header("READABILITY MODELS")

    c1, c2 = st.columns([.50, .50])

    with c1:
        ModelType = st.selectbox(
        'Please select a model below:',
        ("---", "Flesch Reading Ease", "Flesch Kincaid Grade", "Smog Index", "Coleman Liau Index"))

        # ------------------------- Flesch Reading Ease Model ------------------------ #

        if ModelType == "Flesch Reading Ease":
            Method = st.selectbox(
            'Please select a method of input:',
            ("---", "Text", "URL"))

            if Method == "Text":
                text_input = st.text_area("", max_chars=10000, height=330)
                if st.button("GO"):
                    if len(text_input) != 0:
                        with st.spinner('Processing...'):
                            time.sleep(2)
                            ease = textstat.flesch_reading_ease(text_input)
                            st.subheader(ease)
                            fre_score = "The Flesch Reading Ease score for this text is {ease}".format(ease=ease)
                            st.write(fre_score)
                            if 0 <= ease <= 30:
                                st.write("This text is very difficult to read, and best understood by university graduates. View the readability table under 'Readability Models' for more information")

                    else:
                        st.error("Please enter some text")

           # --------------------------- Flesch Kincaid Grade --------------------------- #

        if ModelType == "Flesch Kincaid Grade":
            Method = st.selectbox(
            'Please select a method of input:',
            ("---", "Text", "URL"))

                # if Method == "Text":
                #     text_input = st.text_area("", max_chars=10000, height=330)
                #     if st.button("GO"):
                #         if len(text_input) != 0:
                #             with st.spinner('Processing...'):
                #                 time.sleep(2)
                #                 ease = textstat.flesch_reading_ease(text_input)
                #                 st.subheader(ease)
                #                 fre_score = "The Flesch Reading Ease score for this text is {ease}".format(ease=ease)
                #                 st.write(fre_score)
                #                 if 0 <= ease <= 30:
                #                     st.write("This text is very difficult to read, and best understood by university graduates. View the readability table under 'Readability Models' for more information")
                #         else:
                #             st.error("Please enter some text")
                # grade = textstat.flesch_kincaid_grade(text)


    # with c2:
    #     doc = st.text_input("Paste your text below (max 500 words)")

    # if select == 'URL':
    #     source_txt = st.text_input("")
    #     if st.button('GO'):
    #         if source_txt is not None:
    #             with st.spinner('Processing...'):
    #                 time.sleep(2)
    #                 modelx = st.selectbox('Please select a model below:',
    #                 (' --- ', 'Flesch Reading Ease', 'Flesch/Kincaid Grade', 'Smog Index', 'Coleman/Liau Index'))

    #                 if modelx b == 'Flesch Reading Ease':
    #                     st.write("The Flesch Reading Ease Formula is a simple approach to assess the grade-level of the reader. It’s also one of the few accurate measures around that we can rely on without too much scrutiny. This formula is best used on school text. It has since become a standard readability formula used by many US Government Agencies, including the US Department of Defense. However, primarily, we use the formula to assess the difficulty of a reading passage written in English.")
    #                     st.image("https://lh3.googleusercontent.com/pnRwfUWRbgnhq9tcIhjoUFG5tnvLwEu3lpS7ecaSruTADHKaS2BjwRAwmD14G43jn89Jga5qW5HzTd8AODw5YfCnT1QWK35KP4ngvTMfUxqHJhB2H6ZUsK_gcnhRDjYheR4NRbc=w2400")
    #                     ease = textstat.flesch_reading_ease(source_txt)
    #                     f_score = ease
    #                     flesch = "This articles Flesch score is {f_score}".format(f_score=f_score) 
    #                     st.subheader(flesch)
        #elif:

            

        #     if models == 'Flesch Reading Ease':
        #         st.write("The Flesch Reading Ease Formula is a simple approach to assess the grade-level of the reader. It’s also one of the few accurate measures around that we can rely on without too much scrutiny. This formula is best used on school text. It has since become a standard readability formula used by many US Government Agencies, including the US Department of Defense. However, primarily, we use the formula to assess the difficulty of a reading passage written in English.")
        #         st.image("https://lh3.googleusercontent.com/pnRwfUWRbgnhq9tcIhjoUFG5tnvLwEu3lpS7ecaSruTADHKaS2BjwRAwmD14G43jn89Jga5qW5HzTd8AODw5YfCnT1QWK35KP4ngvTMfUxqHJhB2H6ZUsK_gcnhRDjYheR4NRbc=w2400")
        #         ease = textstat.flesch_reading_ease(source_txt)
        #         f_score = ease
        #         flesch = "This articles Flesch score is {f_score}".format(f_score=f_score) 
        #         st.subheader(flesch)

            # else:
            #     st.write("Please enter a valid URL")

        # if models == "Flesch Reading Ease":
        #     ease = textstat.flesch_reading_ease(text)
        #     f_score = ease
        #     flesch = "This articles Flesch score is {f_score}".format(f_score=f_score) 
        #     st.subheader(flesch)
        #     st.write("The Flesch Reading Ease Formula is a simple approach to assess the grade-level of the reader. It’s also one of the few accurate measures around that we can rely on without too much scrutiny. This formula is best used on school text. It has since become a standard readability formula used by many US Government Agencies, including the US Department of Defense. However, primarily, we use the formula to assess the difficulty of a reading passage written in English.")

        #     st.image("https://lh3.googleusercontent.com/pnRwfUWRbgnhq9tcIhjoUFG5tnvLwEu3lpS7ecaSruTADHKaS2BjwRAwmD14G43jn89Jga5qW5HzTd8AODw5YfCnT1QWK35KP4ngvTMfUxqHJhB2H6ZUsK_gcnhRDjYheR4NRbc=w2400")
            
        # else:
        #     st.write("Please select a model from the list")
        #     if 'https://' in source_txt:
        #         with st.spinner('Processing...'):
                    
        #             time.sleep(2)

        #             # Retrieve data
        #             URL = source_txt

        #             # Open the URL
        #             page = urllib.request.Request(URL)
        #             result = urllib.request.urlopen(page)

        #             # Store the HTML page in a variable
        #             resulttext = result.read()

        #             # Parsing the data/ creating BeautifulSoup object
        #             soup = bs.BeautifulSoup(resulttext, 'lxml')

        #             # Fetching the data
        #             text = ""
        #             for paragraph in soup.find_all('p'):
        #                 text += paragraph.text

        #             MODELS = srsly.read_json(Path(__file__).parent / "models.json")

        #             model = ["Flesch Reading Ease", "Flesch/Kincaid Grade", "Smog Index", "Coleman/Liau Index"]

        #             models = st.selectbox(
        #             'Please select a model below:',
        #             (' --- ', 'Flesch Reading Ease', 'Flesch/Kincaid Grade', 'Smog Index', 'Coleman/Liau Index'))

        #             if models == "Flesch Reading Ease":
        #                 ease = textstat.flesch_reading_ease(text)
        #                 f_score = ease
        #                 flesch = "This articles Flesch score is {f_score}".format(f_score=f_score) 
        #                 st.subheader(flesch)
        #                 st.write("The Flesch Reading Ease Formula is a simple approach to assess the grade-level of the reader. It’s also one of the few accurate measures around that we can rely on without too much scrutiny. This formula is best used on school text. It has since become a standard readability formula used by many US Government Agencies, including the US Department of Defense. However, primarily, we use the formula to assess the difficulty of a reading passage written in English.")

        #                 st.image("https://lh3.googleusercontent.com/pnRwfUWRbgnhq9tcIhjoUFG5tnvLwEu3lpS7ecaSruTADHKaS2BjwRAwmD14G43jn89Jga5qW5HzTd8AODw5YfCnT1QWK35KP4ngvTMfUxqHJhB2H6ZUsK_gcnhRDjYheR4NRbc=w2400")
                        
        #             else:
        #                 st.write("Please select a model from the list")

        #             grade = textstat.flesch_kincaid_grade(text)
        #             smog_index = textstat.smog_index(text)
        #             laiu_index = textstat.coleman_liau_index(text)


        #     else:
        #         st.error('Please enter a valid link')
  

if __name__ == "__main__":
    run()

