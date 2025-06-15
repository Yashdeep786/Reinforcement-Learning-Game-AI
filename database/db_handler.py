import sqlite3

 FOR-INTERFACE
class DBHandler:
    def __init__(self, db_path="game_ai.db"):
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
=======
DB_NAME = "game_ai.db"

class DBHandler:
    def __init__(self):
        self.conn = sqlite3.connect(DB_NAME, check_same_thread=False)
 main
        self.cursor = self.conn.cursor()
        self._init_table()

    def _init_table(self):
 FOR-INTERFACE
        self.cursor.execute("""
=======
        self.cursor.execute('''
main
            CREATE TABLE IF NOT EXISTS game_logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_signal TEXT,
                ai_response TEXT,
                reward INTEGER
            )
 FOR-INTERFACE
        """)

        ''')
main
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
