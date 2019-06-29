import requests

poke_url = "https://pokeapi.co/api/v2/{group}/{ID}"

def get_pokemon(poke_id):
    url = poke_url.format(group = "pokemon", ID = poke_id)
    resp = requests.get(url)
    if not resp.ok:
        return "Something has gone awry"
    
    return resp.json()

def get_location(poke_id):
    results = []
    url = poke_url.format(group = 'pokemon', ID = poke_id)
    url += '/encounters'
    locations = requests.get(url)
    if not locations:
        return ["This pokemon cannot be encountered in the wild"]
    for location in locations.json():
        results.append(location['location_area']['name'])
    
    return results
    
# mew = get_pokemon(151)

# print(mew.keys())
# print(mew['location_area_encounters'])

pidgey = get_pokemon(16)
pidgey_loc = get_location(16)

print(pidgey_loc)
    
# print(pidgey['types'])

# print(pidgey.keys())
# print(pidgey['name'])
# print(pidgey['is_default'])
print('**************************')


# for num in range(1, 807):
#     url = poke_url.format(group = 'pokemon', ID = num)
#     pokemon = requests.get(url).json()
#     if pokemon['is_default'] == 'False':
#         print(pokemon['name'])

running = True
num = 0
pokedex = []
''' LOGIC FOR GETTING ALL POKEMON '''
while running:
    dictionary = {}
    num += 1
    try:
        url = poke_url.format(group = 'pokemon', ID = num)
        print(url)
        pokemon = requests.get(url)
        poke_dict = pokemon.json()
        dictionary.setdefault('name', poke_dict['name'])
        dictionary.setdefault('locations', get_location(num))
        
#         if pokemon['is_default'] == 'False':
#             print(pokemon['name'])
        print(poke_dict['name'])
        pokedex.append(dictionary)    
    except:
        running = False

print("Finished!")



'''
[
    {
        'name': pokemon['name']
        'locations': [
            ...all location names...
        ]
        'types': [
            ...all applicable types...
        ]
        'image': 'front facing img url'
    }
]

'''