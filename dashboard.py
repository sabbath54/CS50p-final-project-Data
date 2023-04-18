import pandas as pd
import streamlit as st 
import plotly.express as px

st.set_page_config(
    page_title="What skills do I need?",
    page_icon=":bar_chart:",
    layout="wide"
)

df = pd.read_csv(r"C:\Users\lukas\Code\Scrapers\Final_data.csv")

# ---- SIDEBAR ----
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

# Count the frequency of each skill required for the selected categories and seniority level
skills_count = pd.Series([skill for skills in df_selection["required_skills"] for skill in eval(skills)]).value_counts()

# Create a pie chart using Plotly Express to visualize the distribution of skills required
fig = px.pie(skills_count, values=skills_count.values, names=skills_count.index, title="Distribution of Required Skills")

# ---- MAINPAGE ----
st.title(":bar_chart: What skills do I need to get a job?")
st.markdown("##")

# Display the total number of unique skills required for the selected categories and seniority level
st.write("Total number of unique skills required for the selected categories and seniority level:", len(skills_count))

# Display the pie chart
st.plotly_chart(fig)

# Display results
st.write("Skill count:")
st.dataframe(skills_count)
st.write("Jobs:")
st.dataframe(df_selection, use_container_width=True)
