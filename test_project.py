import streamlit as st
import pandas as pd
from project import get_data, get_filtered_data, create_bar_chart

# Test that data can be loaded and returned as a pandas DataFrame
def test_get_data():
    assert isinstance(get_data(), pd.DataFrame)

# Test that filtered data is returned correctly
def test_get_filtered_data():
    df = get_data()
    df_selection, skills_count = get_filtered_data(df)
    assert isinstance(df_selection, pd.DataFrame)
    assert isinstance(skills_count, pd.Series)

# Test that the bar chart is created correctly
def test_create_bar_chart():
    skills_count = pd.Series({'skill1': 100, 'skill2': 80, 'skill3': 50})
    fig = create_bar_chart(skills_count)
    assert fig.data[0].x.tolist() == [50, 80, 100]
    assert fig.data[0].y.tolist() == ['skill3', 'skill2', 'skill1']
