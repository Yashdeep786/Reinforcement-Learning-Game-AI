import streamlit as st
from ai.rl_agent import SignalAgent
from env.signal_env import SignalEnv

# Page title
st.title("🧠 Signal: The Emergent Language Game")

# Initialize agent and environment
agent = SignalAgent()
env = SignalEnv()

# Input: User sends a signal
user_pattern = st.text_input("Your Signal (e.g., 🔴🟡🔴):")

# --- Initialize session state ---
for key in ['last_state', 'last_response', 'show_feedback']:
    if key not in st.session_state:
        st.session_state[key] = None if key != 'show_feedback' else False

# --- Step 1: Send Signal ---
if st.button("Send Signal") and user_pattern.strip():
    state = env.receive_input(user_pattern.strip())
    ai_response = agent.choose_action(state)

    # Store in session for feedback step
    st.session_state['last_state'] = state
    st.session_state['last_response'] = ai_response
    st.session_state['show_feedback'] = True

# --- Step 2: Show AI Response and Collect Feedback ---
if st.session_state['show_feedback']:
    st.write(f"🤖 **AI Responds with:** `{st.session_state['last_response']}`")

    feedback = st.radio("Did AI understand you?", ('yes', 'no'), key="feedback")

    if st.button("Submit Feedback"):
        reward = env.evaluate_response(feedback)
        agent.learn(
            st.session_state['last_state'],
            st.session_state['last_response'],
            reward
        )
        st.success("✅ Feedback registered. AI is learning!")
        st.session_state['show_feedback'] = False

# --- Optional: View AI Memory ---
with st.expander("🧠 View Agent Memory"):
    st.write(agent.memory)

