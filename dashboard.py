import pandas as pd
import streamlit as st 
import plotly.express as pt

st.set_page_config(
    page_title="What skills do I need?",
    page_icon=":bar_chart:",
    layout="wide"
)

df = pd.read_csv(r"C:\Users\lukas\Code\Scrapers\Final_data.csv")

st.dataframe(df)

#----SIDEBAR----
st.sidebar.header("Filter here:")
city = st.sidebar