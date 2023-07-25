import random
import math

class Warrior:
    # initialize warrior
    def __init__(self, name="Warrior", maxHealth=0, maxAttack=0, maxBlock=0):
        self.name = name
        self.maxHealth = maxHealth
        self.maxAttack = maxAttack
        self.maxBlock = maxBlock

    def attack(self):
        attackAmt = self.maxAttack * (random.random() + .5)

        return attackAmt

    def block(self):
        blockAmt = self.maxBlock * (random.random() + .5)

        return blockAmt

class Battle:

    def startFight(self, warrior1, warrior2):
        while True:
            if self.getAttackResult(warrior1, warrior2) == "Game Over":
                print("Game Over")
                break
            if self.getAttackResult(warrior2, warrior1) == "Game Over":
                print("Game Over")
                break

    @staticmethod
    def getAttackResult(warriorA, warriorB):
        warriorAAttackAmt = warriorA.attack()

        warriorBBlockAmt = warriorB.block()

        damage2WarriorB = math.ceil(warriorAAttackAmt - warriorBBlockAmt)

        warriorB.maxHealth = warriorB.maxHealth - damage2WarriorB

        print("{} attack {} and deals {} damage".format(warriorA.name, warriorB.name, damage2WarriorB))

        print("{} is down to {} health".format(warriorB.name, warriorB.maxHealth))

        if warriorB.maxHealth <= 0:
            print("{} has Died and {} is Victorious".format(warriorB.name, warriorA.name))

            return "Game Over"
        else:
            return "Fight Again"

def main():
    maximus = Warrior("Maximus", 50, 20, 10)
    gelaxon = Warrior("Galaxon", 50, 20, 10)

    battle = Battle()

    battle.startFight(maximus, gelaxon)

main()
