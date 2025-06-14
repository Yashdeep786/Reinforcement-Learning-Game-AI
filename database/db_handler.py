# database/db_handler.py

import sqlite3

class DBHandler:
    def __init__(self, db_name="signal_game.db"):
        self.db_name = db_name
        self._init_db()

    def _get_connection(self):
        return sqlite3.connect(self.db_name)

    def _init_db(self):
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS game_logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                move TEXT,
                result TEXT,
                reward INTEGER
            )
        ''')
        conn.commit()
        conn.close()

    def log(self, move, result, reward):
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO game_logs (move, result, reward)
            VALUES (?, ?, ?)
        ''', (move, result, reward))
        conn.commit()
        conn.close()

    def fetch_last_logs(self, limit=10):
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute('''
                       SELECT move, result, reward
                       FROM game_logs
                       ORDER BY id DESC LIMIT ?
                       ''', (limit,))
        rows = cursor.fetchall()
        conn.close()
        return [
            {"round": idx + 1, "move": row[0], "result": row[1], "reward": row[2]}
            for idx, row in enumerate(reversed(rows))
        ]
