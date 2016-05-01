import random

def dicerand(dicenum):
    if dicenum == 1:
        return 1
    elif dicenum == 0:
        return 0
    else:
        return random.randrange(1, dicenum + 1, 1)


def throw_da_dice(throws, dice):
    throw_sum = 0
    rand_throw = 0
    avg = float
    for i in range(0, throws):
        rand_throw = dicerand(dice)
        throw_sum = throw_sum + rand_throw
    return throw_sum


def hit(damage, armor):
    if damage - armor >= 0:
        return damage - armor
    else:
        return 0


# KARTA POSTACI - WSPOLCZYNNIKI BAZOWE:

base_damage = [1, 4]
bonus_damage = [0, 0]
crit_chance = [1, 3]

base_armor = 1
bonus_armor = [0, 0]

# ----

def total_armor(base_armor, bonus_armor):

    armor_bonus_roll = throw_da_dice(bonus_armor[0], bonus_armor[1])
    total_armor = base_armor + armor_bonus_roll

    return total_armor

def total_damage(base_damage, bonus_damage):

    base_damage_roll = throw_da_dice(base_damage[0], base_damage[1])
    bonus_damage_roll = throw_da_dice(bonus_damage[0], bonus_damage[1])
    total_damage = base_damage_roll + bonus_damage_roll

    return total_damage


print total_armor(base_armor, bonus_armor)
print total_damage(base_damage, bonus_damage)
