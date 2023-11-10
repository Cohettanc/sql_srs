import streamlit as st
import pandas as pd
import duckdb

st.write("Spaced Repetition Sytem for SQL")
data = {"a": [8, 8, 9]}
df = pd.DataFrame(data)

option = st.selectbox("what would you like to review?",
                      ["Joins", "GroupBy", "Windows Functions"],
                      index = None,
                      placeholder='Select a topic')



query_sql = st.text_area(label="entre ton input")
st.write(query_sql)
st.dataframe(duckdb.sql(query_sql).df())
