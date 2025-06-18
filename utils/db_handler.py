import sqlite3

class DBHandler:
    def __init__(self, db_path="game_ai.db"):
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.init_tables()

    def init_tables(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS player_progress (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE,
                level INTEGER DEFAULT 1,
                score INTEGER DEFAULT 0
            )
        """)
        self.conn.commit()

    def add_player(self, username):
        try:
            self.cursor.execute("INSERT INTO player_progress (username) VALUES (?)", (username,))
            self.conn.commit()
        except sqlite3.IntegrityError:
            pass  # User already exists

    def get_player(self, username):
        self.cursor.execute("SELECT level, score FROM player_progress WHERE username=?", (username,))
        return self.cursor.fetchone()

    def update_progress(self, username, level, score):
        self.cursor.execute("""
            UPDATE player_progress
            SET level=?, score=?
            WHERE username=?
        """, (level, score, username))
        self.conn.commit()
