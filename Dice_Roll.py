import random


def dice_roll(max, qty):
    print(random.randint(1, max))
    if qty > 1:
        for _ in range((qty-1)):
            print(random.randint(1, max))


dice_roll(int(input("Dice Sides: ")), int(input("Times Rolled: ")))
