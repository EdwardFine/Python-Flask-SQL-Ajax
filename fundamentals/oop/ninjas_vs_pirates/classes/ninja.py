class Ninja:

    def __init__( self , name ):
        self.name = name
        self.strength = 5
        self.speed = 15
        self.health = 100
        self.recover = False
    
    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def light_attack( self , pirate ):
        pirate.health -= self.strength
        return self
    def heavy_attack(self,pirate):
        pirate.health -= self.strength *2.25
        self.recover=True
        return self
    def increaseSpeed(self):
        self.speed += 5
        return self
    def increaseStrength(self):
        self.strength+=5
        return self