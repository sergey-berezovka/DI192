# Exercise 3: String module
import string
import random

letters = string.ascii_letters

random_string = ""

for _ in range(5):
    random_char = random.choice(letters)
    random_string += random_char

print(random_string)