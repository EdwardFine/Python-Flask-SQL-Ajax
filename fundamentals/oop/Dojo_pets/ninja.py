from pet import Pet

class Ninja:
    def __init__(self, first_name , last_name , treats , pet_food , pet ):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet
    
    def walk(self,treats=0):
        if treats>0 and treats <= self.treats:
            self.treats -= treats
            print(f"{self.first_name} gave {self.pet.name} {treats} treats on today's walk. {self.treats} treats remaining.")
        else:
            print(f"{self.first_name} took {self.pet.name} on a walk")
        self.pet.play(treats)
        return self
    
    def feed(self,amount):
        if amount <= self.pet_food:
            self.pet_food-=amount
            self.pet.eat(amount)
            print(f"Feeding {self.pet.name} {amount} food. {self.pet_food} food remaining.")
        else:
            print(f"Unable to feed {amount} food. Only have {self.pet_food} food remaining.")
        return self
    
    def bathe(self,treats=0):
        if treats>0 and treats <= self.treats:
            self.treats -= treats
            print(f"{self.first_name} gave {self.pet.name} {treats} during a bath. {self.treats} treats remaining.")
        else:
            print(f"{self.first_name} gave {self.pet.name} a bath.")
        self.pet.noise()
        self.pet.energy += treats
        self.pet.health += treats
        return self



