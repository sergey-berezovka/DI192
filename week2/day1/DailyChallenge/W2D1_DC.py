# Daily challenge: Old MacDonald’s Farm
class Farm:
    def __init__(self, farm_name):
        self.name = farm_name
        self.animals = {}

    def add_animal(self, animal_type=None, count=1, **kwargs):

        if animal_type in self.animals:
            self.animals[animal_type] += count
        else:
            self.animals[animal_type] = count

        if kwargs:
            for animal, qty in kwargs.items():
                if animal in self.animals:
                    self.animals[animal] += qty
                else:
                    self.animals[animal] = qty
            return

    def get_info(self):
        output = f"{self.name}'s farm\n\n"

        for animal, count in self.animals.items():
            output += f"{animal} : {count}\n"

        output += "\n    E-I-E-I-0!"
        return output

    def get_animal_types(self):
        return sorted(self.animals.keys())

    def get_short_info(self):
        animal_list = self.get_animal_types()

        formatted = []
        for animal in animal_list:
            if self.animals[animal] > 1:
                formatted.append(animal + "s")
            else:
                formatted.append(animal)

        if len(formatted) > 1:
            animals_string = ", ".join(formatted[:-1]) + " and " + formatted[-1]
        else:
            animals_string = formatted[0]

        return f"{self.name}'s farm has {animals_string}."
    
macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())