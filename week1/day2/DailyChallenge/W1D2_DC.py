# Challenge 1: Multiples of a Number
number = int(input("Enter a number: "))
lenght = int(input("Enter a length: "))
list_of_numbers = []
for i in range(1, lenght + 1):
    list_of_numbers.append(number * i)
print(list_of_numbers)

# Challenge 2: Remove Consecutive Duplicate Letters
text = input("Enter a string: ")
if not text:
    print("")
else:
    result = text[0]

    for char in text[1:]:
        if char != result[-1]:
            result += char
    print(result)

