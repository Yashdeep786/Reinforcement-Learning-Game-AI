import streamlit as st
from utils.db_handler import DBHandler

db = DBHandler()

st.title("Player Profile")

username = st.text_input("Enter your username")

if st.button("Load Profile"):
    if username:
        db.add_player(username)
        level_score = db.get_player(username)
        if level_score:
            level, score = level_score
            st.write(f"Level: {level}")
            st.write(f"Score: {score}")
        else:
            st.write("New player profile created!")
    else:
        st.warning("Please enter a username.")
