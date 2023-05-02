class Pirate:

    def __init__( self , name ):
        self.name = name
        self.strength = 10
        self.speed = 5
        self.health = 100
        self.recover = False

    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def light_attack ( self , ninja ):
        ninja.health -= self.strength
        return self
    def heavy_attack(self,ninja):
        ninja.health -= self.strength *2.25
        self.recover=True
        return self
    def increaseSpeed(self):
        self.speed += 5
        return self
    def increaseStrength(self):
        self.strength+=5
        return self