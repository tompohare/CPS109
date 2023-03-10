"""Guess a number between 1 and 6"""

import random

guess = int(input('Guess a number between 1 and 6: '))

number = 0 # a number picked randomly
count = 0 # number of tries taken to match the guess

while guess != number:
    count += 1
    # Randomly pick a number between 1 and 6
    number = random.randrange(1, 7)

    if guess == number:
        print(f'Yes! the number chosen is {number} in {count} tries')
    else:
        print(f'Nope! you guessed {guess} but the number was {number}')