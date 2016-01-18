enemy = {
        "hp"     : 104,
        "attack" : 8,
        "armor"  : 1
        }

_data=  [ [ [8,4,0],
            [10,5,0],
            [25,6,0],
            [40,7,0],
            [74,8,0] ],

          [ [13,0,1],
            [31,0,2],
            [53,0,3],
            [75,0,4],
            [102,0,5],
            [0,0,0] ],

          [ [25,1,0],
            [50,2,0],
            [100,3,0],
            [20,0,1],
            [40,0,2],
            [80,0,3],
            [0,0,0] ] ]

weapons,armors,rings = [
       [
           { key : value for key, value in zip(["cost","attack","armor"],line) }
           for line in section
       ]
       for section in _data
   ]

def combine(items):
    return { key: sum(item[key] for item in items) for key in items[0] }

def playerWins(equipment):
    enemy_hp = enemy["hp"]
    player_hp = 100
    while True:
        enemy_hp -= max(1, equipment["attack"] - enemy["armor"])
        if enemy_hp <= 0:
            return True
        player_hp -= max(1, enemy["attack"] - equipment["armor"])
        if player_hp <= 0:
            return False

min_gold = float("inf")
max_gold = 0
for ring1 in rings:
    for ring2 in rings:
        for weapon in weapons:
            for armor in armors:
                if 0 != ring2["cost"] == ring1["cost"]:
                    continue
                equipment = combine([weapon,armor,ring1,ring2])
                if playerWins(equipment):
                    min_gold = min(equipment["cost"], min_gold)
                else:
                    max_gold = max(equipment["cost"], max_gold)
print(min_gold)
print(max_gold)
