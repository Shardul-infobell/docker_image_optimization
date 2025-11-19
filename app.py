import streamlit as st

st.title("Greeting App")

name = st.text_input("Enter your name:")

if name:
    st.success(f"Hello {name}, Good morning! I hope you are doing well!")

else:
    st.warning("Please enter your name.")