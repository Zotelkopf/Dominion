from typing import Self, Callable
from random import shuffle
from card_models import *
from core.lib.src.card_models import Card


class Cardbuffer:
    def __init__(self) -> None:
        self.cards: list[Card] = []
        self.count = 0

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

    # needed for all Cardbuffers?
    def drawTo(self, target: Self) -> None:
        card: Card = self.removeTop()
        if card is not None:
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
        self.card = card
        self.count = card.getSupplyCount(playerCount)
        self.cards: list[Card] = [self.card] * self.count

    def receive(self, card: Card) -> None:
        if card == self.card:
            super().receive(card)
        else:
            raise ValueError
    
    def remove(self, card: Card) -> bool:
        if card == self.card:
            super().remove(card)
        else:
            raise ValueError
        
    
class Deck(Cardbuffer):
    def addToTop(self, card: Card) -> None:
        self.cards.insert(0, card)
        self.count += 1
        

class InPlayBuffer(Cardbuffer):
    pass


class Supply:
    def __init__(self) -> None:
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

    

