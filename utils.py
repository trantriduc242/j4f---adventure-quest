# utils.py
import random

def roll_dice(sides=6):
    return random.randint(1, sides)

def fancy_print(text):
    border = "=" * (len(text) + 4)
    print(border)
    print("| " + text + " |")
    print(border)
