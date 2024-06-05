import streamlit as st

def main():
    st.title("Simple User Input Checker")

    # Text input widget
    user_input = st.text_input("Enter some text:")

    # Check if user input is not empty
    if user_input:
        st.write("You entered:", user_input)
    else:
        st.write("Please enter some text.")

if __name__ == "__main__":
    main()

