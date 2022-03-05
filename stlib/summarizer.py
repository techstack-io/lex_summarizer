# ---------------------------------------------------------------------------- #
#          Stackmetric IO - Copyright ©️ 2022 All Rights Reserved.         #
# ---------------------------------------------------------------------------- #

def run():

    from nltk.tokenize import word_tokenize, sent_tokenize
    import streamlit as st
    import streamlit.components.v1 as components
    from nltk.corpus import stopwords
    from typing import ByteString
    from wordcloud import WordCloud
    import plotly.express as px
    import chart_studio
    import matplotlib.pyplot as plt
    import scipy as sp
    import pandas as pd
    import numpy as np
    import validators
    import bs4 as bs
    import urllib.request
    import requests
    import string
    import heapq
    import time
    import nltk
    import re

    # ---------------------------------------------------------------------------- #

    st.header("SUMMARIZER")
    st.write(
    """**LEX** is a text summarization tool which allows the user to copy and paste text and summarize its contents. In this section LEX
    can accept copied text or an uploaded file and summarize its contents. 
    This product is currently in development and it is strictly a *proof of concept* and *not optimized for any real time commercial application or insights*. If you encounter any
    any inconsistency or error during the runtime, please get back to us with the error and the dataset so that it can be reproduced and solved.
    Submit the error message to **support@stackmetric.com** for anything more.
    This app is not optimized to summarize less tha 1,000 words and other limitations apply."""
    )

    model = st.selectbox(
     'Please select input method below:',
     ('---', 'Frequency Based', 'Luhns Algorithm', 'Upload File'))

    # option = st.selectbox(
    #  'Please select input method below:',
    #  ('---', 'Input Text', 'Paste a Link','Upload File'))

    s_example = "Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of de Finibus Bonorum et Malorum (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, Lorem ipsum dolor sit amet.., comes from a line in section 1.10.32.The standard chunk of Lorem Ipsum used since the 1500s is reproduced below for those interested. Sections 1.10.32 and 1.10.33 from de Finibus Bonorum et Malorum by Cicero are also reproduced in their exact original form, accompanied by English versions from the 1914 translation by H. Rackham."

    # -------------------------------- Text Input -------------------------------- #

    if model == 'Frequency Based':
        option = st.selectbox(
        'Please select input method below:',
        ('---', 'Input Text', 'Paste a Link','Upload File'))
        if option == 'Input Text':
            text_input = st.text_area("Use the example below or input your own \
                text in English (between 1,000 and 10,000 characters)", value=s_example, max_chars=10000, height=330)

            if st.button('Summarize'):
                if len(text_input) < 1000:
                    st.error('Please enter a text in English of minimum 1,000 \
                        characters')
                else:
                    with st.spinner('Processing...'):
                        time.sleep(2)
                        st.text('')

                        # Raw Text
                        text = re.sub(r'\[[0-9]*\]', ' ', text_input)
                        text = re.sub(r'\s+', ' ', text_input)

                        nltk.download('punkt')
                        nltk.download('stopwords')

                        # Clean Text
                        clean_text = text.lower()
                        clean_text = re.sub(r'\W', ' ', clean_text)
                        clean_text = re.sub(r'\d', ' ', clean_text)
                        clean_text = re.sub(r'\s+', ' ', clean_text)
                        stopwords = nltk.corpus.stopwords.words('english')
                        word_frequency = nltk.FreqDist(nltk.word_tokenize
                                                        (clean_text))
                        # Word Dictionary
                        word2count = {}
                        for word in nltk.word_tokenize(clean_text):
                            if word not in stopwords:
                                if word not in word2count.keys():
                                    word2count[word] = 1
                                else:
                                    word2count[word] += 1

                        highest_frequency = max(word2count.values())
                        highest_frequency

                        # Weighted Words
                        for word in word2count.keys():
                            word2count[word] = (word2count[word] / highest_frequency)

                        # Tokenize sentences
                        sentences = nltk.sent_tokenize(text)

                        # Sentence Dictionary
                        sent2score = {}
                        for sentence in sentences:
                            for word in nltk.word_tokenize(sentence.lower()):
                                if word in word2count.keys():
                                    if len(sentence.split(' ')) < 25:
                                        if sentence not in sent2score.keys():
                                            sent2score[sentence] = word2count[word]
                                        else:
                                            sent2score[sentence] += word2count[word]

                        best_sentences = heapq.nlargest(10, sent2score, key=sent2score.get)
                        summary = ' '.join(best_sentences)
                        summary
                        st.write(summary)
                        # Wordcloud
                        st.write("Word Cloud")
                        st.set_option('deprecation.showPyplotGlobalUse', False)
                        wordcloud = WordCloud(background_color = "#f2f8fb", width=800, height=400).generate(summary)
                        plt.imshow(wordcloud, interpolation='bilinear')
                        plt.axis("off")
                        plt.show()
                        # st.pyplot()

                        # Plotly Charts #

                        # --- Lists 

                        # Convert word2count dict to a list
                        dict2list=list(word2count.items())

                        # Sort list in descending order
                        dict2list = sorted(word2count.items(), key=lambda x:x[1], reverse=True)

                        # First 7 words in sorted list of weighted words in descending order
                        weighted_words_des = dict2list[:7]

                        # --- Dicts 

                        # Covert sorted list back to dict (this is the complete dict)
                        sortdict = dict(dict2list)

                        # Sorted dict
                        d=dict(weighted_words_des)

                        # Separate keys and values
                        keys = d.keys()
                        val = d.values()

                        # Convert keys and values into a list
                        # This will be our x and y axis for our chart
                        x_axis = list(keys)
                        y_axis = list(val)

                        st.write(highest_frequency)

                        fig = px.bar(x=x_axis, y=y_axis, labels=dict(x="Words", y="Weight", color="Place"))
                        st.subheader('Weighted Words')
                        st.plotly_chart(fig)

                        highF = "The word that appears the most in the article is " + x_axis[0]
                        numy = highest_frequency
                        numx = y_axis[0]
                        numofx = x_axis[0] + " - It appears {numy} times".format(numy=numy, numx=numx) 
                        numF = x_axis[0] + " also has a weight of {numx} which makes is the most important word in this article".format(numx=numx)

                        st.subheader(highF)
                        st.subheader(numofx)
                        st.subheader(numF)
                        # END Tex Input #

    # -------------------------------- Link Input -------------------------------- #

        if option == 'Paste a Link':
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

                        # Raw Text
                        text = re.sub(r'\[[0-9]*\]', ' ', text)
                        text = re.sub(r'\s+', ' ', text)

                        # Clean Text
                        clean_text = text.lower()
                        clean_text = re.sub(r'\W', ' ', clean_text)
                        clean_text = re.sub(r'\d', ' ', clean_text)
                        clean_text = re.sub(r'\s+', ' ', clean_text)

                        nltk.download('punkt')
                        nltk.download('stopwords')

                        stopwords = nltk.corpus.stopwords.words('english')
                        word_frequency = nltk.FreqDist(nltk.word_tokenize(clean_text))
                        sentences = nltk.sent_tokenize(text)

                        # Create a `dictionary` and name it word2count where words [keys] and counts [values]
                        word2count = {}
                        for word in nltk.word_tokenize(clean_text):
                            if word not in stopwords:
                                if word not in word2count.keys():
                                    word2count[word] = 1
                                else:
                                    word2count[word] += 1

                        highest_frequency = max(word2count.values())
                        highest_frequency

                        for word in word2count.keys():
                            word2count[word] = (word2count[word] / highest_frequency)

                        sent2score = {}
                        for sentence in sentences:
                            for word in nltk.word_tokenize(sentence.lower()):
                                if word in word2count.keys():
                                    if len(sentence.split(' ')) < 25:
                                        if sentence not in sent2score.keys():
                                            sent2score[sentence] = word2count[word]
                                        else:
                                            sent2score[sentence] += word2count[word]

                        best_sentences = heapq.nlargest(10, sent2score, key=sent2score.get)
                        summary = ' '.join(best_sentences)
                        summary
                        st.write(summary)

                        # ------------------------------- Plotly Charts ------------------------------ #

                        # ------------ Lists ------------- #

                        # Convert word2count dict to a list
                        dict2list=list(word2count.items())

                        # Sort list in descending order
                        dict2list = sorted(word2count.items(), key=lambda x:x[1], reverse=True)

                        # First 7 words in sorted list of weighted words in descending order
                        weighted_words_des = dict2list[:7]

                        # ------------ Dicts --------------------- #

                        # Covert sorted list back to dict (this is the complete dict)
                        sortdict = dict(dict2list)

                        # Sorted dict
                        d=dict(weighted_words_des)

                        # Separate keys and values
                        keys = d.keys()
                        val = d.values()

                        # Convert keys and values into a list
                        # This will be our x and y axis for our chart
                        x_axis = list(keys)
                        y_axis = list(val)

                        highF = "The word that appears the most in the article is " + x_axis[0]
                        numy = highest_frequency
                        numx = y_axis[0]
                        numofx = "The word " + x_axis[0] + " appears {numy} times".format(numy=numy, numx=numx) 
                        numF = x_axis[0] + " also has a weight of {numx} which makes is the most important word in this article".format(numx=numx)

                        st.subheader(highF)
                        st.subheader(numofx)
                        st.subheader(numF)

                        fig = px.bar(x=x_axis, y=y_axis, labels=dict(x="Words", y="Weight", color="Place"))
                        st.subheader('Weighted Words')
                        st.plotly_chart(fig)
                        # END Tex Input #        
                else:
                    st.error('Please enter a valid link')


if __name__ == "__main__":
    run()


