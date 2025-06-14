# database/db_handler.py

import sqlite3

class DBHandler:
    def __init__(self, db_name="game_ai.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def save_vocab(self, vocab):
        self.cursor.execute("DELETE FROM signal_vocab")
        for signal, meaning in vocab.items():
            self.cursor.execute("INSERT INTO signal_vocab (signal, meaning) VALUES (?, ?)", (signal, meaning))
        self.conn.commit()

    def load_vocab(self):
        self.cursor.execute("SELECT signal, meaning FROM signal_vocab")
        return dict(self.cursor.fetchall())

    def close(self):
        self.conn.close()
