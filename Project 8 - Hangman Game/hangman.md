# Hangman Game
This project consists of a `get_valid_word()` and `hangman()` functions together making the whole functioning of the Hangman game.

## Functioning

### `get_valid_word()` function

The program makes use of a [JSON wordlist with 2,465 words](https://www.randomlists.com/data/words.json) for picking up a random word for the game.
Some words consists of `-` (Hyphens), so to filter out those words, the following logic is used:-
```py
valid_word = random.choice(words)
while '-' in valid_word:
    valid_word = random.choice(words)

return valid_word.upper()
```

### `hangman()` function

A valid is chosen randomly using the `random.choice()` method. Now all the letters are converted to a set and stored in `word_letters`, valid alphabets are stored as a set in `alphabets`,
and the used letters are stored as a set in `used_letters`.

```py
    word = get_valid_word(words)
    word_letters = set(word)
    alphabets = set(string.ascii_uppercase)
    used_letters = set()
```

The following list stores the hangman structure to be printed each time a wrong guess is made.

```py
man = ["""|----------|""",
"""|          |""",
    """|          O""",
    """|        / | \ """,
    """|          |""",
    """|         / \\
|
|________________"""]
```

<br>

The main loop body starts here, it runs until the whole word is guessed correctly, or the user had made enough wrong guesses to complete the hangman structure.
```py
wrong_guess = 0
while len(word_letters) > 0 and wrong_guess < 5:
    for i in range(wrong_guess+1):
        print(man[i])
```

<br> 

Afterwords it displays the letters already used; and displays the word to guess, with the words being filled in that have been guessed correctly, and the rest unguessed being denoted by the `-`.
 ```py
 print("\nYou have used the following letters: ", ' '.join(used_letters))
        
 word_list = [letter if letter in used_letters else '-' for letter in word]
 print("\nCurrent word to guess: ", ' '.join(word_list))
 ```
 <br>
 
 It asks for the user to input a character, it goes in the selection statements later.
 - If the input character is a valid character it further checks if it's a correct word guess. If yes then it removes that character, elsewise it increments `wrong_guess`.
 - If the input character is already used, it notifies the user to consider their choice again. (`wrong_guess` is not incrememnted)
 - If the input character is not a valid character, it notifies the user to consider their choice agian. (`wrong_guess` is not incrememnted)
 ```py
        user_input = input("Guess a letter: ").upper()
        print()

        if user_input in alphabets - used_letters:
            used_letters.add(user_input)
            if user_input in word_letters:
                word_letters.remove(user_input)
            else: wrong_guess+=1

        elif user_input in used_letters:
            print("You've already used that character. Consider using another one.\n\n")

        else:
            print("Invalid Letter Entered. Consider trying again.\n\n")
```

<br>

After exiting the loop, it checks whether the user won, or lost.

```py
if wrong_guess == 5:
        for item in man:
            print(item)
        print(f"\nOops! You've used all of your lives!\nThe correct word was {word}")

else:
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("\nVoila! You guessed the word!\n", ' '.join(word_list))
```

