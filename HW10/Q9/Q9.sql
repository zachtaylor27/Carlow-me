SELECT pokemon.name, pokemon_types.name
FROM pokemon
JOIN pokemon_types ON pokemon.type_id = pokemon_types.id;