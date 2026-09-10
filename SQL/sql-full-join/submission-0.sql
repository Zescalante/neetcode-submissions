CREATE TABLE pokemon_types (
    id INTEGER PRIMARY KEY,
    name TEXT,
    weakness TEXT
);

CREATE TABLE pokemon (
    id INTEGER PRIMARY KEY,
    name TEXT,
    type_id INTEGER
);

INSERT INTO pokemon_types (id, name, weakness) VALUES
(1, 'Fire', 'Water'),
(2, 'Water', 'Grass'),
(3, 'Grass', 'Fire'),
(4, 'Electric', 'Ground');

INSERT INTO pokemon (id, name, type_id) VALUES
(4, 'Charmander', 1),
(7, 'Squirtle', 2),
(3, 'Bulbasaur', 3),
(147, 'Dratini', 6),
(65, 'Alakazam', 7);
-- Do not modify above this line. --
SELECT
    T.name AS type,
    P.name AS pokemon,
    T.weakness
FROM pokemon P
FULL JOIN pokemon_types T ON P.type_id = T.id
ORDER BY type ASC;





