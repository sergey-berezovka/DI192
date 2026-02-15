import random
# Excercise 1: Ask for User Input:
while True:
    user_input = input("Enter exactly 10 characters: ")
    if len(user_input) == 10:
        break
    else:
        print("Please enter a string that is exactly 10 characters long.")

print("Perfect string!")

# Excercise 2&3: Print the First and Last Characters:
print(f"First character: {user_input[0]}")
print(f"Last character: {user_input[-1]}")

# Excercise 4: Build the String Character by Character:
for i in range(len(user_input)):
    print(user_input[:i+1])

# Excercise 5: Jumble the String:
letters = list(user_input)
random.shuffle(letters)
print(''.join(letters))