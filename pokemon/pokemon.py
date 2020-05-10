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

def retrieve_stats(pokemon):
    stats = pokemon["stats"]
    return stats

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

def get_winner(pk1_data, pk2_data):
    if pk1_data["pk_type_pk"] in pk2_data["pk_damage_to"]:
        pokemon_winner = pk2_name_input
    elif pk2_data["pk_type_pk"] in pk1_data["pk_damage_to"]:
        pokemon_winner = pk1_name_input
    elif pk1_data["pk_bs_avg"] > pk2_data["pk_bs_avg"]:
        pokemon_winner = pk1_name_input
    elif pk2_data["pk_bs_avg"] > pk1_data["pk_bs_avg"]:
        pokemon_winner = pk2_name_input
    else:
        pokemon_winner = "Winner can't be determined"
    return pokemon_winner

def input_pokemon(pk_name_input):
    pk_choice = get_pokemon(pk_name_input)
    pk_type_url = retrieve_type(pk_choice)
    pk_type = get_type(pk_type_url)
    pk_type_pk = get_pk_type(pk_type)
    pk_damage_from = get_damage_from(pk_type)
    pk_damage_to = get_damage_to(pk_type)
    print("First Pokemon type is: ", pk_type_pk)
    print("First Pokemon weakness is against: ", pk_damage_from)
    print("First Pokemon strength is against: ", pk_damage_to)
    stat_list = retrieve_stats(pk_choice)
    pk_bs_avg = best_pk_stat(stat_list)
    return {"pk_damage_to":pk_damage_to, "pk_type_pk":pk_type_pk, "pk_bs_avg":pk_bs_avg}

def best_pk_stat(pk_stats):
    sum_base_stat = 0
    for stat in pk_stats:
        base_stat = stat["base_stat"]
        sum_base_stat = base_stat + sum_base_stat
    pk_avg = sum_base_stat / len(pk_stats)
    return pk_avg

pk1_name_input = input("Which is your first Pokemon choice: ")
pk1_result = input_pokemon(pk1_name_input)

pk2_name_input = input("Which is your second Pokemon choice: ")
pk2_result = input_pokemon(pk2_name_input)

pk_winner = get_winner(pk1_result, pk2_result)
print("The winner is...: ", pk_winner)




