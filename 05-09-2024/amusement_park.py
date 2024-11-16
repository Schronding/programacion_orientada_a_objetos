class Attraction():
    def __init__(self, name, age_required, height_required):
        self._name = name
        self._age_required = age_required
        self._height_required = height_required

    def get_age_required(self):
        return self._age_required
    
    def get_height_required(self):
        return self._height_required
    
    def get_name(self):
        return self._name
    
    def validate_age(self, age):
        try:
            if type(age) != int or age <= 0:
                raise InvalidAge
        except InvalidAge as ERROR:
            print(ERROR)
        
    def validate_height(self, height):
        try: 
            if type(height) != int or height <= 0:
                raise InvalidHeight
        except InvalidHeight as ERROR:
            print(ERROR)
    
class Passenger():
    def __init__(self, age, height):
        self.age = age
        self.height = height

    def enter_attraction(self, attraction):
        valid_age = False
        valid_height = False

        # Validates if the age of the passenger is valid
        attraction.validate_age(self.age)

        if self.age >= attraction.get_age_required():
            valid_age = True
        else: 
            print("You're not tall enough to enter. Sorry! :(")
        
        # Validates if the height of the passenger is valid
        attraction.validate_height(self.height)

        if self.height >= attraction.get_height_required():
            valid_height = True
        else:
            print("You're not tall enough to enter. Sorry! :(")
        
        # Finally determines if the passenger is able to enter the attraction
        if valid_height and valid_age:
            print(f"You are allowed to enter {attraction.get_name()}. Enjoy!")

class PersonalizedException(Exception):
    def __init__():
        pass

class InvalidAge(PersonalizedException):
    def validate_age(passenger):
        if type(passenger.age) != int or passenger.age <= 0:
            raise InvalidAge

class InvalidHeight(PersonalizedException):
    def validate_height(passenger):
        if type(passenger.height) != int or passenger.height <= 0:
            raise InvalidHeight

def main():
    RollerCoaster = Attraction("SuperMan", 18, 170)
    Carrousel = Attraction("Le Grand Carrousel", 14, 160)
    SpookyHouse = Attraction("Leyendas de Mexico", 16, 100)

    AliceCoronel = Passenger(19, 165)
    BrayanCoronel = Passenger(-23, 170)
    UlisesOlivares = Passenger(35, -175)

    AliceCoronel.enter_attraction(RollerCoaster)
    BrayanCoronel.enter_attraction(Carrousel)
    UlisesOlivares.enter_attraction(SpookyHouse)
    
if __name__ == "__main__":
   main()

    
    

    



        
