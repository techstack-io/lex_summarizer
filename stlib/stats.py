
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
  
    select = st.radio(
    "Please select an option:",
    ('Paste a Link', 'Drama'))

    if select == 'Paste a Link':
                source_txt = st.text_input("")
                if st.button('Paste a Link'):
                    if 'https://' in source_txt:
                        with st.spinner('Processing...'):
                            time.sleep(2)

                            # Retrieve data
                            URL = source_txt

                            # Open the URL
                            page = urllib.request.Request(URL)
                            result = urllib.request.urlopen(page)

                            # Store the HTML page in a variable
                            resulttext = result.read()

                            # Parsing the data/ creating BeautifulSoup object
                            soup = bs.BeautifulSoup(resulttext, 'lxml')

                            # Fetching the data
                            text = ""
                            for paragraph in soup.find_all('p'):
                                text += paragraph.text

                            ease = textstat.flesch_reading_ease(text)
                            f_score = ease
                            flesch = "This articles Flesch score is {f_score}".format(f_score=f_score) 
                            st.subheader(flesch)
                            st.write("The Flesch Reading Ease Formula is a simple approach to assess the grade-level of the reader. It’s also one of the few accurate measures around that we can rely on without too much scrutiny. This formula is best used on school text. It has since become a standard readability formula used by many US Government Agencies, including the US Department of Defense. However, primarily, we use the formula to assess the difficulty of a reading passage written in English.")
   
                            
                            st.image("https://lh3.googleusercontent.com/pnRwfUWRbgnhq9tcIhjoUFG5tnvLwEu3lpS7ecaSruTADHKaS2BjwRAwmD14G43jn89Jga5qW5HzTd8AODw5YfCnT1QWK35KP4ngvTMfUxqHJhB2H6ZUsK_gcnhRDjYheR4NRbc=w2400")
                            
                            grade = textstat.flesch_kincaid_grade(text)
                            smog_index = textstat.smog_index(text)
                            laiu_index = textstat.coleman_liau_index(text)


                    else:
                        st.error('Please enter a valid link')
  


# end of app

# This code allows you to run the app standalone
# as well as part of a library of apps
if __name__ == "__main__":
    run()

