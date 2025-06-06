import streamlit as st
import pandas as pd

st.title("My First Streamlit App")
df = pd.DataFrams({
    'Column 1': [1,2,3,4],
    'Column 2': [10,20,30,40]
})
st.write(df)
st.line_chart(df)