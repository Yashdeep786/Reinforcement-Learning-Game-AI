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

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS game_logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                player_id TEXT,
                timestamp TEXT,
                action TEXT,
                result TEXT
            )
        """)

        self.conn.commit()


    def get_progress(self, player_id):
        cursor = self.conn.cursor()
        cursor.execute('''
            SELECT score, level, timestamp FROM player_progress
            WHERE player_id = ?
            ORDER BY timestamp DESC
            LIMIT 1
        ''', (player_id,))
        return cursor.fetchone()
    
    def fetch_last_logs(self, limit=10):
        cursor = self.conn.cursor()
        cursor.execute('''
            SELECT player_id, score, level, timestamp FROM player_progress
            ORDER BY timestamp DESC
            LIMIT ?
        ''', (limit,))
        return cursor.fetchall()

    def close(self):
        if self.conn:
            self.conn.close()

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
