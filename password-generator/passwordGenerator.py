import random

appercase_letters = "ABCDEFGHIJKLNMOPQRSTUVWXYZ"
lowercase_letters = appercase_letters.lower()
digits = "0123456789"
symbols = "!@#$%^&"

apper, lower, nums, symb = True, True, True, True

char_to_use = ""
lengh_of_password = 20
amount = 10
passord_storage = {}

if apper:
    char_to_use += appercase_letters

if lower:
    char_to_use += lowercase_letters

if digits:
    char_to_use += digits

if symb:
    char_to_use += symbols


for p in range(amount):
    passord_storage[p] = ""
    for i in range(lengh_of_password):
        passord_storage[p] += char_to_use[int(random.randrange(0,len(char_to_use)))]

print(passord_storage)
