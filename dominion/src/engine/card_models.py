from enum import Enum
from typing import Self

Set = Enum('Set', ['Null', 'Baseset', 'Baseset1', 'Baseset2', 'Intrigue', 'Prosperity',  'Seaside', 'Alchemy', 'Nocturne', 'Plunder'])

class Card:
    _self: Self | None = None
    def __new__(cls):
        if cls._self is None:
            cls._self = super().__new__(cls)
        return cls._self

    def __init__(self, name: str, cost: int, set: Set) -> None:
        self.name: str = name
        self.cost: int = cost
        self.set: Set = set
        
    def __str__(self) -> str:
        return self.name
    
    def calculateCost(self) -> None:
        pass 

    def getSupplyCount(self) -> int:
        return 10

    def onGain(self) -> None:
        pass

    def onPlay(self) -> None:
        pass

    def onDiscard(self) -> None:
        pass

    def onCleanUp(self) -> None:
        pass    

    def onTrash(self) -> None:
        pass

    
class Victory(Card):
    def __init__(self, name: str, cost: int, points: int, set: Set) -> None:
        super().__init__(name, cost, set)
        self.points: int = points
        
    def getPoints(self) -> int:
        return self.points
        
    def getSupplyCount(self, playerCount: int) -> int:
        if playerCount == 2:
            return 8
        return 12


class Curse(Card):
    def __init__(self, name: str, cost: int, set: Set) -> None:
        super().__init__(name, cost, set)
        self.points: int = -1

    def getPoints(self) -> int:
        return self.points

    def getSupplyCount(self, playerCount: int) -> int:
        return 10 * (playerCount - 1)


class Treasure(Card):
    def __init__(self, name: str, cost: int, value: int, set: Set) -> None:
        super().__init__(name, cost, set)
        self.value: int = 0

    def getValue(self) -> int:
        return self.value
    
    def onPlay(self):
        pass


class Loot(Card):
    def getSupplyCount(self) -> int:
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

