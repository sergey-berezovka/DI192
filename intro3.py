lst = [("name", "Elie"), ("job", "Instructor")]
result = dict(lst)
print(result)

list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]
result = dict(zip(list1,list2))
print(result)

vowels = "aeiou"
result = {vowel: 0 for vowel in vowels}
print(result)

result = {i: chr(64+i) for i in range(1,27)}
print(result)

string = "awesome sauce"
vowels = "aeiou"
result = {vowel: string.count(vowel) for vowel in vowels}
print(result)

