import streamlit as st
import yaml
import atexit  # ✅ Added to handle app shutdown
from db_handler import DBHandler

# Load config
with open("config.yaml", "r", encoding="utf-8") as f:
    config = yaml.safe_load(f)

# Page Setup
st.set_page_config(
    page_title=config["interface"]["page_title"],
    page_icon=config["interface"]["page_icon"],
    layout="centered"
)

# Custom Styles
st.markdown("""
    <style>
    body {
        background-color: #0e0e0e;
        color: #f1f1f1;
    }
    .block-container {
        padding: 2rem;
        background: radial-gradient(circle, #1c1c1c 0%, #000000 100%);
        border-radius: 10px;
    }
    .emoji-box {
        background-color: #141414;
        border-left: 5px solid #ff9100;
        padding: 12px;
        margin-bottom: 20px;
        font-size: 1.1rem;
        border-radius: 10px;
    }
    .signal-button {
        display: inline-block;
        padding: 10px 25px;
        background-color: #ff9100;
        color: white;
        font-weight: bold;
        border-radius: 10px;
        border: none;
        cursor: pointer;
        text-decoration: none;
        transition: all 0.3s ease-in-out;
        font-size: 16px;
        margin-top: 10px;
    }
    .signal-button:hover {
        background-color: #ff6500;
        transform: scale(1.05);
    }
    .history-box {
        background-color: #1a1a1a;
        padding: 1rem;
        border-radius: 8px;
        border: 1px solid #444;
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.title("🎮 Signal Game")

# Vocabulary
st.markdown("### 📘 Signal Vocabulary")
st.markdown("""
<div class='emoji-box'>
🟥 = **Danger** | 🟦 = **Safe** | 🔺 = **Move Up** | ⬛ = **Stop** | 🟨 = **Caution**
</div>
""", unsafe_allow_html=True)

# DB Init
db = DBHandler(config["database"]["path"])
atexit.register(db.close)  # ✅ Handles shutdown safely

signal_map = config["signals"]

# Gameplay Section
st.markdown("### 🚀 Send Your Signal")
col1, col2 = st.columns([4, 1])
with col1:
    user_signal = st.text_input("Enter signal emoji (e.g., 🟥):", key="signal_input")
with col2:
    if st.button("🎯 PLAY", use_container_width=True):
        if user_signal.strip():
            ai_response = signal_map.get(user_signal.strip(), "Unknown signal")
            reward = 1 if ai_response != "Unknown signal" else 0

            # Display AI response
            if reward:
                st.success(f"🧠 AI Response: **{ai_response}** 🏆 Reward: {reward}")
            else:
                st.error("🧠 AI Response: **Unknown signal** 🚫 Reward: 0")

            # Save to DB
            db.log(user_signal.strip(), ai_response, reward)

# Game History
if config["interface"]["enable_history"]:
    st.markdown("### 📜 Game History")
    logs = db.fetch_last_logs(config["interface"]["max_logs"])
    if logs:
        st.markdown("<div class='history-box'>", unsafe_allow_html=True)
        for entry in logs:
            st.markdown(f"**{entry['signal']}** → {entry['response']} | 🏆 Reward: {entry['reward']}")
        st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.info("No game history yet. Be the first to play!")

# Reset Button (Optional feature)
if st.button("🔁 Reset Game History"):
    db.cursor.execute("DELETE FROM game_logs")
    db.conn.commit()
    st.success("Game history has been cleared!")
