class Pet:
    health = 0
    energy = 0
    def __init__(self,name,type,tricks):
        self.name = name
        self.type = type
        self.tricks = tricks
        
    
    def sleep(self):
        self.energy+=25
        return self
    
    def eat(self, amount):
        self.energy +=(2*amount)
        self.health+=(3*amount)
        return self
    
    def play(self,treats):
        self.energy += treats
        self.health+=5
        return self
    
    def noise(self):
        print("Grrrr")
        return self
    
    def display_stats(self):
        print(f"Health: {self.health}")
        print(f"Energy: {self.energy}")
        return self

class Cat(Pet):
    def noise(self):
        print("Meow")
        return self

class Dog(Pet):
    def noise(self):
        print("Bark")
        return self

class Rat(Pet):
    def noise(self):
        print("Squeek")
        return self
