import random as r


def roll1():
    pair_dice =[]
    for i in range(1, 7):
        for j in range(1, 7):
            pair_dice.append((i, j))
    print(pair_dice)
    print(r.choice(pair_dice))


def roll2():
    first = r.randint(1, 6)
    second = r.randint(1, 6)
    return first, second

