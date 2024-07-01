from src.engine.card_models import Card
from src.engine.card_structs import Cardbuffer, Deck


def makeBuffer(cards: list[Card]) -> Cardbuffer:
    buffer: Cardbuffer = Cardbuffer()
    buffer.cards = cards
    buffer.count = len(cards) 
    return buffer

def makeDeck(cards: list[Card]) -> Deck:
    deck: Deck = Deck()
    deck.cards = cards
    deck.count = len(cards) 
    return deck

def bufferHasCards(buffer: Cardbuffer, cards: list[Card]) -> bool:
    if buffer.count == len(cards) and buffer.cards == cards:
        return True
    return False