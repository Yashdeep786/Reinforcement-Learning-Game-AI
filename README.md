# Signal: The Emergent Language Game

An original interactive game where you and an AI communicate through signals — not words.

## 🚀 Project Features
- Human-AI signal communication
- Reinforcement learning agent
- Streamlit-based UI
- Emergent symbolic language system

## 🧠 How to Play
1. Enter a pattern (like 🔴🟡🔴)
2. AI replies with its pattern
3. Give feedback: Did it understand?
4. AI learns from your response

## 🤝 Contributions
PRs welcome for:
- Advanced RL models
- Dynamic mood engine
- Multiplayer mode

## 🧰 Requirements
- Python 3.8+
- streamlit

## ▶️ Run
```bash
streamlit run ui/app.py
```

## Signal Encoder/Decoder Module

- `encode(word)` → returns visual signal like 🟥
- `decode(signal)` → returns meaning like "danger"
- `update_vocab(signal, meaning)` → adds/updates vocabulary
- Automatically stores vocab in SQLite via db_handler

Used by agent and environment to interpret messages.
