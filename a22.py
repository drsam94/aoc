PART = 2
enemy = {
        "hp" : 58,
        "damage" : 9
        }

def copy_timers(timers, optional_key = ""):
    new_timers = {k:v for k,v in timers.items()}
    if optional_key:
        new_timers[optional_key] = 5 if optional_key == "recharge" else 6
    return new_timers

def apply_timers(enemy_hp, player_mana, timers):
    if timers["poison"] > 0:
        enemy_hp -= 3
        timers["poison"] -= 1
    if timers["shield"] > 0:
        timers["shield"] -= 1
    if timers["recharge"] > 0:
        player_mana += 101
        timers["recharge"] -= 1
    return enemy_hp,player_mana,timers

def min_mana(enemy_hp = enemy["hp"], player_hp = 50,
             player_mana = 500, timers = {"poison":0,"shield":0,"recharge":0},
             spent_mana = 0, current_min = float("inf"), process_boss_attack_first = False):
    if spent_mana >= current_min or  player_mana < 0:
        return current_min

    if PART == 2:
        player_hp -= 1
        if player_hp <= 0:
            return current_min

    if process_boss_attack_first:
        enemy_hp, player_mana, timers = apply_timers(enemy_hp, player_mana, timers)
        if enemy_hp < 0:
            return spent_mana
        player_hp -= enemy["damage"] - (7 if timers["shield"] > 0 else 0)
        if player_hp < 0:
            return current_min

    enemy_hp, player_mana, timers = apply_timers(enemy_hp, player_mana, timers)

    current_min = min(current_min, min_mana(enemy_hp - 4, player_hp, player_mana - 53,
                                    copy_timers(timers), spent_mana + 53, current_min, True))

    current_min = min(current_min, min_mana(enemy_hp - 2, player_hp + 2, player_mana - 73,
                                    copy_timers(timers), spent_mana + 73, current_min, True))
    if timers["shield"] == 0:
        current_min = min(current_min, min_mana(enemy_hp, player_hp, player_mana - 113,
                          copy_timers(timers,"shield"), spent_mana + 113, current_min, True))
    if timers["poison"] == 0:
        current_min = min(current_min, min_mana(enemy_hp, player_hp, player_mana - 173,
                          copy_timers(timers,"poison"), spent_mana + 173, current_min, True))
    if timers["recharge"] == 0:
        current_min = min(current_min, min_mana(enemy_hp, player_hp, player_mana - 229,
                          copy_timers(timers,"recharge"), spent_mana + 229, current_min, True))
    return current_min

print(min_mana())
