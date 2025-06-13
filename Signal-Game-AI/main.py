import streamlit as st
from ai.rl_agent import SignalAgent
from env.signal_env import SignalEnv
from database.db_handler import DBHandler  # NEW
from utils.logger import log_signal


st.title("🧠 Signal: The Emergent Language Game")

agent = SignalAgent()
env = SignalEnv()
db = DBHandler()  # NEW

user_pattern = st.text_input("Your Signal (e.g., 🔴🟡🔴):")
if st.button("Send Signal"):
    state = env.receive_input(user_pattern)
    ai_response = agent.choose_action(state)
    st.write(f"🤖 AI Responds with: {ai_response}")

    feedback = st.radio("Did AI understand you?", ('yes', 'no'))
    if st.button("Submit Feedback"):
        reward = env.evaluate_response(feedback)
        agent.learn(state, ai_response, reward)
        db.log(user_pattern, ai_response, reward)  # NEW
        st.success("Feedback registered. AI is learning!")
