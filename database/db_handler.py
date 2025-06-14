import sqlite3

class DBHandler:
    def __init__(self, db_path="game_ai.db"):
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self.cursor = self.conn.cursor()
        self._init_table()

    def _init_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS game_logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_signal TEXT,
                ai_response TEXT,
                reward INTEGER
            )
        """)
        self.conn.commit()

    def log(self, user_signal, ai_response, reward):
        self.cursor.execute(
            "INSERT INTO game_logs (user_signal, ai_response, reward) VALUES (?, ?, ?)",
            (user_signal, ai_response, reward)
        )
        self.conn.commit()

    def fetch_last_logs(self, limit=10):
        self.cursor.execute(
            "SELECT user_signal, ai_response, reward FROM game_logs ORDER BY id DESC LIMIT ?",
            (limit,)
        )
        rows = self.cursor.fetchall()
        return [{"move": signal, "result": response, "reward": reward} for signal, response, reward in rows]

    def close(self):
        self.conn.close()
