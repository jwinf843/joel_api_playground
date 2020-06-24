import json

def save_pokedex(pokedex, name):
    filename = "{}.txt".format(name)
    with open(filename, 'w') as outfile:
        json.dump(pokedex, outfile, indent=4)
        
def load_pokedex(file_name):
    filename = '{}.txt'.format(file_name)
    with open(filename) as json_file:
        pokdedex = json.load(json_file)
        return pokdedex

def get_pokemon_name_db(file_name, number):
    pokedex = load_pokedex(file_name)
    for pokemon in pokedex:
        if number == pokemon['number']:
            return pokemon['name']
        
    
def get_pokemon_number_db(file_name, name):
    pokedex = load_pokedex(file_name)
    for pokemon in pokedex:
        if name == pokemon['name']:
            return pokemon['number']

def get_location_db(file_name, ID):
    pokedex = load_pokedex(file_name)
    for pokemon in pokedex:
        if ID == pokemon['name'] or ID == pokemon['number']:
            return pokemon['locations']
        
def get_type_db(file_name, ID):
    pokedex = load_pokedex(file_name)
    for pokemon in pokedex:
        if ID == pokemon['name'] or ID == pokemon['number']:
            return pokemon['types']

''' 
bulbasaur = get_pokemon_db(1)
print(bulbasaur) # {
    name,
    number,
    locations,
}
'''