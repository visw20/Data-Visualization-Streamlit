import streamlit as st

st.title('Simple Streamlit App')
st.write('Hello, Streamlit!')

name = st.text_input('Enter your name:')
if name:
    st.write(f'Hello, {name}!')


