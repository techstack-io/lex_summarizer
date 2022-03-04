
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

  
    # select = st.radio(
    # 'Please select an option:',
    # ('URL', 'Enter or paste text'))

    c1, c2 = st.columns([.33, .66])

    with c1:
        ModelType = st.radio(
            "Choose your model",
            ["Flesch Reading Ease", "Flesch/Kincaid Grade", "Smog Index", "Coleman/Liau Index" ],
            help="Choose from 4 models",
        )

   
        if ModelType == "Flesch Reading Ease":
            
            source_txt = st.text_input("")
            
            if st.button('GO'):
                ease = textstat.flesch_reading_ease(source_txt)
                st.subheader(ease)      
            
            @st.cache(allow_output_mutation=True)
            def load_model():
                source_txt = st.text_input("")
                ease = textstat.flesch_reading_ease(source_txt)
                return ease
            

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
  


# end of app

# This code allows you to run the app standalone
# as well as part of a library of apps
if __name__ == "__main__":
    run()

