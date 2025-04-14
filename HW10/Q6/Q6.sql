CREATE TABLE pokemon_types (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE pokemon (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL UNIQUE,
    height REAL,
    weight REAL,
    base_experience INTEGER,
    type_id INTEGER DEFAULT 999,
    FOREIGN KEY (type_id) REFERENCES pokemon_types(id)
);