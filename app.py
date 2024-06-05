import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def upload_and_visualize():
    st.title("CSV File Uploader and Visualizer")
    
    # File uploader widget
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    
    if uploaded_file is not None:
        st.write("Uploaded file:", uploaded_file.name)
        
        # Load the CSV file into a DataFrame
        df = pd.read_csv(r"C:\Users\Viswajith\Downloads\BankNote_Authentication.csv")
        
        # Display the DataFrame
        st.write("Data Preview:")
        st.write(df.head())
        
        # Data visualization using Matplotlib
        st.subheader("Data Visualization")
        x_column = st.selectbox("Select X-axis column", df.columns)
        y_column = st.selectbox("Select Y-axis column", df.columns)
        
        if st.button("Generate Scatter Plot"):
            fig, ax = plt.subplots()
            ax.scatter(df[x_column], df[y_column])
            ax.set_xlabel(x_column)
            ax.set_ylabel(y_column)
            ax.set_title(f"{y_column} vs {x_column}")
            st.pyplot(fig)
    else:
        st.write("Please upload a CSV file.")

def main():
    upload_and_visualize()

if __name__ == "__main__":
    main()
