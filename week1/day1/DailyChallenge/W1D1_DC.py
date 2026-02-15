# Excercise 1: Ask for User Input:
user_input = input("Enter exactly 10 characters long):")

# Excercise 2: Check the length of the input string:
if len(user_input) == 10:
    print("Perfect string!")
elif len(user_input) < 10:
    print("String not long enough.")
else:
    print("String too long.")

# Excercise 3: Print the First and Last Characters:
if len(user_input) >= 1:
    print(f"First character: {user_input[0]}")
    print(f"Last character: {user_input[-1]}")

# Excercise 4: Build the String Character by Character:
user_input = "Helloworld"
for i in range(len(user_input)):
    print(user_input[:i+1])

# Excercise 5: Jumble the String:
import random
user_input = "Helloworld"
letters = list(user_input)
random.shuffle(letters)
print(''.join(letters))