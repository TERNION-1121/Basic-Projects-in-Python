import random

def pwd_gen(length = None):
    ALPHA_LOWER = "abcdefghijklmnopqrstuvwxyz"
    ALPHA_UPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    NUMBERS = "0123456789"
    SYMBOLS = '''~`!@#$%^&*()_-+={[}]|\:;"'<,>.?/'''
    CHARACTERS = ALPHA_LOWER + ALPHA_UPPER + NUMBERS + SYMBOLS
    if length != None:
         print(f"Password generated: {''.join(random.sample(CHARACTERS, length))}")      
    else:
         print(f"Password generated: {''.join(random.sample(CHARACTERS, 5))}")

pwd_gen()