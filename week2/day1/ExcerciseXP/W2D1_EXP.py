# Exercise 1: Cats
class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

# Step 1: Create cat object:
cat1 = Cat("Funny", 3)
cat2 = Cat("Sunny", 7)
cat3 = Cat("Shiny", 1)

# Step 2: Create a function to find the oldest cat:
def find_oldest_cat(cat1, cat2, cat3):
    if cat1.age >= cat2.age and cat1.age >= cat3.age:
        return cat1
    if cat2.age >= cat1.age and cat2.age >= cat3.age:
        return cat2
    else: 
        return cat3
    
oldest = find_oldest_cat(cat1, cat2, cat3)

# Step 3: Print the oldest cat details:
print(oldest.name, oldest.age)

# Exercise 2 : Dogs
# Create the Dog Class:
class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print(f"{self.name} goes woof!")

    def jump(self):
        print(f"{self.name} jumps {self.height} * 2 cm high!")

# Step 2: Create Dog Objects:
davids_dog = Dog("Rex", 40)
sarahs_dog = Dog("Bella", 15)

# Step 3: Print Dog Details and Call Methods:
print(f"{davids_dog.name} is {davids_dog.height} cm tall")
davids_dog.bark()
davids_dog.jump()
print()
print(f"{sarahs_dog.name} is {sarahs_dog.height} cm tall")
sarahs_dog.bark()
sarahs_dog.jump()

# Step 4: Compare Dog Sizes:
if davids_dog.height > sarahs_dog.height:
    print(f"{davids_dog.name} is bigger.")
elif sarahs_dog.height > davids_dog.height:
    print(f"{sarahs_dog.name} is bigger.")
else:
    print("Both dogs are the same height.")

# Exercise 3 : Who’s the song producer?
# Goal: Create a Song class to represent song lyrics and print them.
class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics
    
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

stairway = Song(["There’s a lady who's sure", "all that glitters is gold", "and she’s buying a stairway to heaven"])

stairway.sing_me_a_song()

# Exercise 4 : Afternoon at the Zoo
class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []

    def add_animal(self, *new_animals):
        for animal in new_animals:
            if animal not in self.animals:
                self.animals.append(animal)

    def get_animals(self):
        print(self.animals)

    def sell_animal(self, sold_animal):
        if sold_animal in self.animals:
            self.animals.remove(sold_animal)

    def sort_animals(self):
        grouped = {}

        for animal in sorted(self.animals):
            first_letter = animal[0]
            if first_letter not in grouped:
                grouped[first_letter] = []
            grouped[first_letter].append(animal)

        return grouped

    def get_groups(self):
        groups = self.sort_animals()

        for letter, animals in groups.items():
            print(f"{letter}: {animals}")

brooklyn_safari = Zoo("Brooklyn Safari")

brooklyn_safari.add_animal("Giraffe", "Bear", "Baboon", "Lion", "Zebra", "Cat", "Cougar")

# brooklyn_safari.add_animal("Giraffe")
# brooklyn_safari.add_animal("Bear")
# brooklyn_safari.add_animal("Baboon")

brooklyn_safari.get_animals()

brooklyn_safari.sell_animal("Bear")

brooklyn_safari.get_animals()

brooklyn_safari.get_groups()













        

        

        