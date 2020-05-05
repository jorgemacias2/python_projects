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

def get_pk_type(type):
    pokemon_type = type["name"]
    return pokemon_type

def get_damage_from(type):
    damage_pk = type["damage_relations"]["double_damage_from"]
    damage_from = [sub["name"] for sub in damage_pk]
    return damage_from

def get_damage_to(type):
    damage_pk = type["damage_relations"]["double_damage_to"]
    damage_to = [sub["name"] for sub in damage_pk]
    return damage_to

def get_winner():
    if pk1_type_pk in pk2_damage_to or pk2_type_pk in pk1_damage_from:
        pokemon_winner = pk2_name_input
    elif pk2_type_pk in pk1_damage_to or pk1_type_pk in pk2_damage_from:
        pokemon_winner = pk1_name_input
    else:
        pokemon_winner = "Winner can't be determined"
    return pokemon_winner

pk1_name_input = input("Which is your first Pokemon choice: ")
pk1_choice = get_pokemon(pk1_name_input)
pk1_type_url = retrieve_type(pk1_choice)
pk1_type = get_type(pk1_type_url)
pk1_type_pk = get_pk_type(pk1_type)
pk1_damage_from = get_damage_from(pk1_type)
pk1_damage_to = get_damage_to(pk1_type)

print("First Pokemon type is: ", pk1_type_pk)
print("First Pokemon weakness is against: ", pk1_damage_from)
print("First Pokemon strength is against: ", pk1_damage_to)

pk2_name_input = input("Which is your second Pokemon choice: ")
pk2_choice = get_pokemon(pk2_name_input)
pk2_type_url = retrieve_type(pk2_choice)
pk2_type = get_type(pk2_type_url)
pk2_type_pk = get_pk_type(pk2_type)
pk2_damage_from = get_damage_from(pk2_type)
pk2_damage_to = get_damage_to(pk2_type)
print("Second Pokemon type is: ", pk2_type_pk)
print("Second Pokemon weakness is against: ", pk2_damage_from)
print("Second Pokemon strength is against: ", pk2_damage_to)

pk_winner = get_winner()
print("The winner is...: ", pk_winner)



