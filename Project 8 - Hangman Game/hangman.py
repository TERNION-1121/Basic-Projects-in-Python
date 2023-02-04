from words import words
import random
import string

def get_valid_word(word_seq):
    valid_word = random.choice(words)
    while '-' in valid_word:
        valid_word = random.choice(words)

    return valid_word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabets = set(string.ascii_uppercase)
    used_letters = set()

    man = ["""|----------|""",
"""|          |""",
    """|          O""",
    """|        / | \ """,
    """|          |""",
    """|         / \\
|
|________________"""]

    wrong_guess = 0
    while len(word_letters) > 0 and wrong_guess < 5:
        for i in range(wrong_guess+1):
            print(man[i])
        
        print("\nYou have used the following letters: ", ' '.join(used_letters))
        
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("\nCurrent word to guess: ", ' '.join(word_list))

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
            

    if wrong_guess == 5:
        for item in man:
            print(item)
        print(f"\nOops! You've used all of your lives!\nThe correct word was {word}")

    else:
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("\nVoila! You guessed the word!\n", ' '.join(word_list))

hangman()