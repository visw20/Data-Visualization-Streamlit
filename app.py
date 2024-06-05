import streamlit as st

def main():
    st.title("Simple User Input Checker")

    # Text input widget
    user_input = st.text_input("Enter some text:")

    # Store user input in session state
    if user_input:
        st.session_state.user_input = user_input

    # Check if user input is stored in session state and display it
    if 'user_input' in st.session_state:
        st.write("Stored input:", st.session_state.user_input)
    else:
        st.write("Please enter some text.")

if __name__ == "__main__":
    main()


