import sqlite3

conn = sqlite3.connect("Q10.db")
cursor = conn.cursor()

with open("Q10.sql") as f:
    cursor.executescript(f.read())

try:
    data = {
        "id": int(input("ID: ")),
        "name": input("Name: "),
        "height": float(input("Height: ")),
        "weight": float(input("Weight: ")),
        "base_experience": int(input("Base Experience: "))
    }

    cursor.execute('''
        INSERT INTO pokemon (id, name, height, weight, base_experience)
        VALUES (:id, :name, :height, :weight, :base_experience)
    ''', data)
    conn.commit()
    print("✅ Pokémon inserted successfully!")

except Exception as e:
    print("❌ Failed to insert Pokémon:", e)

conn.close()