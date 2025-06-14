import os
import sys
import streamlit as st
from ai.rl_agent import SignalAgent
from env.signal_env import SignalEnv
from database.vocab_utils import save_vocab, load_vocab, ensure_vocab_table
from database.db_handler import DBHandler
from utils.logger import log_signal

st.title("🧠 Signal: The Emergent Language Game")

agent = SignalAgent()
env = SignalEnv()
ensure_vocab_table()
db = DBHandler()
agent.vocab = load_vocab()

user_pattern = st.text_input("Your Signal (e.g., 🔴🟡🔴):")
if st.button("Send Signal"):
    state = env.receive_input(user_pattern)
    ai_response = agent.choose_action(state)
    st.write(f"🤖 AI Responds with: {ai_response}")

    feedback = st.radio("Did AI understand you?", ('yes', 'no'))
    if st.button("Submit Feedback"):
        reward = env.evaluate_response(feedback)
        agent.learn(state, ai_response, reward)
        db.log(user_pattern, ai_response, reward)
        save_vocab(agent.vocab)
        log_signal(user_pattern, ai_response, reward)
        st.success("Feedback registered. AI is learning!")

# Optional: show session history
if 'history' not in st.session_state:
    st.session_state['history'] = []

if user_pattern and st.button("Track History"):
    st.session_state['history'].append((user_pattern, ai_response, reward))

with st.expander("📜 Session History"):
    for i, (us, ai, rw) in enumerate(st.session_state['history']):
        st.write(f"{i+1}. You: {us} → AI: {ai} | Reward: {rw}")
