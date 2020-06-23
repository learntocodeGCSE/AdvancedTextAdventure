from pprint import pprint
import random
import math

class hero:
    def __init__(self, Hhealth, Hattack, Hluck, Hranged, Hdefence, Hmagic, Hname):
        self.health = Hhealth
        self.attack = Hattack
        self.luck = Hluck
        self.ranged = Hranged
        self.defence = Hdefence
        self.magic = Hmagic
        self.name = Hname

    def getHealth(self):
        return self.health
    def getAttack(self):
        return self.attack
    def getLuck(self):
        return self.luck
    def getRanged(self):
        return self.ranged
    def getDefence(self):
        return self.defence
    def getMagic(self):
        return self.magic
    def getName(self):
        return self.name

    def setHealth(self, newHealth):
        self.health = newHealth
    def setAttack(self, newAttack):
        self.attack = newAttack
    def setLuck(self, newLuck):
        self.luck = newLuck
    def setRanged(self, newRanged):
        self.ranged = newRanged
    def setDefence(self, newDefence):
        self.defence = newDefence
    def setMagic(self, newMagic):
        self.magic = newMagic
    def setName(self, newName):
        self.name = newName


    










        
