# 🧱 Repository Structure - Signal: The Emergent Language Game

This document outlines the complete structure of the repository, including the purpose and functionality of each directory and file.

---

## 📁 Root Directory

| File/Folder         | Description                                                                 |
|---------------------|-----------------------------------------------------------------------------|
| `app.py`            | 🔌 Entry point that integrates all modules: Agent, Environment, Interface. |
| `rl_agent.py`       | 🧠 Contains the reinforcement learning logic for the agent.                 |
| `signal_env.py`     | 🌍 The game environment where interactions and episodes take place.         |
| `README.md`         | 📘 Overview, installation, usage, and contribution instructions.            |
| `CONTRIBUTING.md`   | 🤝 Contribution guidelines for collaborators.                               |
| `requirements.txt`  | 📦 Python dependencies to install via pip.                                  |
| `game_ai.db`        | 🗃️ SQLite database storing learning episodes and signal mappings.           |
| `feature_request.md`| 💡 Template for feature suggestions.                                        |
| `bug_report.md`     | 🐞 Template for reporting issues.                                           |
| `LICENSE`           | ⚖️ Open-source license file.                                                |

---

## 📁 database/

| File                | Description                                                                 |
|---------------------|-----------------------------------------------------------------------------|
| `db_handler.py`     | 📂 Functions to read/write agent learning data and signals to the database. |

---

## 📁 utils/

| File                | Description                                                                 |
|---------------------|-----------------------------------------------------------------------------|
| `encoder.py`        | 🔡 Utilities for encoding/decoding signals (e.g., emojis or patterns).      |
| `logger.py`         | 📊 Optional: custom logging setup.                                          |

---

## 📁 tests/

| File                | Description                                                                 |
|---------------------|-----------------------------------------------------------------------------|
| `test_agent.py`     | ✅ Unit tests for the Agent logic and behavior.                             |
| `test_db_link.py`   | ✅ Tests for database operations and storage integrity.                     |
| `test_encoder.py`   | ✅ Tests for encoding/decoding logic.                                       |

---

## 🔁 Flow Overview

User (Player) ─▶ Interface (Frontend)
└▶ app.py ─▶ rl_agent.py (decision-making)
└▶ signal_env.py (rules + rewards)
└▶ database/ (save learning data)
└▶ utils/ (encode signals)
