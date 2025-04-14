CREATE TABLE pokemon (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL UNIQUE,
    height REAL CHECK(height > 1),
    weight REAL CHECK(weight < 1000),
    base_experience INTEGER
);