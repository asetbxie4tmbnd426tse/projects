import random

appercase_letters = "ABCDEFGHIJKLNMOPQRSTUVWXYZ"
lowercase_letters = appercase_letters.lower()
digits = "0123456789"
symbols = "!@#$%^&"

def generate_password(lengh: int, apper=True, lower=True, nums=True, symb=True):
    char_to_use = ""
    password = ""
    
    if apper:
        char_to_use += appercase_letters
    if lower:
        char_to_use += lowercase_letters
    if digits:
        char_to_use += digits
    if symb:
        char_to_use += symbols
    
    for i in range(lengh):
        password += char_to_use[int(random.randrange(0,len(char_to_use)))]
    return password

def to_dictionarey(app_name: str, username: str, password: str):
    ret = {
        "app_name": app_name,
        "username": username,
        "password": password
    }
