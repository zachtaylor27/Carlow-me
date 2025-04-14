import sqlite3
import csv

conn = sqlite3.connect("Q7.db")
cursor = conn.cursor()

with open("pokemon.csv", newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        cursor.execute('''
            INSERT OR IGNORE INTO pokemon (id, name, height, weight, base_experience, type_id)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (row['id'], row['name'], row['height'], row['weight'], row['base_experience'], 999))

conn.commit()
conn.close()