import math
from enum import Enum
from card_models import Card, Treasure, Action
from card_structs import Cardbuffer, Deck, InPlayBuffer, CardConditions


Phase = Enum('Phase', ['Action', 'Buy', 'CleanUp'])


class Turn:
    def __init__(self) -> None:
        self.phase: Phase = Phase.Action
        self.actions: int = 1
        self.buys: int = 1
        self.coins: int = 0
        self.potions: int = 0


class Player:
    def __init__(self, name: str) -> None:
        self.name = name
        self.controller: PlayerController = PlayerController()
        self.points: int = 0
        self.deck: Deck = Deck()
        self.hand: Cardbuffer = Cardbuffer()
        self.discard: Cardbuffer = Cardbuffer()

    def hasActions(self) -> bool:
        for card in self.hand:
            if isinstance(card, Action):
                return True
        return False
    
    def hasTreasures(self) -> bool:
        for card in self.hand:
            if isinstance(card, Treasure):
                return True
        return False

    def shuffle(self) -> None:
        self.discard.dumpTo(self.deck)
        self.deck.shuffle()

    def gain(self, card: Card) -> None:
        self.deck.receive(card)

    def draw(self, count: int = 1) -> None:
        for i in range(count):
            if not self.deck.drawTo(self.hand):
                self.shuffle()
                if not self.deck.drawTo(self.hand):
                    break

    def playAction(self, card: Action) -> None:
        self.hand.moveTo(card, self.inPlay)
        card.onPlay()
    
    def playTreasure(self, card: Treasure) -> None:
        self.hand.moveTo(card, self.inPlay)
        card.onPlay()

    def makeTurn(self, turn: Turn, inPlay: InPlayBuffer) -> None:
        pass
    

class PlayerController:
    def confirmAction(self, prompt: str, context: Card) -> bool:
        return self.askQuestion(context, prompt, ['Yes', 'No']) == 'Yes'

    def askQuestion(self, context: Card, prompt: str, options: list[str]) -> str:
        return ''

    def selectCardsFromCards(self, context: Card, prompt: str, cards: list[Card], 
                             min: int = 0, max: int = math.inf) -> list[Card]:
        return []
    
    def selectCardsFromBuffer(self, context: Card, prompt: str, buffer: Cardbuffer, 
                              conditions: CardConditions, min: int = 0, max: int = math.inf) -> list[Card]:
        return []
    
    def selectCardFromCards(self, context: Card, prompt: str, cards: list[Card], 
                            optional: bool = False) -> Card | None:
        min = 0 if optional else 1
        card = self.selectCardsFromCards(context, prompt, cards, min, 1)
        return card[0] if card else None
    
    def selectCardFromBuffer(self, context: Card, prompt: str, buffer: Cardbuffer, 
                             conditions: CardConditions, optional: bool = False) -> Card | None:
        min = 0 if optional else 1
        card = self.selectCardsFromBuffer(context, prompt, buffer, conditions, min, 1)
        return card[0] if card else None

