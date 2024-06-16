from typing import Self
from random import shuffle
from card_models import *


class Cardbuffer:
    def __init__(self) -> None:
        self.cards: list[Card] = []

    def receive(self, card: Card) -> None:
        self.cards.append(card)

    def addToTop(self, card: Card) -> None:
        self.cards.insert(0, card)

    def shuffle(self) -> None:
        shuffle(self.cards)

    def moveTo(self, card: Card, target: Self) -> None:
        if card in self.cards:
            target.receive(card)
            self.cards.remove(card)

    def drawTo(self, target: Self) -> None:
        if len(self.cards) != 0:
            target.receive(self.cards.pop(0))

    def dumpTo(self, target: Self) -> None:
        for card in self.cards:
            target.receive(card)
        self.cards.clear()
            

class SupplyPile(Cardbuffer):
    def __init__(self, card: Card, playerCount: int) -> None:
        self.cards: list[Card] = [card] * card.getSupplyCount(playerCount)
        self.card = card

    def receive(self, card: Card) -> None:
        if card == self.card:
            super().receive(card)
        else:
            raise ValueError
        

class InPlayBuffer(Cardbuffer):
    pass


class Supply:
    def __init__(self) -> None:
        pass


class Player:
    def __init__(self) -> None:
        pass


class PlayerContoller:
    def __init__(self) -> None:
        pass

    

