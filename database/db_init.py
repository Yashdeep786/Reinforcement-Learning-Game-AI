import sqlite3

def init_db():
    conn = sqlite3.connect("game_ai.db")
    c = conn.cursor()

    # ✅ Create signal_vocab table
    c.execute('''
        CREATE TABLE IF NOT EXISTS signal_vocab (
            signal TEXT PRIMARY KEY,
            meaning TEXT
        )
    ''')

    # Add other tables here too if needed (like agent_policy, game_logs)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
