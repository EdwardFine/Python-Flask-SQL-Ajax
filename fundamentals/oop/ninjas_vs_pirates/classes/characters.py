class Character:
    def __init__( self , name ):
        self.name = name
    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")
    def light_attack( self , defender ):
        defender.health -= self.strength
        return self
    def heavy_attack(self,defender):
        defender.health -= self.strength *2.25
        return self
    def increaseSpeed(self):
        self.speed += 5
        return self
    def increaseStrength(self):
        self.strength+=5
        return self

class Ninja(Character):
    def __init__(self,name):
        super().__init__(name)
        self.strength = 5
        self.speed = 15
        self.health = 100
        self.recover = False

class Pirate(Character):
    def __init__(self,name):
        super().__init__(name)
        self.strength = 10
        self.speed = 5
        self.health = 100
        self.recover = False