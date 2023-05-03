class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name
    def addAnimal(self, name,type,age=3,health=10,happiness=10):
        type = type.lower()
        if type =="tiger":
            self.animals.append( Tiger(name,age,health,happiness) )
        elif type =="lion":
            self.animals.append(Lion(name,age,health,happiness))
        elif type == "bear":
            self.animals.append(Bear(name,age,health,happiness))
        else:
            self.animals.append(Animal(name,age,health,happiness))
        return self
    def print_all_info(self):
        print("-"*30, self.name, "-"*30)
        for animal in self.animals:
            animal.display_info()
        return self
    def feed(self,name):
        for animal in self.animals:
            if name == animal.name:
                animal.feed()
                return self
        print("Animal Not Found")
        return self

class Animal:
    def __init__(self, name,age=3,health =10,happiness=10):
        self.name = name
        self.age = age
        self.health = health
        self.happiness = happiness
        self.type = "Unknown"
    def display_info(self):
        print(f"{self.type}:\t {self.name}, {self.age} years old:\t Health:{self.health}.\t Happiness:{self.happiness}")
        return self
    def feed(self):
        print(f"{self.name} is satiated.")
        self.health += 10
        self.happiness+=10
        return self

class Lion(Animal):
    def __init__(self,name,age,health,happiness):
        super().__init__(name,age,health,happiness)
        self.type = "Lion"
        self.origin = "Africa"
    def feed(self):
        print(f"{self.name} ate a nice piece of meat.")
        self.happiness+=5
        self.health+=15
        return self

class Tiger(Animal):
    def __init__(self,name,age,health,happiness):
        super().__init__(name,age,health,happiness)
        self.type = "Tiger"
        self.species = "Sunda"
    def feed(self):
        print(f"{self.name} ate a nice boar.")
        self.health += 20
        self.happiness +=10
        return self

class Bear(Animal):
    def __init__(self,name,age,health,happiness):
        super().__init__(name,age,health,happiness)
        self.type = "Bear"
        self.digest = "Omnivore"
    def feed(self):
        print(f"{self.name} had some salmon, berries and honey.")
        self.health += 15
        self.happiness +=20
        return self



zoo1 = Zoo("John's Zoo")
zoo1.addAnimal("Nala","lion",5,15,10)
zoo1.addAnimal("Simba","lion",4,20,5)
zoo1.addAnimal("Rajah","tiger",happiness=20)
zoo1.addAnimal("Shere Khan","tiger",3,15)
zoo1.addAnimal("Yogi","Bear",10,20,20)
zoo1.addAnimal("Slyvester","Cat",4,8,5)
zoo1.print_all_info()
zoo1.feed("Yogi").feed("Nala").feed("Rajah").feed("Slyvester")
