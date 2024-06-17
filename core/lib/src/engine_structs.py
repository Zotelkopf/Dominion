from typing import Self, Callable
from random import shuffle
from card_models import *
from cards import *


class EmptySupplyExpection(Exception):
    pass

class WrongSupplyError(ValueError):
    pass

class EmptyDeckExpection(Exception):
    pass


class Cardbuffer:
    def __init__(self) -> None:
        self.cards: list[Card] = []
        self.count: int = 0

    def shuffle(self) -> None:
        shuffle(self.cards)

    def receive(self, card: Card) -> None:
        self.cards.append(card)
        self.count += 1

    def remove(self, card: Card) -> bool:
        if card in self.cards:
            self.cards.remove(card)
            self.count -= 1
            return True
        return False

    def removeTop(self) -> Card | None:
        if self.count <= 0: 
            return None
        self.count -= 1
        return self.cards.pop(0)

    def moveTo(self, card: Card, target: Self) -> None:
        if self.remove(card):
            target.receive(card)
        else:
            raise ValueError

    def dumpTo(self, target: Self) -> None:
        card: Card = self.removeTop()
        while(card is not None):
            target.receive(card)
            card = self.removeTop()

    def FilterInto(self, fn: Callable[[Card], Self], count: int = -1):
        if count < 0:
            card: Card = self.removeTop()
            while(card is not None):
                fn(card).receive(card)
                card = self.removeTop() 
        else:
            for i in range(count):
                card: Card = self.removeTop()
                if card is None:
                    break
                fn(card).receive(card)

            
class SupplyPile(Cardbuffer):
    def __init__(self, card: Card, playerCount: int) -> None:
        self.card: Card = card
        self.count: int = card.getSupplyCount(playerCount)
        self.cards: list[Card] = [self.card] * self.count

    def receive(self, card: Card) -> None:
        if card == self.card:
            super().receive(card)
        else:
            raise WrongSupplyError
    
    def remove(self, card: Card) -> bool:
        if card == self.card:
            super().remove(card)
        else:
            raise WrongSupplyError
        
    def drawTo(self, target: Self) -> None:
        card: Card = self.removeTop()
        if card is not None:
            target.receive(card)
        else:
            raise EmptySupplyExpection
        
    
class Deck(Cardbuffer):
    def addToTop(self, card: Card) -> None:
        self.cards.insert(0, card)
        self.count += 1

    def drawTo(self, target: Self) -> None:
        card: Card = self.removeTop()
        if card is not None:
            target.receive(card)
        else:
            raise EmptyDeckExpection
        

class InPlayBuffer(Cardbuffer):
    pass


class Supply:
    def __init__(self, expansions: list[Set], playerCount: int) -> None:
        self.supplies: dict[Card, SupplyPile] = {}
        self.expansions: list[Set] = expansions
        self.playerCount: int = playerCount

        self.setup(expansions, playerCount)

    def setup(self, expansions: list[Set], playerCount: int) -> None:
        if Set.Alchemy in expansions: self.supplies[Potion()] = SupplyPile(Potion(), playerCount)
        self.supplies[Copper()] = SupplyPile(Copper(), playerCount)
        self.supplies[Silver()] = SupplyPile(Silver(), playerCount)
        self.supplies[Gold()] = SupplyPile(Gold(), playerCount)
        if Set.Prosperity in expansions: self.supplies[Platinum()] = SupplyPile(Platinum(), playerCount)

        self.supplies[Curse()] = SupplyPile(Curse(), playerCount)
        self.supplies[Estate()] = SupplyPile(Estate(), playerCount)
        self.supplies[Duchy()] = SupplyPile(Duchy(), playerCount)
        self.supplies[Province()] = SupplyPile(Province(), playerCount)
        if Set.Prosperity in expansions: self.supplies[Colony()] = SupplyPile(Colony(), playerCount)

        

    def reset(self) -> None:
        self.setup(self.expansions, self.playerCount)        

    def getSupplyOf(self, card: Card) -> SupplyPile:
        return self.supplies[card]
    
    def getCardsInSupply(self) -> list[Card]:
        return self.supplies.keys
    
    async def gain(self, card: Card, location: Cardbuffer) -> None:
        try:
            self.getSupplyOf(card).drawTo(location)
            await card.onGain()
        except EmptySupplyExpection:
            pass

    async def buy(self, card: Card) -> None:
        pass
    
    

class CardConditions:
    def __init__(self) -> None:
        self.expansions: list[Set] = []
        self.minExpansions: int = 0
        self.maxExpansions: int = 0
        self.minCost: int = 0
        self.maxCost: int = 0

    def allowsFor(card: Card) -> bool:
        pass



class Player:
    def __init__(self) -> None:
        self.points: int = 0

        self.deck: Deck = Deck()
        self.hand: Cardbuffer = Cardbuffer()
        self.discardPile: Cardbuffer = Cardbuffer()




class PlayerContoller:
    def __init__(self) -> None:
        pass

    

