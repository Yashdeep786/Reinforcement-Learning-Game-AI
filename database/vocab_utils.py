import sqlite3

DB_NAME = "game_ai.db"

def ensure_vocab_table():
    conn = sqlite3.connect(DB_NAME)
    conn.execute('''
        CREATE TABLE IF NOT EXISTS signal_vocab (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            signal TEXT UNIQUE,
            meaning TEXT
        )
    ''')
    conn.commit()
    conn.close()

def save_vocab(vocab):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("DELETE FROM signal_vocab")
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
