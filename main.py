
import streamlit as st
from ai.rl_agent import SignalAgent
from env.signal_env import SignalEnv
from database.db_handler import DBHandler
from database.vocab_utils import load_vocab
from utils.logger import log_signal

# 🔹 Initialize
st.set_page_config(page_title="Signal Game", page_icon="🎮")
st.title("🎮 Signal Game Interface")

agent = SignalAgent()
env = SignalEnv()
db = DBHandler()
vocab = load_vocab()
last_10 = db.fetch_last_logs()


# 🔹 Show Vocabulary
st.subheader("📘 Signal Vocabulary")
for emoji, meaning in vocab.items():
    st.write(f"{emoji} = {meaning}")

# 🔹 Step 1: Send Signal
st.subheader("🚀 Send Your Signal")
user_signal = st.text_input("Enter signal emoji (e.g., 🟥):")

if st.button("Send Signal"):
    if user_signal.strip() in vocab:
        state = env.receive_input(user_signal.strip())
        agent_response = agent.choose_action(state)

        st.success(f"✅ Agent says: {vocab[user_signal.strip()]}")
        st.session_state["last_signal"] = user_signal.strip()
        st.session_state["last_response"] = agent_response
    else:
        st.error("❌ Invalid signal! Please use a signal from the vocabulary above.")

# 🔹 Step 2: Give Feedback (only after signal is sent)
if "last_signal" in st.session_state and "last_response" in st.session_state:
    st.subheader("🗣️ Was the agent's response correct?")
    feedback = st.radio("Give Feedback:", ("👍 Yes", "👎 No"))

    if st.button("Submit Feedback"):
        reward = env.evaluate_response(feedback)
        agent.learn(
            st.session_state["last_signal"],
            st.session_state["last_response"],
            reward,
              # next_state = current state for now
        )

        db.log(
            st.session_state["last_signal"],
            st.session_state["last_response"],
            reward
        )

        log_signal(st.session_state["last_signal"], st.session_state["last_response"], reward)
        st.success(f"✅ Feedback submitted! " f" Agent learned with reward = {reward}")

        del st.session_state["last_signal"]
        del st.session_state["last_response"]

# 🔹 Game History
st.subheader("📜 Game History")
if st.button("Show Last 10 Rounds"):
    history = db.fetch_last_logs()
    if history:
        for i, log in enumerate(history, start=1):
            fb = "👍" if log['reward'] > 0 else "👎"
            st.write(f"{i}. {log['move']} → {log['result']} | Feedback: {fb}")
    else:
        st.info("No history found.")
