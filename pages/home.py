import streamlit as st

# Page config
st.set_page_config(page_title="Signal Game Landing", page_icon="🚀", layout="centered")

# Custom CSS
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
    background-attachment: fixed;
    font-family: 'Segoe UI', sans-serif;
    color: white;
}

.stApp {
    background-color: transparent;
}

.main-box {
    padding: 4rem 2rem;
    border-radius: 20px;
    background: rgba(0, 0, 0, 0.5);
    backdrop-filter: blur(8px);
    text-align: center;
    margin-top: 6rem;
    box-shadow: 0 0 25px rgba(0, 255, 255, 0.2);
    animation: fadeIn 1s ease-in-out;
}

.title {
    font-size: 4rem;
    font-weight: bold;
    background: linear-gradient(90deg, #00ffe7, #00c3ff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    text-shadow: 0 0 20px #00eaff;
}

.subtitle {
    font-size: 1.3rem;
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

@keyframes fadeIn {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
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
