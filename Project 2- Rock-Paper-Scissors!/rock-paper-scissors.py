from random import choice
def rps(user_action = input("Enter your choice of action (rock, paper, scissors):\n")):

    possible_actions = ['rock', 'paper', 'scissors']
    while True: 
        computer_action = choice(possible_actions)

        wins = [['rock', 'scissors'], ['paper', 'rock'], ['scissors', 'paper']]

        if user_action in possible_actions:
            print(f"You chose {user_action}, and the computer chose {computer_action}.", end = " ") 
            if [user_action, computer_action] in wins:
                print("You won!")
            elif user_action == computer_action: 
                print('Draw!')
            else:
                print("You lost!")
        else:
            print('Invalid Input Action!')
            
        again = input("\nWant to continue (y/n) ? ")
        if again.lower() == 'y':
            user_action = input("Enter your choice of action (rock, paper, scissors):\n")
            continue
        else: 
            break

rps()