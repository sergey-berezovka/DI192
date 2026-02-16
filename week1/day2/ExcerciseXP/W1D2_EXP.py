# Exercise 1: Favorite Numbers
my_fav_numbers = {3,7,10}
my_fav_numbers.add(20)
my_fav_numbers.add(30)
my_fav_numbers.remove(30)
friend_fav_numbers = {1,2,3}
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers) # Union sets
print(our_fav_numbers)

print("My favorite numbers:", my_fav_numbers)
print("Friend's favorite numbers:", friend_fav_numbers)
print("Our favorite numbers:", our_fav_numbers)

# Exercise 2: Tuple
my_tuple = (1, 2, 3)
additional_tuple = (4, 5, 6)
union_tuples = my_tuple + (additional_tuple, ) # Adding the additional tuple
print(union_tuples)

# Exercise 3: List Manipulation
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
basket.remove("Blueberries")
basket.append("Kiwi")
basket.insert(0, "Apples")
basket.count("Apples")
basket.clear()
print("Final basket:", basket)

# Exercise 4: Floats
# 2 → int
# 2.0 → float
my_list = [1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]
numbers_my_list = [int(x * 0.5) if x % 2 == 0 else x * 0.5 for x in range(3, 11)]
print(numbers_my_list)

# Exercise 6: While Loop
while True:
    user_name = input("Enter your name: ")
    if len(user_name) > 3 and not any(char.isdigit() for char in user_name):
        print("thank you")
        break
    else:
        print(f"give correct name: {user_name}")

# Exercise 7: Favorite Fruits
favorite_fruits = input("Enter your favorite fruits (separated by spaces): ").split()
fruit = input("Enter the name of any fruit: ")
if fruit in favorite_fruits:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy it!")

# Exercise 8: Pizza Toppings?
toppings = []
while True:
    topping = input("Enter a pizza topping (or 'quit' to finish): ")
    if topping.lower() == 'quit':
        break
    toppings.append(topping)
    print(f"Adding {topping} to your pizza.")
cost = len(toppings) * 2.5
print(f"Your pizza toppings: {toppings}")
print(f"Total cost of your pizza: ${cost:.2f}")

# Exercise 9: Cinemax Tickets
total_cost = 0
while True:
    age_input = input("Enter age (or 'quit' to finish): ")

    if age_input.lower() == "quit":
        break
    age = int(age_input)
    if age < 3:
        cost = 0
    elif 3 <= age <= 12:
        cost = 10
    else:
        cost = 15
    total_cost += cost
print(f"Total ticket cost: ${total_cost}")

# Bonus:
attendees = []
while True:
    age_input = input("Enter age (or 'quit' to finish): ")
    if age_input.lower() == "quit":
        break
    age = int(age_input)
    attendees.append(age)

allowed = []
for age in attendees:
    if 16 <= age <= 21:
        allowed.append(age)
print("Final list of attendees:", allowed)


