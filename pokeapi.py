import requests

poke_url = "https://pokapi.co/api/v2/{group}/{ID}"

def get_pokemon(poke_id):
    url = poke_url.format(group = "pokemon", ID = poke_id)