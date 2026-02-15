# Excercise 1: Hello World
for i in range(4):
    print("Hello world")

# Excercise 2: Some Math
import math
result = (99 ** 3) * 8
print(result)

# Excercise 3: What is the output?
print(5 < 3)  # False
print(3 == 3)  # True
print(3 == "3")  # False
try:
    print("3" > 3)  # TypeError: '>' not supported between instances of 'str' and 'int'
except TypeError:  
    print("TypeError: '>' not supported between instances of 'str' and 'int'") 
print("Hello" == "hello")  # False

# Excercise 4: Your computer brand
computer_brand = "Dell"
print(f"I have a {computer_brand} computer")

# Excercise 5: Your Information
name = "Sergei Berezovka"
age = 47
shoe_size = 42
info = f"My name is {name}, I am {age} years old and my shoe size is {shoe_size}."
print(info)

# Excercise 6: A & B
a = 10
b = 7
if a > b:
    print("Hello World")
else:
    print("")

# Excercise 7: Odd or Even
number = 7
if number % 2 == 0:
    print("Even")
else:
    print("Odd")

# Excercise 8: What’s your name?
name = input(str("What is your name? "))
my_name = "Sergei"
if name == my_name:
    print(f"Hello {name}! We have the same name!")
else:
    print(f"Hello {name}! Nice to meet you!")

# Excercise 9: Tall enough to ride a roller coaster
height = int(input("What is your height in cm? "))
if height >= 151:
    print("You are tall enough to ride!")
else:
    print("You need to grow some more to ride!")