import streamlit as st

st.header("This is a button")

if st.button("Say Hello"):
    st.write("Hello All!!")
else: 
    st.write("Goodbye")