import requests
import json
import os.path

def get_pokemon(pokemon_name):
    url = "https://pokeapi.co/api/v2/pokemon/{pk}".format(pk=pokemon_name)
    result = requests.get(url)
    pokemon = result.json()
    return pokemon

def retrieve_stats(pokemon):
    stats = pokemon["stats"]
    return stats

def get_type(pk_choice):
    types = pk_choice["types"]
    types_list = [sub["type"] for sub in types]
    type = []
    for type_element in types_list:
        if os.path.exists(type_element["name"]+".json"):
            with open(type_element["name"]+".json", "r") as file:
                file_result = json.loads(file.read())
                type.append(file_result)
        else:
            result = requests.get(type_element["url"])
            type1 = result.json()
            with open(type1["name"]+".json", "w") as file:
                file.write(json.dumps(type1))
            type.append(type1)
    return type

def get_pk_type(type_list):
    pokemon_type = []
    for type_element in type_list:
        pokemon_type1 = type_element["name"]
        pokemon_type.append(pokemon_type1)
    return pokemon_type

def get_damage_from(type):
    types_of_damages = ["double_damage_from", "half_damage_from", "no_damage_from"]
    damage_from1 = []
    for damages in types_of_damages:
        for type_damage in type:
            damage_pk1 = type_damage["damage_relations"][damages]
            damage_from1.append([sub["name"] for sub in damage_pk1])
        damage_from = []
        for x in damage_from1:
            for y in x:
                damage_from.append(y)
        if damages == "double_damage_from":
            double_damage_from = list(dict.fromkeys(damage_from))
        if damages == "half_damage_from":
            half_damage_from = list(dict.fromkeys(damage_from))
        if damages == "no_damage_from":
            no_damage_from = list(dict.fromkeys(damage_from))
        damage_from1 = []
    return (double_damage_from, half_damage_from, no_damage_from)

def get_damage_to(type):
    types_of_damages = ["double_damage_to", "half_damage_to", "no_damage_to"]
    damage_to1 = []
    for damages in types_of_damages:
        for type_damage in type:
            damage_pk1 = type_damage["damage_relations"][damages]
            damage_to1.append([sub["name"] for sub in damage_pk1])
        damage_to = []
        for x in damage_to1:
            for y in x:
                damage_to.append(y)
        if damages == "double_damage_to":
            double_damage_to = list(dict.fromkeys(damage_to))
        if damages == "half_damage_to":
            half_damage_to = list(dict.fromkeys(damage_to))
        if damages == "no_damage_to":
            no_damage_to = list(dict.fromkeys(damage_to))
        damage_to1 = []
    return (double_damage_to, half_damage_to, no_damage_to)

def get_points(pk1_data, pk2_data):
    pk_points = 0
    if any(x in pk1_data["pk_type_pk"] for x in pk2_data["pk_damage_to"]):
        pk_points = pk_points - 2
    if any(x in pk2_data["pk_type_pk"] for x in pk1_data["pk_damage_to"]):
        pk_points = pk_points + 2
    if any(x in pk1_data["pk_type_pk"] for x in pk2_data["pk_half_damage_to"]):
        pk_points = pk_points - 0.5
    if any(x in pk2_data["pk_type_pk"] for x in pk1_data["pk_half_damage_to"]):
        pk_points = pk_points + 0.5
    else:
        pk_points = pk_points + 0
    return pk_points

def get_winner(pk1_data, pk2_data):
    if any(x in pk1_data["pk_type_pk"] for x in pk2_data["pk_damage_to"]) and any(x in pk2_data["pk_type_pk"] for x in pk1_data["pk_damage_to"]):
        if pk1_data["pk_bs_avg"] > pk2_data["pk_bs_avg"]:
            pokemon_winner = pk1_name_input
        if pk2_data["pk_bs_avg"] > pk1_data["pk_bs_avg"]:
            pokemon_winner = pk2_name_input
        else:
            pokemon_winner = "Winner can't be determined"
    elif any(x in pk1_data["pk_type_pk"] for x in pk2_data["pk_damage_to"]):
        pokemon_winner = pk2_name_input
    elif any(x in pk2_data["pk_type_pk"] for x in pk1_data["pk_damage_to"]):
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
    pk_type = get_type(pk_choice)
    pk_type_pk = get_pk_type(pk_type)
    pk_damage_from = get_damage_from(pk_type)[0]
    pk_half_damage_from = get_damage_from(pk_type)[1]
    pk_damage_to = get_damage_to(pk_type)[0]
    pk_half_damage_to = get_damage_to(pk_type)[1]
    pk_no_damage_to = get_damage_to(pk_type)[2]
    pk_no_damage_from = get_damage_from(pk_type)[2]
    print("Pokemon type is: ", pk_type_pk)
    print("Pokemon strength is against: ", pk_damage_to)
    print("Pokemon half strength is against: ", pk_half_damage_to)
    print("Pokemon weakness is against: ", pk_damage_from)
    print("Pokemon half weakness is against", pk_half_damage_from)
    print("Pokemon makes zero damage against", pk_no_damage_to)
    print("Pokemon receives zero damage from", pk_no_damage_from)
    stat_list = retrieve_stats(pk_choice)
    pk_bs_avg = best_pk_stat(stat_list)
    return {"pk_damage_to":pk_damage_to, "pk_half_damage_to":pk_half_damage_to, "pk_no_damage_to":pk_no_damage_to, "pk_type_pk":pk_type_pk, "pk_bs_avg":pk_bs_avg}

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

pk_points = get_points(pk1_result, pk2_result)
if pk_points == 0:
    print("Points winner: Can't be determined")
elif pk_points > 0:
    print("Points winner: ", pk1_name_input, "with", pk_points, "points")
elif pk_points < 0:
    print("Points winner: ", pk2_name_input, "with", pk_points, "points")