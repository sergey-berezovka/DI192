# # Exercise 1: Converting Lists into Dictionaries
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# my_dict = dict(zip((keys), (values)))
# print(my_dict)

# # Exercise 2: Cinemax #2
# family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

# total = 0
# for key,value in family.items():
#     if value < 3:
#         print(f"{key} is Free")
#     elif value < 12:
#         print(f"{key}  is 10$")
#         total += 10
#     else:
#         print(f"{key} is 15$")
#         total += 15
# print(f"The total price for the family is {total}$")

# Exercise 3: Zara

brand = {
    "name": "Zara", "creation_date": 1975, 
    "creator_name": "Amancio Ortega Gaona", 
    "type_of_clothes": ["men", "women", "children", "home"], 
    "international_competitors": ["Gap", "H&M", "Benetton"], 
    "number_stores": 7000, 
    "major_color": {
        "France": "blue", "Spain": "red", "US": ["pink", "green"]
    }
}
print(brand)

# 1. Change the number of stores to 2.
brand["number_stores"] = 2
print(brand)

# 2. Print a sentence that explains who Zara's clients are.
print(f"Zara's clients are {', '.join(brand['type_of_clothes'])}.")

# 3. Add a key called country_creation with a value of Spain.
brand["country_creation"] = "Spain"
print(brand)

# 4. Check if international_competitors exists and, if so, add “Desigual” to the list.
if "international_competitors" in brand:
    brand["international_competitors"].append ("Desigual")
print(brand)

# 5. Delete the creation_date key
del brand["creation_date"]
print(brand)

# 6.Print the last item in international_competitors.
print(brand["international_competitors"][-1])

# 7. Print the major colors in the US.
print(brand["major_color"]["US"])

# 8. Print the number of keys in the dictionary.
print(len(brand))

# 9. Print all keys of the dictionary.
print(brand.keys())



