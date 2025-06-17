import streamlit as st

# Page config
st.set_page_config(page_title="Signal Game Landing", page_icon="🚀", layout="centered")

# Google Font import
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@500;800&display=swap" rel="stylesheet">
""", unsafe_allow_html=True)

# Custom CSS
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
    background-attachment: fixed;
    font-family: 'Orbitron', sans-serif;
    color: white;
    overflow: hidden;
}

body::before {
    content: '';
    position: fixed;
    top: 0;
    left: 0;
    width: 200%;
    height: 200%;
    background: radial-gradient(circle at 50% 50%, rgba(255,255,255,0.05) 0%, transparent 40%);
    animation: moveBackground 60s linear infinite;
    z-index: -1;
}

@keyframes moveBackground {
    0% { transform: translate(0, 0); }
    100% { transform: translate(-50%, -50%); }
}

.stApp {
    animation: fadePage 1.2s ease-in-out;
}

@keyframes fadePage {
    0% { opacity: 0; transform: scale(1.05); }
    100% { opacity: 1; transform: scale(1); }
}

.main-box {
    padding: 4rem 2rem;
    border-radius: 20px;
    background: rgba(0, 0, 0, 0.5);
    backdrop-filter: blur(8px);
    text-align: center;
    margin-top: 6rem;
    box-shadow: 0 0 50px rgba(0, 255, 255, 0.4);
    border: 2px solid rgba(0, 255, 255, 0.5);
    animation: pulse 3s infinite;
}

@keyframes pulse {
    0% { box-shadow: 0 0 50px rgba(0, 255, 255, 0.4); }
    50% { box-shadow: 0 0 80px rgba(0, 255, 255, 0.8); }
    100% { box-shadow: 0 0 50px rgba(0, 255, 255, 0.4); }
}

.title {
    font-size: 4rem;
    font-weight: 800;
    background: linear-gradient(90deg, #00ffe7, #00c3ff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    text-shadow: 0 0 20px #00eaff;
}

.subtitle {
    font-size: 1.4rem;
    margin-top: 1rem;
    margin-bottom: 2.5rem;
    color: #cfcfcf;
}

.play-button {
    padding: 1.2rem 4rem;
    font-size: 1.5rem;
    font-weight: bold;
    color: white;
    background: linear-gradient(135deg, #ff6ec4, #7873f5);
    border: none;
    border-radius: 18px;
    cursor: pointer;
    transition: transform 0.3s, box-shadow 0.3s;
}

.play-button:hover {
    transform: scale(1.08);
    box-shadow: 0 0 30px rgba(255, 110, 196, 0.6);
}
</style>
""", unsafe_allow_html=True)

# Content
st.markdown("""
<div class="main-box">
    <div class="title">🚀 Welcome to Signal Game</div>
    <div class="subtitle">Crack the code. Talk in signals. Train your AI.</div>
    <form action="main.py">
        <button class="play-button" type="submit">🎮 Enter the Arena</button>
    </form>
</div>
""", unsafe_allow_html=True)
