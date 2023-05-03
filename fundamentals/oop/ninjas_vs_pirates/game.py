from classes.characters import Ninja, Pirate
import random

def printMoves():
    print(
        "\n========================\n"
        "1.Basic Attack\n"
        "2.Heavy Attack\n"
        "3.Speed Increase\n"
        "4.Strength Increase\n"
        "========================\n")

def printStats():
    print(
        f"\nName:\t\t{player.name}\t{comp.name}\n"
        f"Health:\t\t{player.health}\t{comp.health}\n"
        f"Speed:\t\t{player.speed}\t{comp.speed}\n"
        f"Strength:\t{player.strength}\t{comp.strength}\n"
    )

def isEvaded(char):
    chance = random.randint(1,100)
    if chance <= char.speed:
        return True
    else:
        return False

def processMenuChoice(input,attacker,defender):
    if input ==1:
        if not isEvaded(defender):
            attacker.light_attack(defender)
            print(f"{attacker.name} hit {defender.name} with a light attack.")
        else:
            print(f"{defender.name} dodged {attacker.name}'s light attack.")
        return True
    elif input ==2:
        attacker.recover = True
        if not isEvaded(defender):
            attacker.heavy_attack(defender)
            print(f"{attacker.name} hit {defender.name} with a heavy attack.")
        else:
            print(f"{defender.name} dodged {attacker.name}'s heavy attack.")
        return True
    elif input ==3:
        if(attacker.speed <=50):
            print(f"{attacker.name} performs some speed training.")
            attacker.increaseSpeed()
            return True
        else:
            print(f"{attacker.name} has reached max speed, choose another option.")
            return False
    elif input ==4:
        if(attacker.strength <=25):
            print(f"{attacker.name} performs some strength training.")
            attacker.increaseStrength()
            return True
        else:
            print(f"{attacker.name} has reached max strength, choose another option.")
            return False
    else:
        print("Input not a choice. Please input the number associated with the menu.")
        return False

def checkRecover(char):
    if char.recover:
        char.recover = False
        return False
    else:
        return True

def playerTurn():
    successful=False
    if checkRecover(player):
        while not successful:
            printMoves()
            try:
                successful = processMenuChoice(int(input()),player,comp)
            except ValueError:
                pass
    else:
        print(f"{player.name} is recovering after that heavy attack!")

def compTurn():
    successful = False
    if checkRecover(comp):
        while not successful:
            successful = processMenuChoice(random.randint(1,4),comp,player)
    else:
        print(f"{comp.name} is recovering after that heavy attack!")

def checkDeath():
    if player.health <=0 or comp.health <=0:
        return True
    else:
        return False

def processWinner():
    if player.health <=0 and comp.health >0:
        print(f"{comp.name} wins the game! Better luck next time.")
        return True
    elif comp.health <=0 and player.health >0:
        print(f"Congratulations {player.name}, you win!")
        return True
    elif comp.health <=0 and player.health <=0:
        print("It's a tie!")
        return True
    else:
        return False

choice = ""
while True:
    if choice == "ninja":
        player = Ninja(input("What is your ninja's name? "))
        comp = Pirate(input("What is the pirate's name? "))
        break
    elif choice == "pirate":
        player = Pirate(input("What is your pirate's name? "))
        comp = Ninja(input("What is the ninja's name? "))
        break
    choice=input("Do you want to play as a ninja or a pirate? ").lower().strip()

while True:
    printStats()
    playerTurn()
    if checkDeath():
        processWinner()
        break
    compTurn()
    if checkDeath():
        processWinner()
        break