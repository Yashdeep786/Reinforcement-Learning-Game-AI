# database/db_handler.py

import sqlite3

DB_NAME = "game_ai.db"

def save_vocab(vocab):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("DELETE FROM signal_vocab")  # clear old
    for signal, meaning in vocab.items():
        c.execute("INSERT INTO signal_vocab (signal, meaning) VALUES (?, ?)", (signal, meaning))
    conn.commit()
    conn.close()

def load_vocab():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT signal, meaning FROM signal_vocab")
    rows = c.fetchall()
    conn.close()
    return {signal: meaning for signal, meaning in rows}
