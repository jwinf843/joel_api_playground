import requests
import json

from api_utils import get_type
from db_utils import load_pokedex, save_pokedex


def add_type(file):
    pokedex = load_pokedex(file)
    new_pokedex = pokedex.copy()
    for index, pokemon in enumerate(pokedex):
        ID = pokemon['number']
        pokemon_type = get_type(ID)
        
        new_pokedex[index].setdefault('types', pokemon_type)
        print(new_pokedex[index])
        
    save_pokedex(new_pokedex, file)
    print('Pokedex Successfully Created')
        
        
add_type('pokedex file')