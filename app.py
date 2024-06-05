import streamlit as st

def upload_file():
    st.title("File Uploader")

    # File uploader widget
    uploaded_file = st.file_uploader("Choose a file")

    # Check if a file is uploaded
    if uploaded_file is not None:
        st.write("Uploaded file:", uploaded_file.name)
    else:
        st.write("Please upload a file.")

def main():
    upload_file()

if __name__ == "__main__":
    main()
