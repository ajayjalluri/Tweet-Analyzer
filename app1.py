import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import base64
import pickle
from PIL import Image
import matplotlib.pyplot as plt
import seaborn as sns

import nltk
import re
from nltk.corpus import stopwords


import pickle

from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, GlobalAveragePooling1D, Dense, Dropout, LSTM, Bidirectional
from bs4 import BeautifulSoup
from tensorflow import keras

model2 = keras.models.load_model('twitter_glove_bi-lstm.h5')

nltk.download('stopwords')


with open("tokenizer.pkl", "rb") as t:
    token = pickle.load(t)
vocab_size = len(token.word_index)+1
# embedding_matrix = np.load("embedding_matrix.npy")
max_len = 30



def decontracted(phrase):
    # specific
    phrase = re.sub(r"won't", "will not", phrase)
    phrase = re.sub(r"can\'t", "can not", phrase)

    # general
    phrase = re.sub(r"n\'t", " not", phrase)
    phrase = re.sub(r"\'re", " are", phrase)
    phrase = re.sub(r"\'s", " is", phrase)
    phrase = re.sub(r"\'d", " would", phrase)
    phrase = re.sub(r"\'ll", " will", phrase)
    phrase = re.sub(r"\'t", " not", phrase)
    phrase = re.sub(r"\'ve", " have", phrase)
    phrase = re.sub(r"\'m", " am", phrase)
    return phrase



page = st.sidebar.selectbox("Select Activity", ["Introduction","Twitter Tweet Prediction",])
st.sidebar.text(" \n")


if page=="Introduction":
    st.header("Twitter Spam Prediction")
    img= Image.open("images//twitter.jpg")
    st.image(img)


if page == "Twitter Tweet Prediction":

    st.header("Twitter Tweet Prediction [ SPAM / NON - SPAM ]")


    raw_text = st.text_area("Enter Tweet")
    preprocessed_Tweets =[]
    if st.button("Analyze"):

        sentance = str(raw_text)
        sentance = re.sub(r"http\S+", "", sentance)
        sentance = BeautifulSoup(sentance, 'html').get_text()
        sentance = decontracted(sentance)
        sentance = re.sub("\S*\d\S*", "", sentance).strip()
        sentance = re.sub('[^A-Za-z]+', ' ', sentance)
        # https://gist.github.com/sebleier/554280
        sentance = ' '.join(e.lower() for e in sentance.split() if e.lower() not in stopwords.words('english'))
        preprocessed_Tweets.append(sentance.strip())




        token_sent = token.texts_to_sequences(preprocessed_Tweets)

        c = model2.predict_classes(token_sent)
        if c[0][0] == 0 :
            st.header("PREDICTION - NON SPAM")
        else :
            st.header("PREDICTION - SPAM")
