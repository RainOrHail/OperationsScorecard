import streamlit as st
import pandas as pd

st.set_page_config(page_title="Scorecard Visual App", layout="wide")

st.title("Scorecard Visual App")

uploaded_file = st.file_uploader("Upload your Excel scorecard", type=["xlsx"])

if uploaded_file is None:
    st.stop()

df = pd.read_excel(uploaded_file, header=1)
st.success("File loaded successfully")
st.dataframe(df)
