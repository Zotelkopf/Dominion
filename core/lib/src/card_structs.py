import math
from random import shuffle
from typing import Self, Callable
from card_models import Card, Set
from cards import *


class WrongSupplyError(ValueError):
    pass


class Cardbuffer:
    def __init__(self) -> None:
        self.cards: list[Card] = []
        self.count: int = 0

    def __getitem__(self, index: int) -> Card:
        return self.cards[index]
    
    def __len__(self) -> int:
        return len(self.cards)

    # shuffles the buffer
    def shuffle(self) -> None:
        shuffle(self.cards)

    # adds given card to the bottom of the buffer
    def receive(self, card: Card) -> None:
        self.cards.append(card)
        self.count += 1

    # deletes given card and returns False if the card isn't in the buffer
    def remove(self, card: Card) -> bool:
        if card in self.cards:
            self.cards.remove(card)
            self.count -= 1
            return True
        return False

    # deletes and returns the first card or None if the buffer is empty
    def removeTop(self) -> Card | None:
        if self.count <= 0: 
            return None
        self.count -= 1
        return self.cards.pop(0)

    # moves a given card from this to a given target, returns False if the card isn't in the buffer
    def moveTo(self, card: Card, target: Self) -> bool:
        if self.remove(card):
            target.receive(card)
            return True
        return False

    # moves all cards to a given target
    def dumpTo(self, target: Self) -> None:
        card: Card = self.removeTop()
        while(card is not None):
            target.receive(card)
            card = self.removeTop()

    # moves count/all (for count = -1) cards to target returned by fn
    def FilterInto(self, fn: Callable[[Card], Self], count: int = -1) -> None:
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
            return super().remove(card)
        else:
            raise WrongSupplyError
    
    # moves the first card to a given target, returns False if the buffer is empty
    def drawTo(self, target: Self) -> bool:
        card: Card | None = self.removeTop()
        if card is not None:
            target.receive(card)
            return True
        return False
        
    
class Deck(Cardbuffer):
    # adds a given card to the top of the buffer
    def addToTop(self, card: Card) -> None:
        self.cards.insert(0, card)
        self.count += 1

    # moves the first card to a given target, returns False if the buffer is empty
    def drawTo(self, target: Self) -> bool:
        card: Card | None = self.removeTop()
        if card is not None:
            target.receive(card)
            return True
        return False
        

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
        self.getSupplyOf(card).drawTo(location)
        await card.onGain()

    async def buy(self, card: Card) -> None:
        pass
    
    
class CardConditions:
    def __init__(self, sets: list[Set] = [], minExpansions: int = 0, maxExpansions: int = 0, 
                 minCost: int = -1, maxCost: int = math.inf, requiredCards: list[Card] = [], 
                 bannedCards: list[Card] = []) -> None:
        self.sets: list[Set] = sets
        self.minExpansions: int = minExpansions
        self.maxExpansions: int = maxExpansions
        self.minCost: int = minCost
        self.maxCost: int = maxCost
        self.requiredCards: list[Card] = requiredCards
        self.bannedCards: list[Card] = bannedCards

    def allowsFor(self, card: Card) -> bool:
        if card in self.bannedCards: 
            return False
        if self.requiredCards and not card in self.requiredCards:
            return False
        if self.sets and not card.set in self.sets:
            return False
        cost: int = card.calculateCost()
        if cost < self.minCost:
            return False
        if cost > self.maxCost:
            return False
        return True