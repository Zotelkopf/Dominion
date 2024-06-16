from enum import Enum

Set = Enum('Set', ['Null', 'Baseset', 'Intrigue', 'Seaside', 'Alchemy', 'Nocturne', 'Plunder'])

class Card:
    def __init__(self):
        self.name = ""
        self.cost = 0
        self.set = Set.Null
        
    def __str__(self):
        return self.name
    
    def recalculateCost(self):
        pass 

    def getSupplyCount(self):
        return 10

    def onGain(self):
        pass

    def onPlay(self):
        pass

    def onDiscard(self):
        pass

    def onTrash(self):
        pass

    
class Victory(Card):
    def __init__(self):
        super().__init__()
        self.points = 0
        
    def getPoints(self):
        return self.points
        
    def getSupplyCount(self, playerCount):
        return 8 if playerCount == 2 else 12

class Curse(Card):
    def __init__(self):
        super().__init__()
        self.points = -1

    def getPoints(self):
        return self.points

    def getSupplyCount(self, playerCount):
        return 10 * (playerCount - 1)

class Treasure(Card):
    def __init__(self):
        super().__init__()
        self.value = 0

    def getValue(self):
        return self.value
    
    def onPlay(self):
        pass

class Loot(Card):
    def getSupplyCount(self):
        return 2

class Action(Card):
    pass

class Reaction(Card):
    pass

class Attack(Card):
    pass

class Duration(Card):
    pass

class Command(Card):
    pass

class Night(Card):
    pass

