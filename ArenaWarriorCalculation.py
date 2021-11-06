import random as random
import math as math


def WarCrit(warrior_level, damage, critchance, critdamage, atk_spd, i=1, n=1, timer=200):
    stage = 1
    pierce = math.floor(warrior_level / 50)
    stagehp = 500 * 1.1 ** stage
    true_crit = damage * critdamage
    full_pierce = pierce
    while stagehp >= 0 and timer - n >= 0:
        if stagehp >= 0:
            n += 1 / (1 + (atk_spd / 2))
            if random.randint(0, 1) < (critchance / i):
                stagehp = stagehp - true_crit
                print("Crit!", stagehp, i)
            else:
                stagehp = stagehp - damage
                print("Normal Hit!", stagehp, i)
        if stagehp <= 0:
            overflow = stagehp
            stagehp = (500 * 1.1 ** (stage + i))
            print("dead!", overflow, i)
            while overflow < 0 < pierce:
                overflow += stagehp
                i += 1
                timer += 1
                pierce -= 1
                if pierce == 0:
                    pierce = full_pierce
                    overflow = 0
                    print("Pierce Reset!")


WarCrit(885, 1.504e10, 6848.78, 6.45, 9.06)
