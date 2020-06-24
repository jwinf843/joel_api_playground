import requests
import json

poke_url = "https://pokeapi.co/api/v2/{group}/{ID}"

def get_pokemon(poke_id):
    url = poke_url.format(group = "pokemon", ID = poke_id)
    resp = requests.get(url)
    if not resp.ok:
        return "Something has gone awry"
    
    return resp.json()

def get_type(poke_id):
    results = []
    url = poke_url.format(group = "pokemon", ID = poke_id)
    resp = requests.get(url)
    if not resp.ok:
        return "Something has gone awry"
    
    pokemon = resp.json()
    for slot in pokemon['types']:
        results.append(slot['type']['name'])
    
    return results

def get_location(poke_id):
    results = []
    url = poke_url.format(group = 'pokemon', ID = poke_id)
    url += '/encounters'
    locations = requests.get(url)
    for location in locations.json():
        results.append(location['location_area']['name'])
    if not results:
        return ["This pokemon cannot be encountered in the wild"]
    return results

def create_pokedex(poke_url):
    running = True
    num = 0
    pokedex = []
    ''' LOGIC FOR GETTING ALL POKEMON '''
    while running:
        dictionary = {}
        num += 1
        try:
            url = poke_url.format(group = 'pokemon', ID = num)
#             print(url)
            pokemon = requests.get(url)
            poke_dict = pokemon.json()
            dictionary.setdefault('name', poke_dict['name'])
            dictionary.setdefault('number', num)
            dictionary.setdefault('locations', get_location(num))
            dictionary.setdefault('types', get_type(num))
            print(poke_dict['name'], num)
            pokedex.append(dictionary)    
        except:
            running = False

    print("Finished!")
    return pokedex
