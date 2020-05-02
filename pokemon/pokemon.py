import requests

def get_pokemon(pokemon_name):
    url = "https://pokeapi.co/api/v2/pokemon/{pk}".format(pk=pokemon_name)
    result = requests.get(url)
    pokemon = result.json()
    return pokemon

def retrieve_type(pokemon):
    types = pokemon["types"]
    type_url = types[0]["type"]["url"]
    return type_url

def get_type(type_url):
    result = requests.get(type_url)
    type = result.json()
    return type


pk1_name_input = input("Which is your first Pokemon choice: ")
pk2_name_input = input("Which is your second Pokemon choice: ")
pk1_choice = get_pokemon(pk1_name_input)
pk2_choice = get_pokemon(pk2_name_input)
print(pk1_choice)
pk1_type_url = retrieve_type(pk1_choice)
pk1_type = get_type(pk1_type_url)
print(pk1_type)

