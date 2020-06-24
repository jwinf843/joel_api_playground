import requests
import json
from api_utils import poke_url, create_pokedex, get_location, get_type
from db_utils import get_pokemon_name_db, get_pokemon_number_db, get_location_db, get_type_db
from pprint import pprint


bulbasaur = get_type(1)
# pprint(bulbasaur['types'])
print(bulbasaur)

charmander = get_type(4)
# pprint(charmander['types'])
print(charmander)
