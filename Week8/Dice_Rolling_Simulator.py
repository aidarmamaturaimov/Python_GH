import random

def roll_dice():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    return dice1 + dice2

number_rolls = int(input("How many times do you want to roll the dice?"))

frequency = {}

for i in range(number_rolls):
    result = roll_dice()
    if result in frequency:
        frequency[result] += 1
    else:
        frequency[result] = 1

print("Dice Roll Results:")
for total in sorted(frequency.keys()):
    print(f"Sum {total}: {frequency[total]} times")
