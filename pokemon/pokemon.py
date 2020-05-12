import requests

def get_pokemon(pokemon_name):
    url = "https://pokeapi.co/api/v2/pokemon/{pk}".format(pk=pokemon_name)
    result = requests.get(url)
    pokemon = result.json()
    return pokemon

def retrieve_type(pokemon):
    types = pokemon["types"]
    type_url = [sub["type"]["url"] for sub in types]
    return type_url

def retrieve_stats(pokemon):
    stats = pokemon["stats"]
    return stats

def get_type(type_url):
    type = []
    i = 0
    while i < len(type_url):
        result = requests.get(type_url[i])
        type1 = result.json()
        type.insert(i, type1)
        i += 1
    return type

def get_pk_type(type):
    pokemon_type = []
    i = 0
    while i < len(type):
        pokemon_type1 = type[i]["name"]
        pokemon_type.insert(i, pokemon_type1)
        i += 1
    return pokemon_type

def get_damage_from(type):
    i = 0
    damage_from1 = []
    while i < len(type):
        damage_pk1 = type[i]["damage_relations"]["double_damage_from"]
        damage_from1.insert(i, [sub["name"] for sub in damage_pk1])
        i += 1
    damage_from = []
    i = 0
    j = 0
    while i < len(damage_from1):
        while j < len(damage_from1[i]):
            bloque12 = damage_from1[i][j]
            damage_from.insert(j + len(damage_from), bloque12)
            j += 1
        i += 1
        j = 0
    damage_from = list(dict.fromkeys(damage_from))
    return damage_from

def get_half_damage_from(type):
    i = 0
    half_damage_from1 = []
    while i < len(type):
        damage_pk1 = type[i]["damage_relations"]["half_damage_from"]
        half_damage_from1.insert(i, [sub["name"] for sub in damage_pk1])
        i += 1
    half_damage_from = []
    i = 0
    j = 0
    while i < len(half_damage_from1):
        while j < len(half_damage_from1[i]):
            bloque12 = half_damage_from1[i][j]
            half_damage_from.insert(j + len(half_damage_from), bloque12)
            j += 1
        i += 1
        j = 0
    half_damage_from = list(dict.fromkeys(half_damage_from))
    return half_damage_from

def get_damage_to(type):
    i = 0
    damage_to1 = []
    while i < len(type):
        damage_pk2 = type[i]["damage_relations"]["double_damage_to"]
        damage_to1.insert(i, [sub["name"] for sub in damage_pk2])
        i += 1
    damage_to = []
    i = 0
    j = 0
    while i < len(damage_to1):
        while j < len(damage_to1[i]):
            bloque12 = damage_to1[i][j]
            damage_to.insert(j + len(damage_to), bloque12)
            j += 1
        i += 1
        j = 0
    damage_to = list(dict.fromkeys(damage_to))
    return damage_to

def get_half_damage_to(type):
    i = 0
    half_damage_to1 = []
    while i < len(type):
        damage_pk1 = type[i]["damage_relations"]["half_damage_to"]
        half_damage_to1.insert(i, [sub["name"] for sub in damage_pk1])
        i += 1
    half_damage_to = []
    i = 0
    j = 0
    while i < len(half_damage_to1):
        while j < len(half_damage_to1[i]):
            bloque12 = half_damage_to1[i][j]
            half_damage_to.insert(j + len(half_damage_to), bloque12)
            j += 1
        i += 1
        j = 0
    half_damage_to = list(dict.fromkeys(half_damage_to))
    return half_damage_to

def get_no_damage_to(type):
    i = 0
    no_damage_to1 = []
    while i < len(type):
        damage_pk1 = type[i]["damage_relations"]["no_damage_to"]
        no_damage_to1.insert(i, [sub["name"] for sub in damage_pk1])
        i += 1
    no_damage_to = []
    i = 0
    j = 0
    while i < len(no_damage_to1):
        while j < len(no_damage_to1[i]):
            bloque12 = no_damage_to1[i][j]
            no_damage_to.insert(j + len(no_damage_to), bloque12)
            j += 1
        i += 1
        j = 0
    no_damage_to = list(dict.fromkeys(no_damage_to))
    return no_damage_to

def get_no_damage_from(type):
    i = 0
    no_damage_from1 = []
    while i < len(type):
        damage_pk1 = type[i]["damage_relations"]["no_damage_from"]
        no_damage_from1.insert(i, [sub["name"] for sub in damage_pk1])
        i += 1
    no_damage_from = []
    i = 0
    j = 0
    while i < len(no_damage_from1):
        while j < len(no_damage_from1[i]):
            bloque12 = no_damage_from1[i][j]
            no_damage_from.insert(j + len(no_damage_from), bloque12)
            j += 1
        i += 1
        j = 0
    no_damage_from = list(dict.fromkeys(no_damage_from))
    return no_damage_from

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
    pk_type_url = retrieve_type(pk_choice)
    pk_type = get_type(pk_type_url)
    pk_type_pk = get_pk_type(pk_type)
    pk_damage_from = get_damage_from(pk_type)
    pk_half_damage_from = get_half_damage_from(pk_type)
    pk_damage_to = get_damage_to(pk_type)
    pk_half_damage_to = get_half_damage_to(pk_type)
    pk_no_damage_to = get_no_damage_to(pk_type)
    pk_no_damage_from = get_no_damage_from(pk_type)
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