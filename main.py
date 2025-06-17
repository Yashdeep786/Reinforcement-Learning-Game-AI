import streamlit as st
import yaml
import atexit
from db_handler import DBHandler

# Load config
with open("config.yaml", "r", encoding="utf-8") as f:
    config = yaml.safe_load(f)

# Page Setup
st.set_page_config(
    page_title=config["interface"]["page_title"],
    page_icon=config["interface"]["page_icon"],
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom Styles - Modern Cyberpunk Theme
st.markdown("""
    <style>
    :root {
        --primary: #ff7700;
        --secondary: #00aaff;
        --dark: #0a0a12;
        --darker: #050508;
        --card: rgba(20, 20, 30, 0.7);
        --success: #00cc88;
        --danger: #ff5555;
    }
    
    * {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    body {
        background: linear-gradient(135deg, var(--darker), #1a0a2e);
        color: #f0f0f0;
        background-attachment: fixed;
    }
    
    .stApp {
        background: transparent !important;
    }
    
    .block-container {
        max-width: 800px;
        padding: 2rem 1.5rem;
        backdrop-filter: blur(10px);
        background: var(--card);
        border-radius: 16px;
        border: 1px solid rgba(255, 119, 0, 0.2);
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
        margin-top: 2rem;
    }
    
    h1 {
        text-align: center;
        font-size: 2.8rem;
        background: linear-gradient(90deg, var(--primary), var(--secondary));
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
        text-shadow: 0 0 15px rgba(255, 119, 0, 0.3);
    }
    
    h3 {
        border-bottom: 2px solid var(--primary);
        padding-bottom: 8px;
        margin-top: 1.5rem;
    }
    
    .signal-card {
        display: flex;
        flex-direction: column;
        background: rgba(10, 15, 30, 0.8);
        border-radius: 12px;
        padding: 1.5rem;
        margin: 1.2rem 0;
        border: 1px solid rgba(0, 170, 255, 0.3);
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.25);
    }
    
    .signal-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(120px, 1fr));
        gap: 15px;
        margin: 1rem 0;
    }
    
    .signal-item {
        background: rgba(30, 30, 50, 0.7);
        border-radius: 10px;
        padding: 12px;
        text-align: center;
        transition: all 0.3s ease;
        border: 1px solid rgba(255, 119, 0, 0.1);
    }
    
    .signal-item:hover {
        transform: translateY(-5px);
        box-shadow: 0 5px 15px rgba(255, 119, 0, 0.2);
        border-color: rgba(255, 119, 0, 0.4);
    }
    
    .signal-emoji {
        font-size: 2.5rem;
        margin-bottom: 8px;
    }
    
    .signal-input {
        background: rgba(20, 25, 40, 0.7) !important;
        color: white !important;
        border: 1px solid rgba(0, 170, 255, 0.4) !important;
        padding: 12px 15px !important;
        border-radius: 12px !important;
        font-size: 1.2rem !important;
    }
    
    .signal-input:focus {
        border-color: var(--primary) !important;
        box-shadow: 0 0 0 2px rgba(255, 119, 0, 0.3) !important;
    }
    
    .play-btn {
        background: linear-gradient(45deg, var(--primary), #ff5500) !important;
        border: none !important;
        color: white !important;
        padding: 12px 0 !important;
        font-size: 1.1rem !important;
        font-weight: 600 !important;
        border-radius: 12px !important;
        transition: all 0.3s !important;
        height: 100%;
    }
    
    .play-btn:hover {
        transform: scale(1.05);
        box-shadow: 0 0 20px rgba(255, 119, 0, 0.4);
    }
    
    .response-card {
        padding: 1.2rem;
        border-radius: 12px;
        margin: 1.5rem 0;
        text-align: center;
        font-size: 1.3rem;
        font-weight: 500;
        border: 1px solid;
        background: rgba(20, 20, 30, 0.9);
    }
    
    .success-card {
        border-color: var(--success);
        color: var(--success);
        box-shadow: 0 0 15px rgba(0, 204, 136, 0.2);
    }
    
    .error-card {
        border-color: var(--danger);
        color: var(--danger);
        box-shadow: 0 0 15px rgba(255, 85, 85, 0.2);
    }
    
    .history-item {
        padding: 1rem;
        margin: 0.8rem 0;
        border-radius: 10px;
        background: rgba(25, 30, 50, 0.7);
        border-left: 4px solid var(--primary);
    }
    
    .reset-btn {
        background: transparent !important;
        border: 1px solid var(--danger) !important;
        color: var(--danger) !important;
        transition: all 0.3s !important;
    }
    
    .reset-btn:hover {
        background: rgba(255, 85, 85, 0.1) !important;
    }
    
    .pulse {
        animation: pulse 2s infinite;
    }
    
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.05); }
        100% { transform: scale(1); }
    }
    </style>
""", unsafe_allow_html=True)

# Title with animated gradient
st.markdown("<h1>🚀 SIGNAL GAME</h1>", unsafe_allow_html=True)

# DB Init
db = DBHandler(config["database"]["path"])
atexit.register(db.close)
signal_map = config["signals"]

# Game Introduction
st.markdown("""
<div style='text-align:center; margin-bottom:1.5rem;'>
    <p style='font-size:1.1rem;'>
        Decrypt the signals and communicate with the AI system. Master the language of emojis!
    </p>
</div>
""", unsafe_allow_html=True)

# Vocabulary Section
st.markdown("### 🔍 SIGNAL DICTIONARY")
with st.container():
    st.markdown("<div class='signal-grid'>", unsafe_allow_html=True)
    
    signals = [
        {"emoji": "🟥", "meaning": "DANGER"},
        {"emoji": "🟦", "meaning": "SAFE"},
        {"emoji": "🔺", "meaning": "MOVE UP"},
        {"emoji": "⬛", "meaning": "STOP"},
        {"emoji": "🟨", "meaning": "CAUTION"},
        {"emoji": "🟩", "meaning": "GO"},
        {"emoji": "🔄", "meaning": "RETREAT"},
        {"emoji": "💡", "meaning": "IDEA"}
    ]
    
    for signal in signals:
        st.markdown(f"""
        <div class='signal-item pulse'>
            <div class='signal-emoji'>{signal['emoji']}</div>
            <div><strong>{signal['meaning']}</strong></div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)

# Gameplay Section
st.markdown("### 💬 TRANSMISSION CONSOLE")
with st.container():
    st.markdown("<div class='signal-card'>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([3, 1])
    with col1:
        user_signal = st.text_input(
            "Enter signal emoji:",
            key="signal_input",
            placeholder="🟥 🟦 🔺 ...",
            label_visibility="collapsed"
        )
    with col2:
        st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)
        play_btn = st.button("🚀 TRANSMIT", use_container_width=True, key="play_btn")
    
    st.markdown("</div>", unsafe_allow_html=True)

# Response Area
response_container = st.empty()

# Game History
if config["interface"]["enable_history"]:
    st.markdown("### 📜 COMMUNICATION LOG")
    logs = db.fetch_last_logs(config["interface"]["max_logs"])
    
    if logs:
        history_container = st.container()
        with history_container:
            for entry in logs:
                reward_class = "var(--success)" if entry['reward'] else "var(--danger)"
                st.markdown(f"""
                <div class='history-item'>
                    <div style="display:flex; justify-content:space-between;">
                        <div><strong>{entry['signal']}</strong> → {entry['response']}</div>
                        <div style='color:{reward_class};'>🏆 {entry['reward']}</div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
    else:
        st.info("📡 No transmissions yet. Initiate first contact!")

# Response Handling
if play_btn and user_signal.strip():
    ai_response = signal_map.get(user_signal.strip(), "Unknown signal")
    reward = 1 if ai_response != "Unknown signal" else 0
    
    # Save to DB
    db.log(user_signal.strip(), ai_response, reward)
    
    # Display response
    if reward:
        response_container.markdown(f"""
        <div class='response-card success-card'>
            <div style='font-size:2rem;'>🧠 AI RESPONSE</div>
            <div style='font-size:1.8rem; margin:15px 0;'>{ai_response}</div>
            <div>🏆 REWARD RECEIVED: {reward}</div>
        </div>
        """, unsafe_allow_html=True)
    else:
        response_container.markdown(f"""
        <div class='response-card error-card'>
            <div style='font-size:2rem;'>⚠️ DECRYPTION FAILED</div>
            <div style='font-size:1.5rem; margin:15px 0;'>Unknown signal pattern</div>
            <div>🚫 REWARD: 0</div>
        </div>
        """, unsafe_allow_html=True)
    
   

# Reset Button
st.markdown("---")
col_reset, _ = st.columns([1, 3])
with col_reset:
    if st.button("🔄 RESET LOGS", use_container_width=True, key="reset_btn", 
                help="Permanently clear all transmission records"):
        db.cursor.execute("DELETE FROM game_logs")
        db.conn.commit()
        st.success("All logs purged!")
        if config["interface"]["enable_history"]:
            st.experimental_rerun()

# Footer
st.markdown("""
<div style='text-align:center; margin-top:2rem; color:#aaa; font-size:0.9rem;'>
    System Status: <span style='color:var(--success);'>ONLINE</span> | v1.2.0
</div>
""", unsafe_allow_html=True)
