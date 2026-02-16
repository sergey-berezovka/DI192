# Exercise 1: Concatenate lists
list1 = [123]
list2 = [456]
list1.extend(list2)
print(list1)

# Exercise 2: Range of numbers
for number in range (1500,2500+1):
    if number % 7 == 0 and number % 5 == 0:
        print(number)

# Exercise 3: Check the index:
names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
user_name = input("Enter a name: ")
if user_name in names:
    index = names.index(user_name)
    print(f"{user_name} is at index {index}.")
else:
    print("Name not found.")

# Exercise 4: Greatest Number
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))
greatest_number = max(number1, number2, number3)
print(f"The greatest number is: {greatest_number}")

# Exercise 5: The Alphabet
alphabet = "abcdefghijklmnopqrstuvwxyz"
vowels = "aeiou"
for letter in alphabet:
    if letter in vowels:
        print(f"{letter} is a vowel.")
    else:
        print(f"{letter} is a consonant.")

# Exercise 6: Words and letters
words = []
for i in range(7):
    word = input("Enter a word: ")
    words.append(word)

letter = input("Enter a single character: ")
while len(letter) != 1:
    letter = input("Please enter exactly one character: ")
for word in words:
    if letter in word:
        print(f"In '{word}' the first occurrence of '{letter}' is at index {word.index(letter)}")
    else:
        print(f"'{letter}' does not appear in '{word}'")

# Exercise 7: Min, Max, Sum
numbers = list(range(1, 1000000+1))
print("Min:", min(numbers))
print("Max:", max(numbers))
print("Sum:", sum(numbers))

# Exercise 8 : List and Tuple
user_input = input("Enter comma-separated numbers: ")
numbers_list = user_input.split(",")
numbers_tuple = tuple(numbers_list)
print(numbers_list)
print(numbers_tuple)

# Exercise 9 : Random number
import random
wins = 0
losses = 0
while True:
    user_input = input("Guess a number between 1 and 9 or 'quit'): ")

    if user_input.lower() == "quit":
        break

    try:
        user_number = int(user_input)

        if not 1 <= user_number <= 9:
            print("Please enter a number between 1 and 9.")
            continue

        random_number = random.randint(1, 9)

        if user_number == random_number:
            print("Winner!")
            wins += 1
        else:
            print(f"Better luck next time. The number was {random_number}.")
            losses += 1

    except ValueError:
        print("Invalid input. Please enter a number or 'quit'.")
print("\nGame over!")
print(f"Total wins: {wins}")
print(f"Total losses: {losses}")





                 