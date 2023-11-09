import streamlit as st
import pandas as pd
import duckdb

st.write("Hello Write")
data = {"a": [8, 8, 9]}
df = pd.DataFrame(data)

tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])

with tab1:
    query_sql = st.text_area(label="entre ton input")
    st.write(query_sql)
    st.dataframe(duckdb.sql(query_sql).df())
