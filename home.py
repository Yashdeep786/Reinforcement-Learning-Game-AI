import streamlit as st

# Page Config
st.set_page_config(page_title="Signal Game - Arena", page_icon="🎮", layout="wide")

# Custom CSS
st.markdown("""
<style>
body {
    background: radial-gradient(circle, #1b2735, #090a0f);
    background-attachment: fixed;
    font-family: 'Segoe UI', sans-serif;
    color: white;
}

.stApp {
    background-color: transparent;
}

.header {
    padding: 2rem 0;
    text-align: center;
    font-size: 3rem;
    font-weight: bold;
    background: linear-gradient(90deg, #00ffe7, #ff6ec4);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    text-shadow: 0 0 25px #00eaff;
    animation: fadeIn 1s ease-in-out;
}

.game-container {
    background: rgba(0, 0, 0, 0.4);
    border-radius: 20px;
    padding: 3rem;
    margin: 2rem 10rem;
    box-shadow: 0 0 30px rgba(0, 255, 255, 0.2);
    backdrop-filter: blur(8px);
}

.signal-box {
    padding: 2rem;
    border: 2px dashed #00eaff;
    border-radius: 20px;
    text-align: center;
    font-size: 2rem;
    margin-bottom: 2rem;
    background: rgba(0, 0, 0, 0.3);
}

button {
    padding: 1rem 2rem;
    font-size: 1.5rem;
    font-weight: bold;
    color: white;
    background: linear-gradient(135deg, #ff6ec4, #7873f5);
    border: none;
    border-radius: 15px;
    cursor: pointer;
    transition: transform 0.3s, box-shadow 0.3s;
}

button:hover {
    transform: scale(1.05);
    box-shadow: 0 0 20px rgba(255, 110, 196, 0.6);
}

.score {
    font-size: 1.5rem;
    margin-top: 1rem;
    color: #cfcfcf;
}

@keyframes fadeIn {
    from { opacity: 0; transform: translateY(-20px); }
    to { opacity: 1; transform: translateY(0); }
}
</style>
""", unsafe_allow_html=True)

# Content
st.markdown('<div class="header">🎯 Signal Game Arena</div>', unsafe_allow_html=True)

st.markdown('<div class="game-container">', unsafe_allow_html=True)

# Signal placeholder (your actual game output here)
st.markdown('<div class="signal-box">🟢 🔴 🔵</div>', unsafe_allow_html=True)

# Input area (replace with your actual game input logic)
user_input = st.text_input("Enter your signal interpretation:", "")

if st.button("Submit Signal"):
    # Replace this logic with your real game function
    st.success(f"Your input '{user_input}' has been recorded!")

# Score display (replace with dynamic game data)
st.markdown('<div class="score">🌟 Current Score: 150</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
