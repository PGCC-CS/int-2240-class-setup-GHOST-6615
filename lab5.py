import random

numbers = []

roll_again = 'y'

while roll_again == 'y':

    print("Rolling the dice...")

    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    dice3 = random.randint(1, 6)

    numbers.append(dice1)
    numbers.append(dice2)
    numbers.append(dice3)

    print("Their values are:")
    print(dice1)
    print(dice2)
    print(dice3)

    roll_again = input("Roll them again? (y = yes): ")

print("List of all generated numbers:")
print(numbers)