import streamlit as st

def main():
    st.title("Simple User Input Checker")

    # Text input widget
    user_input = st.text_input("Enter your name:")

    # Store user input in session state
    if user_input:
        st.session_state.user_input = user_input

    # Check if user input is stored in session state and display a greeting
    if 'user_input' in st.session_state:
        if st.session_state.user_input.lower() == "viswa":
            st.write(f"Hello, {st.session_state.user_input.capitalize()}!")
        else:
            st.write(f"Hello, {st.session_state.user_input}!")
    else:
        st.write("Please enter your name.")

if __name__ == "__main__":
    main()

