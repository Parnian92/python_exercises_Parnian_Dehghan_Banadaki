#session_04
#2) Rock,Paper,Scissors
import random
options=['rock','paper','scissors']
while True:
    user_choice= input("Enter rock, paper, or scissors (or 'exit' to quit):").strip().lower()
    if user_choice=='exit':
        print('Game over.')
        break
    if user_choice not in options:
        print('Invalid input! Please try again.')
        continue
    computer_choice= random.choice(options)
    print('computer chose:',computer_choice)
    if user_choice== computer_choice:
        print('it is a tie')
    elif(user_choice=='rock'and computer_choice=='scissors')or\
        (user_choice=='paper'and computer_choice=='rock')or\
        (user_choice=='scissors'and computer_choice=='paper'):
        print('You win!')
    else:
        print('Computer wnis!')
