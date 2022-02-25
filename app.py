from audioop import reverse
import chart_studio
import streamlit as st
from nltk.tokenize import word_tokenize, sent_tokenize
import streamlit.components.v1 as components
from nltk.corpus import stopwords
from typing import ByteString
from wordcloud import WordCloud
import plotly.express as px
import tkinter as tk
import matplotlib.pyplot as plt
import urllib.request
import scipy as sp
import pandas as pd
import numpy as np
import validators
import bs4 as bs
import requests
import string
import heapq
import time
import nltk
import re

chart_studio.tools.set_credentials_file(username='stackmetric', api_key='dKDqbCGui7MYZ2AGfj6l')

# ------------------------------- Main Function ------------------------------ #

import plotly.express as px
import chart_studio.plotly as py
import plotly.graph_objects as go

option = st.selectbox(
    'Please select input method below:',
    ('---', 'Input Text', 'Paste a Link','Upload File'))

s_example = "Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of de Finibus Bonorum et Malorum (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, Lorem ipsum dolor sit amet.., comes from a line in section 1.10.32.The standard chunk of Lorem Ipsum used since the 1500s is reproduced below for those interested. Sections 1.10.32 and 1.10.33 from de Finibus Bonorum et Malorum by Cicero are also reproduced in their exact original form, accompanied by English versions from the 1914 translation by H. Rackham."
    
# ---------------------------------- Text --------------------------------- #

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
                text = re.sub(r'\[[0-9]*\]', ' ', text_input)
                text = re.sub(r'\s+', ' ', text_input)

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
                st.write(summary)
                # --------------------------- Sort Words2count dict -------------------------- #
                dict2list=list(word2count.items())
                # Whole list
                dict2list = sorted(word2count.items(), key=lambda x:x[1], reverse=True)
                #! dict sorted not indexed (whole dictionary)
                sortdict = dict(dict2list)
                sortdict
                #* sorted list of weighted words (descending x7)
                weighted_words_des = dict2list[:7]
                # weighted_words_des

                d=dict(weighted_words_des)
                # Sorted dictionary! 
                d
                keys = d.keys()
                keys
                val = d.values()
                val

                x=keys
                y=val
                print(weighted_words_des)

                trace0 = go.Scatter(

                    x = weighted_words_des, 
                    y = weighted_words_des
                    # x=['qeeg', 'brain', 'death', 'case', 'science', 'penalty' , 'could', 'court'],
                    # y=[1, 0.923076923, 0.538461538, 0.461538462, 0.384615385, 0.346153846, 0.346153846, 0.307692308]
                )
                data = [trace0]

                fig = px.scatter( x=['qeeg', 'brain', 'death', 'case', 'science', 'penalty' , 'could', 'court'],  y=[1, 0.923076923, 0.538461538, 0.461538462, 0.384615385, 0.346153846, 0.346153846, 0.307692308])

                st.write(data)
                st.subheader('Weighted Words')
                st.plotly_chart(fig)
# trace0 = go.Scatter(
#     x=[1, 2, 3, 4],
#     y=[10, 15, 13, 17]
# )
# trace1 = go.Scatter(
#     x=[1, 2, 3, 4],
#     y=[16, 5, 11, 9]
# )
# data = [trace0, trace1]

# py.plot(data, filename = 'basic-line', auto_open=True)

