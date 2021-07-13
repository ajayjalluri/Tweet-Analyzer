import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import base64
import pickle
from PIL import Image
import matplotlib.pyplot as plt
import seaborn as sns

page = st.sidebar.selectbox("Select Activity", ["Introduction","Twitter Tweet Prediction",])
st.sidebar.text(" \n")


if page=="Introduction":
    st.header("Twitter Spam Prediction")
    img= Image.open("images//twitter.jpg")
    st.image(img)


if page == "Twitter Tweet Prediction":

    st.header("Twitter Tweet Prediction")


    raw_text = st.text_area("Enter Tweet")

    if st.button("Analyze"):
        st.header("Prediction :")
