import sqlite3

# Connect to SQLite database
conn = sqlite3.connect("signal_game.db")
cursor = conn.cursor()

# Create tables
cursor.execute('''
CREATE TABLE IF NOT EXISTS signal_vocab (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    emoji TEXT UNIQUE,
    meaning TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS agent_policy (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    state TEXT,
    action TEXT,
    q_value REAL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS game_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    move TEXT,
    result TEXT,
    reward INTEGER,
    round_number INTEGER
)
''')

# ✅ INSERT DUMMY VOCAB HERE — after cursor is defined
dummy_vocab = [
    ('🟥', 'danger'),
    ('🟦', 'safe'),
    ('🔺', 'move up'),
    ('⬛', 'help'),
    ('🟨', 'caution')
]

cursor.executemany('INSERT OR IGNORE INTO signal_vocab (emoji, meaning) VALUES (?, ?)', dummy_vocab)

conn.commit()
conn.close()

print("✅ Database and tables created successfully!")
