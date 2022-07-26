# Rock-Paper-Scissors game 👊🖐✌

This program makes use of simple selection statements to control the program flow to make the **Rock-Paper-Scissors** game work.

## How does it work?

The function takes input from the user, the user has to enter one of the below mentioned, three actions:
1. `rock`
2. `paper`
3. `scissors`
```py
user_action = input("Enter your choice of action (rock, paper, scissors):\n")
```
<hr>

Using the `choice()` function, available in `random` module, the computer stores one of the above mentioned **actions** in `computer_action`
```py
  possible_actions = ['rock', 'paper', 'scissors']
  computer_action = random.choice(possible_actions)
 ```
 
 Further the selection statements in the code compare the values of both, `user_action` and `computer_action` to display the output.
 The following rules are followed:
 - **Rock** wins over **Scissors** and/or loses to **Paper**
 - **Paper** wins over **Rock** and/or loses to **Scissors**
 - **Scissors** win over **Paper** and/or loses to **Rock**
 <br>
 
 ```py
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
```
