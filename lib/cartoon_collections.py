def roll_call_dwarves(dwarves):
    for index, dwarf in enumerate(dwarves):
        print(f"{index + 1}. {dwarf}")

def summon_captain_planet(calls):
    return [call.title() + "!" for call in calls]

def long_planeteer_calls(calls):
    for call in calls:
        if len(call) > 4:
            return True
    return False

def find_the_cheese(foods):
    if "cheddar" in foods:
        return "cheddar"
    elif "gouda" in foods:
        return "gouda"
    elif "camembert" in foods:
        return "camembert"
    return None
