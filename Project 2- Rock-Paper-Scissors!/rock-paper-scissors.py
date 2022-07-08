import random

def rps(user_action = input("Enter your choice of action (rock, paper, scissors):\n")):

    possible_actions = ['rock', 'paper', 'scissors']
    while user_action: 
        computer_action = random.choice(possible_actions)

        if user_action == computer_action:
            print(f"You chose {user_action}, and the Computer chose {computer_action}. It's a draw!")
        
        elif user_action == 'rock':
            if computer_action == 'scissors':
                print(f"You chose {user_action}, and the Computer chose {computer_action}. You won!")
            elif computer_action == 'paper':
                print(f"You chose {user_action}, and the Computer chose {computer_action}. You lost!")

        elif user_action == 'paper':
            if computer_action == 'rock':
                print(f"You chose {user_action}, and the Computer chose {computer_action}. You won!")
            elif computer_action == 'scissors':
                print(f"You chose {user_action}, and the Computer chose {computer_action}. You lost!") 
        
        elif user_action == 'scissors':
            if computer_action == 'paper':
                print(f"You chose {user_action}, and the Computer chose {computer_action}. You won!")
            elif computer_action == 'rock':
                print(f"You chose {user_action}, and the Computer chose {computer_action}. You lost!") 
        
        else:
            print("Invalid input action!")
            
        again = input("\nWant to continue (y/n) ? ")
        if again == 'y':
            user_action = input("Enter your choice of action (rock, paper, scissors):\n")
            continue
        else: 
            break

rps()