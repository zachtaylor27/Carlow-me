import sqlite3
import csv

conn = sqlite3.connect("Q4.db")
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS pokemon_types")
cursor.execute('''
CREATE TABLE pokemon_types (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
)
''')

with open("pokemon_type_names.csv", newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row['local_language_id'] == '9':
            cursor.execute('''
                INSERT OR IGNORE INTO pokemon_types (id, name)
                VALUES (?, ?)
            ''', (row['type_id'], row['name']))

conn.commit()
conn.close()