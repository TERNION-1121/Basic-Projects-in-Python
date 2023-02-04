# Dice Simulator in Python

This program is **Dice Simulator**, which works on a very simple logic.

The program uses the `randint()` function, available in `random` module to print number between 1 to 6.

```py
    again = 'y'
    while again:
        print(f"The dice rolled {random.randint(1,6)}")
        again = input("Want to continue? (y/n):\t")
        
        if again == 'y': continue 
        else: break```
