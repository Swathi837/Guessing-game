import streamlit as st
import random

st.title("Guess the Number 🎯")

if "number" not in st.session_state:
    st.session_state.number = random.randint(1, 100)

guess = st.number_input("Your guess:", min_value=1, max_value=100, step=1)

if st.button("Check"):
    if guess == st.session_state.number:
        st.success("🎉 Correct! Restart to play again.")
    elif guess < st.session_state.number:
        st.warning("Higher!")
    else:
        st.warning("Lower!")