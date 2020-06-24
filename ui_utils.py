from db_utils import *

def main_menu():
    pass

def get_pokemon_by_name():
    poke_name = input('What pokemon would you like to look up?\n    ').lower()
    pokedex = load_pokedex('pokedex file')
    for pokemon in pokedex:
        if poke_name in pokemon['name']:
            return pokemon
    
def get_pokemon_by_number():
    try:
        poke_number = int(input('What pokemon would you like to look up?\n    '))
        pokedex = load_pokedex('pokedex file')
        for pokemon in pokedex:
            if poke_number == pokemon['number']:
                return pokemon
    except:
        print('You must type in a number')
        pokemon = get_pokemon_by_number()
        return pokemon
    
def get_pokemon_by_type():
    type_list = ['Fire', 'Water', 'Grass', 'Eletric', 'Psychic', 'Steel', 'Normal', 'Fairy', 'Dark', 'Flying', 'Ghost', 'Poison', 'Ice', 'Ground', 'Rock', 'Dragon', 'Fighting', 'Bug']
    for index in range(3):
        print('     \t'.join(type_list[index * 6: index * 6 + 6]))
    results = []
    poke_type_1 = input('Please enter a type to search: \n\t').lower()
    
    pokedex = load_pokedex('pokedex file')
    for pokemon in pokedex:
        if poke_type_1 in pokemon['types']:
            results.append(pokemon)
            
    print([pokemon['name'].capitalize() for pokemon in results])
    'Figure out how to filter results by a second type input'
        
    
    
def display_pokemon(pokemon):
    name = pokemon['name'].capitalize()
    type_string = ' and '.join(pokemon['types'])
    pokemon_number = pokemon['number']
    loc_string = pokemon['locations'][0]
    if loc_string != "This pokemon cannot be encountered in the wild":
        loc_string = 'This pokemon can be found in {} different locations'.format(len(pokemon['locations']))
    
    
    output = '''    This is {name}!
    It is a {type_string} type Pokemon.
    It's Pokemon ID is {pokemon_number}.
    {loc_string}'''.format(
        name = name,
        type_string = type_string,
        pokemon_number = pokemon_number,
        loc_string = loc_string
    )

    return output

'''
Search Pokemon by name/number/location
When a pokemon is sought, display ALL info except:
    location. Instead display number of locations
    If you want more info, a secondary prompt
    will write out full locations
'''


rando = get_pokemon_by_type()
print(rando)