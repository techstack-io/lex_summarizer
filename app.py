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
    
# ---------------------------------- Text Input --------------------------------- #

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

                fig = px.bar(x=x_axis, y=y_axis)

                st.subheader('Weighted Words')
                st.plotly_chart(fig)


