# Exercise 2: Dogs
class Dog:
    def __init__(self, name, age, weight):
        # ... code to initialize attributes ...
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        # ... code to return bark message ...
        return(f"{self.name} is barking")

    def run_speed(self):
        # ... code to return run speed ...
        return(self.weight / self.age * 10)

    def fight(self, other_dog):
        # ... code to determine and return winner ...
        my_power = self.run_speed() * self.weight
        other_power = other_dog.run_speed() * self.weight
    
        if my_power > other_power:
            print(f"{self.name} wins!")
        elif my_power < other_power:
            print(f"{other_dog.name} wins!")
        else:
            print("It's a draw!")

# Step 2: Create dog instances
#... your code here
dog1 = Dog("Palkan", 4, 20)
dog2 = Dog("Bella", 2, 15)

# Step 3: Test dog methods
print(dog1.bark())
print(dog2.run_speed())
print(dog1.fight(dog2))