# Random Password Generator
This program generates a random password using the `random` module.

## Functioning
It has four constants:-
- `ALPHA_LOWER` => Stores alphabets from **a-z**.
- `ALPHA_UPPER` => Stores alphabets from **A-Z**.
- `NUMBERS` => Stores numbers from **0-9**.
- `SYMBOLS` => Stores symbols **(~`!@#$%^&*()_-+={[}]|\:;"'<,>.?/)**.

The constant `CHARACTERS` includes all the above mentioned constants concatenated into a single constant.
```py
CHARACTERS = ALPHA_LOWER + ALPHA_UPPER + NUMBERS + SYMBOLS
```
<br>

The function argument asks for a positive integer value, which indicates the `length` of the password that would be generated.
If not mentioned, the function prints a password of length 5 characters.

```py
 if length != None:
         print(f"Password generated: {''.join(random.sample(CHARACTERS, length))}")      
    else:
         print(f"Password generated: {''.join(random.sample(CHARACTERS, 5))}")
```
