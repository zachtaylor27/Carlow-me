import sqlite3

conn = sqlite3.connect("Q6.db")
cursor = conn.cursor()

with open("Q6.sql") as f:
    cursor.executescript(f.read())

cursor.execute("INSERT INTO pokemon_types (id, name) VALUES (?, ?)", (999, "unknown"))

conn.commit()
conn.close()