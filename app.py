import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

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
        
        # Data visualization using Matplotlib
        if not df.empty:
            st.subheader("Data Visualization")
            
            # Assuming the CSV file has columns 'X' and 'Y'
            fig, ax = plt.subplots()
            ax.scatter(df['X'], df['Y'])
            ax.set_xlabel('X')
            ax.set_ylabel('Y')
            ax.set_title('Scatter Plot')
            
            # Display the plot in Streamlit
            st.pyplot(fig)
    else:
        st.write("Please upload a CSV file.")

def main():
    upload_file()

if __name__ == "__main__":
    main()
