import streamlit as st

def upload_file():
    st.title("File Uploader")

    # File uploader widget
    uploaded_file = st.file_uploader("Choose a file")

    # Check if a file is uploaded
    if uploaded_file is not None:
        st.write("Uploaded file:", uploaded_file.name)

        # Check the file type and display the content
        if uploaded_file.type == "text/plain":
            # To read a text file
            content = uploaded_file.read().decode("utf-8")
            st.text_area("File content", content, height=300)
        elif uploaded_file.type == "application/pdf":
            # Display PDF file content
            import PyPDF2
            pdf_reader = PyPDF2.PdfFileReader(uploaded_file)
            num_pages = pdf_reader.numPages
            pdf_text = ""
            for page in range(num_pages):
                pdf_text += pdf_reader.getPage(page).extract_text()
            st.text_area("PDF content", pdf_text, height=300)
        else:
            st.write("File type not supported.")
    else:
        st.write("Please upload a file.")

def main():
    upload_file()

if __name__ == "__main__":
    main()
