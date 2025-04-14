CREATE TABLE pokemon (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL UNIQUE,
    height REAL,
    weight REAL,
    base_experience INTEGER
);