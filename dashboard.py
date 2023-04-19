import pandas as pd
import streamlit as st 
import plotly.express as px

st.set_page_config(
    page_title="What skills do I need?",
    page_icon=":bar_chart:",
    layout="wide"
)

# Cache and load the data
@st.cache_data
def get_data():
    df = pd.read_csv(r"C:\Users\lukas\Code\Scrapers\data.csv")
    return df
df = get_data()

# ---- SIDEBAR ----
st.sidebar.header("Filter here:")
seniority = st.sidebar.multiselect(
    "Select seniority:",
    options=df["seniority"].unique(),
    default=df["seniority"].unique()
)

categorie = st.sidebar.multiselect(
    "Select categorie:",
    options=df["categories"].unique(),
    default=df["categories"].unique()
)

df_selection = df.query(
    "seniority == @seniority & categories == @categorie"
).reset_index(drop=True)

# Count the frequency of each skill required for the selected categories and seniority level
skills_count = pd.Series(
    [skill for skills in df_selection["required_skills"] for skill in eval(skills)]
    ).value_counts()

# Create a horizontal bar chart using Plotly Express to visualize the top 15 required skills
top_skills_count = skills_count.nlargest(15)[::-1]
fig = px.bar(
    top_skills_count,
    x=top_skills_count.values,
    y=top_skills_count.index,
    orientation='h',
    title="Top 15 Required Skills")
fig.update_layout(
    xaxis_title="Appearance count",
    yaxis_title="Skill name")

# ---- MAINPAGE ----
st.title(":bar_chart: What skills do I need to get a job?")

# Display the total number of records in the dataframe
st.write(
    "Number of records:",
    len(df_selection)
    )

# Display the total number of unique skills required for the selected categories and seniority level
st.write(
    "Total number of unique skills required for the selected categories and seniority level:",
    len(skills_count)
    )

# Display the bar chart
st.plotly_chart(fig)

# Display top 16-50 skills
top_16_to_50_skills = skills_count.nlargest(50)[15:].reset_index().rename(
    columns={"index": "Skill name",
    0: "Appearance count"}
    )
top_16_to_50_skills.index = range(16, len(top_16_to_50_skills) + 16)
st.write(
    "**Top 16-50 skills and their appearance count:**"
    )
st.dataframe(
    top_16_to_50_skills,
    height=500
    )

# Display jobs
st.write(
    "**Jobs:**"
    )
df_selection.rename(
    columns={"listing_name": "Listing name", "categories": "Categorie", "seniority": "Seniority", "required_skills": "Required skills"},
    inplace=True
    )
df_selection.index += 1
st.dataframe(
    df_selection,
    use_container_width=True
    )

# Hide streamlit style
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(
    hide_st_style,
    unsafe_allow_html=True
    )