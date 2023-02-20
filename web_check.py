import streamlit as st
import sqlite3
import pandas as pd

db = sqlite3.connect("resources/database.db", check_same_thread=False)
df = pd.read_sql_query("SELECT * FROM contact", db)

page_size = 10
empty = st.empty()
empty.dataframe(df.iloc[0:page_size, :])

next_btn = st.button("Next", key="next", help="Next page")
prev_btn = st.button("Prev", key="prev", help="Previous page")

if next_btn:
    empty.dataframe(df.iloc[page_size:page_size*2, :])
if prev_btn:
    empty.dataframe(df.iloc[0:page_size, :])
