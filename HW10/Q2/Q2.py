import sqlite3
import csv

conn = sqlite3.connect("Q2.db")
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS pokemon (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL UNIQUE,
    height REAL,
    weight REAL,
    base_experience INTEGER
)
''')

with open("pokemon.csv", newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        cursor.execute('''
            INSERT OR IGNORE INTO pokemon (id, name, height, weight, base_experience)
            VALUES (?, ?, ?, ?, ?)
        ''', (row['id'], row['name'], row['height'], row['weight'], row['base_experience']))

conn.commit()
conn.close()