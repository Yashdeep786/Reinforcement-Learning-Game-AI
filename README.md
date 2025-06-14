# 🧠 Signal: The Emergent Language Game

An interactive reinforcement learning game where **humans and AI agents develop a shared nonverbal language** using emoji-based signals.

Built using Python, Streamlit, and SQLite — this project explores how communication can emerge from feedback-driven interaction.

---

## 🎮 Gameplay Overview

1. **Send a Signal** — Choose an emoji from the shared vocabulary (e.g., 🟥 for "danger").
2. **AI Responds** — The agent selects a response based on its memory and learning.
3. **Provide Feedback** — Tell the system whether the AI understood your message.
4. **Learning Happens** — Positive feedback reinforces correct interpretations.
5. **History Log** — View the last 10 rounds of interaction.

---

## 🛠️ Features

- ✅ Streamlit-based UI for real-time interaction
- ✅ Reinforcement learning agent with memory
- ✅ SQLite database for vocab and history
- ✅ Real-time feedback-based training loop
- ✅ Persistent vocabulary management
- ✅ Modular codebase (Agent, Env, DB, Logger, Utils)

---

## 🗂️ Project Structure

SignalGame/
├── ai/ # Reinforcement learning agent
│ └── rl_agent.py
├── env/ # Game environment logic
│ └── signal_env.py
├── database/ # Vocabulary + logging database
│ ├── db_handler.py
│ ├── db_init.py
│ └── vocab_utils.py
├── utils/ # Logging and encoding tools
│ ├── logger.py
│ └── signal_encoder.py
├── main.py # 🔥 Streamlit frontend interface
├── game_ai.db # (Auto-generated) SQLite database
└── README.md # 📘 