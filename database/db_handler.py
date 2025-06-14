import sqlite3

DB_NAME = "game_ai.db"

class DBHandler:
    def __init__(self):
        self.conn = sqlite3.connect(DB_NAME, check_same_thread=False)
        self.cursor = self.conn.cursor()
        self._init_table()

    def _init_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS game_logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_signal TEXT,
                ai_response TEXT,
                reward INTEGER
            )
        ''')
        self.conn.commit()

    def log(self, user_signal, ai_response, reward):
        self.cursor.execute(
            "INSERT INTO game_logs (user_signal, ai_response, reward) VALUES (?, ?, ?)",
            (user_signal, ai_response, reward)
        )
        self.conn.commit()

    def close(self):
        self.conn.close()
