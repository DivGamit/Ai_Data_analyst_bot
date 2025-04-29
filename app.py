import streamlit as st
from file_handler import handle_uploads
from agent import run_agent
from dotenv import load_dotenv
import os

load_dotenv()

st.set_page_config(page_title="AI Data Bot", layout="wide")
st.title("🤖 AI Data Analysis Bot")

uploaded_files = st.file_uploader("Upload PDF, CSV, or DOCX files", type=["pdf", "csv", "docx"], accept_multiple_files=True)

if uploaded_files:
    docs, dataframes = handle_uploads(uploaded_files)
    user_input = st.text_input("Ask a question or request a chart:")

    if user_input:
        result = run_agent(user_input, docs, dataframes)
        if isinstance(result, str):
            st.write(result)
        else:
            st.pyplot(result)
