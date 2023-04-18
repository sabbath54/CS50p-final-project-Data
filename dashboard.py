import pandas as pd
import streamlit as st 
import plotly.express as pt

st.set_page_config(
    page_title="What skills do I need?",
    page_icon=":bar_chart:",
    layout="wide"
)

df = pd.read_csv(r"C:\Users\lukas\Code\Scrapers\Final_data.csv")

#----SIDEBAR----
st.sidebar.header("Filter here:")
seniority = st.sidebar.multiselect(
    "Select seniority:",
    options=df["seniority"].unique(),
)

categorie = st.sidebar.multiselect(
    "Select categorie:",
    options=df["categories"].unique(),
)

df_selection = df.query(
    "seniority == @seniority & categories == @categorie"
)

st.dataframe(df_selection)