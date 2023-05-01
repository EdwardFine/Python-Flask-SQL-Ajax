from ninja import Ninja
import pet

if __name__=="__main__":
    pet1 = pet.Cat("Moira","Cat","Headbutt")
    pet2 = pet.Dog("Kooper","Dog","Shake")
    pet3 = pet.Rat("Gary","Rat","Attack")
    ninja1 = Ninja("Edward","Fine",10,15,pet1)

    ninja1.walk(2)
    ninja1.feed(5)
    ninja1.bathe()
    pet1.display_stats()