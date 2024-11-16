# Administrator of the Zoo

from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name):
        self.name = name 


    @abstractmethod
    def make_sound(self):
        pass


class Tiger(Animal):
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex
        self.species = "tiger"

    def make_sound(self):
        return "*Growls Menancenly*"

class Penguin(Animal):
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex
        self.species = "penguin"

    def make_sound(self):
        return "*Judges You in Silence*"

class Serpent(Animal):
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex
        self.species = "serpent"

    def make_sound(self):
        return "*does SSSsssSSssSSSSSssS!*"

class Place:
    def __init__(self, biome, animal : Animal):
        self.biome = biome
        self.animal = animal
    
    def place_animal(self):
        sound = self.animal.make_sound()
        pronoun = "he" if self.animal.sex == "male" else "she"
        print(f"You have placed the {self.animal.species} {self.animal.name} in the cage that resembles the {self.biome} biome. {pronoun.capitalize()} {sound}\n")
        
tiger1 = Tiger("Tigresa", "female")
penguin1 = Penguin("Skipper", "male")
serpent1 = Serpent("Jormungander", "male")

savanna_cage = Place("savanna", tiger1)
antartic_tundra_cage = Place("antartic tundra", penguin1)
midgard_ocean_cage = Place("oceans of midgard", serpent1)

savanna_cage.place_animal()
antartic_tundra_cage.place_animal()
midgard_ocean_cage.place_animal()