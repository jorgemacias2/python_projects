import requests


def get_pokemon(pokemon_name):
    url = "https://pokeapi.co/api/v2/pokemon/{pk}".format(pk=pokemon_name)
    result = requests.get(url)
    pokemon = result.json()
    return pokemon


def retrieve_types(pokemon):
    types = pokemon["types"]
    types_url = [sub["type"]["url"] for sub in types]
    types_fetched = []
    for type_url in types_url:
        result = requests.get(type_url)
        type_fetched = result.json()
        types_fetched.append(type_fetched)
    return types_fetched


def retrieve_stats(pokemon):
    stats = pokemon["stats"]
    return stats


def best_pk_stat(pk_stats):
    sum_base_stat = 0
    for stat in pk_stats:
        base_stat = stat["base_stat"]
        sum_base_stat = base_stat + sum_base_stat
    pk_avg = sum_base_stat / len(pk_stats)
    return pk_avg


def get_damage_relations(types):
    damage_relations = {"double_damage_to": [], "half_damage_from": [], "no_damage_from": []}
    damage_relations_lists = [type_pk["damage_relations"] for type_pk in types]
    for damage_relation in damage_relations_lists:
        damage_relations["double_damage_to"] += damage_relation["double_damage_to"]
        damage_relations["half_damage_from"] += damage_relation["half_damage_from"]
        damage_relations["no_damage_from"] += damage_relation["no_damage_from"]
    return damage_relations


def remove_duplicates(mylist):
    return list(dict.fromkeys(mylist))


def input_pokemon(name_input):
    choice = get_pokemon(name_input)
    types = retrieve_types(choice)
    types_name = [type_pk["name"] for type_pk in types]
    damage_relations = get_damage_relations(types)
    double_damage_to = remove_duplicates([double_damage_to["name"] for double_damage_to in damage_relations["double_damage_to"]])
    half_damage_from = remove_duplicates([half_damage_from["name"] for half_damage_from in damage_relations["half_damage_from"]])
    no_damage_from = remove_duplicates([no_damage_from["name"] for no_damage_from in damage_relations["no_damage_from"]])
    print("Pokemon types are: ", types_name)
    print("Pokemon double damage to: ", double_damage_to)
    print("Pokemon half damage from: ", half_damage_from)
    print("Pokemon no damage from: ", no_damage_from)
    stat_list = retrieve_stats(choice)
    bs_avg = best_pk_stat(stat_list)
    return {
        "name": choice["name"],
        "double_damage_to": double_damage_to,
        "half_damage_from": half_damage_from,
        "no_damage_from": no_damage_from,
        "types_name": types_name,
        "bs_avg": bs_avg
    }


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


def check_types(types_name, types_against):
    count = 0
    for pk_type in types_name:
        if pk_type in types_against["double_damage_to"]:
            count += 1
        if pk_type in types_against["half_damage_from"]:
            count += 1
        if pk_type in types_against["no_damage_from"]:
            count += 4
    return count


def find_winner(pk1_data, pk2_data):
    count = 0
    count += check_types(pk1_data["types_name"], pk2_data)
    count -= check_types(pk2_data["types_name"], pk1_data)
    if count != 0:
        return pk2_data if count > 0 else pk1_data
    elif pk1_data["bs_avg"] != pk2_data["bs_avg"]:
        return pk1_data if pk1_data["bs_avg"] > pk2_data["bs_avg"] else pk2_data
    else:
        return None


pk1_name_input = input("Which is your first Pokemon choice: ")
pk1_result = input_pokemon(pk1_name_input)

pk2_name_input = input("Which is your second Pokemon choice: ")
pk2_result = input_pokemon(pk2_name_input)

pk_winner = find_winner(pk1_result, pk2_result)
print("The winner is...: ", pk_winner["name"])

#pk_winner = get_winner(pk1_result, pk2_result)
#print("The winner is...: ", pk_winner)

#pk_points = get_points(pk1_result, pk2_result)
#if pk_points == 0:
#   print("Points winner: Can't be determined")
#elif pk_points > 0:
#   print("Points winner: ", pk1_name_input, "with", pk_points, "points")
#elif pk_points < 0:
#   print("Points winner: ", pk2_name_input, "with", pk_points, "points")