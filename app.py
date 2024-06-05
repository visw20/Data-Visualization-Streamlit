import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def upload_file():
    st.title("CSV File Uploader and Visualizer")

    # File uploader widget
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

    # Check if a file is uploaded
    if uploaded_file is not None:
        st.write("Uploaded file:", uploaded_file.name)

        # Display CSV file content using pandas
        df = pd.read_csv(uploaded_file)
        st.dataframe(df)
        
        # Basic visualizations
        st.write("## Visualizations")
        
        # Line plot
        st.write("### Line Plot")
        columns = df.columns.tolist()
        x_axis = st.selectbox("Select X-axis column for line plot", columns)
        y_axis = st.selectbox("Select Y-axis column for line plot", columns)
        
        if st.button("Generate Line Plot"):
            fig, ax = plt.subplots()
            ax.plot(df[x_axis], df[y_axis])
            ax.set_xlabel(x_axis)
            ax.set_ylabel(y_axis)
            ax.set_title(f"{y_axis} vs {x_axis}")
            st.pyplot(fig)
        
        # Bar plot
        st.write("### Bar Plot")
        x_axis_bar = st.selectbox("Select X-axis column for bar plot", columns, key="bar_x")
        y_axis_bar = st.selectbox("Select Y-axis column for bar plot", columns, key="bar_y")
        
        if st.button("Generate Bar Plot"):
            fig, ax = plt.subplots()
            ax.bar(df[x_axis_bar], df[y_axis_bar])
            ax.set_xlabel(x_axis_bar)
            ax.set_ylabel(y_axis_bar)
            ax.set_title(f"{y_axis_bar} vs {x_axis_bar}")
            st.pyplot(fig)
        
        # Scatter plot
        st.write("### Scatter Plot")
        x_axis_scatter = st.selectbox("Select X-axis column for scatter plot", columns, key="scatter_x")
        y_axis_scatter = st.selectbox("Select Y-axis column for scatter plot", columns, key="scatter_y")
        
        if st.button("Generate Scatter Plot"):
            fig, ax = plt.subplots()
            ax.scatter(df[x_axis_scatter], df[y_axis_scatter])
            ax.set_xlabel(x_axis_scatter)
            ax.set_ylabel(y_axis_scatter)
            ax.set_title(f"{y_axis_scatter} vs {x_axis_scatter}")
            st.pyplot(fig)
        
    else:
        st.write("Please upload a CSV file.")

def main():
    upload_file()

if __name__ == "__main__":
    main()
