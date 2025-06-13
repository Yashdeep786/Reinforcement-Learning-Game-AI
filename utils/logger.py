# utils/logger.py

from datetime import datetime

def log_signal(user_signal, ai_response, reward):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{now}] User: {user_signal} | AI: {ai_response} | Reward: {reward}")
