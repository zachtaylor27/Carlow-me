import sqlite3
import csv

conn = sqlite3.connect("Q8.db")
cursor = conn.cursor()

cursor.execute("DELETE FROM pokemon WHERE id > 50")

# Build a type mapping from name to id
type_map = {}
with open("pokemon_types.csv", newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        type_map[row['pokemon_id']] = int(row['type_id'])

for pid, tid in type_map.items():
    cursor.execute("UPDATE pokemon SET type_id = ? WHERE id = ?", (tid, pid))

conn.commit()
conn.close()