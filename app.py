
import streamlit as st
import pandas as pd

def upload_file():
    st.title("CSV File Uploader")

    # File uploader widget
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

    # Check if a file is uploaded
    if uploaded_file is not None:
        st.write("Uploaded file:", uploaded_file.name)

        # Display CSV file content using pandas
        df = pd.read_csv(uploaded_file)
        st.dataframe(df)
    else:
        st.write("Please upload a CSV file.")

def main():
    upload_file()
