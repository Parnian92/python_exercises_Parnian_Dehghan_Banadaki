#session_04
#1) Number Guessing Game
import random
target_number=random.randint(1,100)
while True:
    guess= float(input('Guess a number:'))
    if guess>target_number:
        print('Guess lower')
    elif guess<target_number:
        print('Guess higher')
    else:
        print('Congratulations! you guessed the correct number.')
        break