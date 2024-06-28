from card_models import Treasure, Action
from cards import Copper, Estate
from card_structs import Cardbuffer, Deck, InPlayBuffer, Supply
from engine_structs import PlayerController, Turn, Phase


class GameEngine:
    def __init__(self) -> None:
        self.trashPile = Cardbuffer()
        self.supply = Supply()

        self.gameOver = False

        self.players = []


class Player:
    def __init__(self, controller: PlayerController) -> None:
        self.controller: PlayerController = controller
        self.points: int = 0
        self.deck: Deck = Deck()
        self.hand: Cardbuffer = Cardbuffer()
        self.discard: Cardbuffer = Cardbuffer()
        self.inPlay: InPlayBuffer = InPlayBuffer()

        # TODO: move to Engine
        for i in range(3): self.deck.receive(Estate())
        for i in range(7): self.deck.receive(Copper())
        self.shuffle()

    def hasActions(self) -> bool:
        for i in range(len(self.hand)):
            if self.hand[i] is Action:
                return True
        return False
    
    def hasTreasures(self) -> bool:
        for i in range(len(self.hand)):
            if self.hand[i] is Treasure:
                return True
        return False

    def shuffle(self) -> None:
        self.discardPile.dumpTo(self.deck)
        self.deck.shuffle()

    def draw(self, count: int = 1) -> None:
        for i in range(count):
            if not self.deck.drawTo(self.hand):
                self.shuffle()
                if not self.deck.drawTo(self.hand):
                    break

    async def playAction(self, card: Action) -> None:
        self.hand.moveTo(card, self.inPlay)
        await card.onPlay()
    
    async def playTreasure(self, card: Treasure) -> None:
        self.hand.moveTo(card, self.inPlay)
        await card.onPlay()

    async def takeTurn(self) -> None:
        turn: Turn = Turn()
        inPlay: InPlayBuffer = InPlayBuffer()

        while(turn.actions > 0 and self.hasActions()):
            # TODO: playercontroller
            card: Action | None = Action()
            if card is None:
                break
            await self.playAction(card)

        turn.phase = Phase.Buy

        while(self.hasTreasures):
            treasures: list[Treasure] = []
            if len(treasures) == 0:
                break
            for treasure in treasures:
                await self.playTreasure(treasure)
