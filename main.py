import streamlit as st
from web_function import load_data

from Tabs import home, predict

Tabs = {
    "Beranda" : home,
    "Prediksi" : predict
}

#sidebar
st.sidebar.title("BANK 123")

#radio option
page = st.sidebar.radio("Page", list(Tabs.keys()))

#load dataset
df, x, y = load_data()

#call app function
if page in ["Prediksi"]:
    Tabs[page].app(df, x, y)
else:
    Tabs[page].app()