from card_structs import Cardbuffer, InPlayBuffer, Supply
from card_models import Card, Victory, Treasure, Action
from cards import Estate, Copper
from game_structs import Player, Turn


class PlayerCountError(Exception):
    pass
   

class GameState:
    def __init__(self, players: list[str]) -> None:
        self.playerCount: int = len(players)
        if self.playerCount < 2 or self.playerCount > 4: raise PlayerCountError()
        self.players: list[Player] = []
        for i, player in enumerate(players):
            self.players.append(Player(player))
            for j in range(3): self.players[i].gain(Estate())
            for j in range(7): self.players[i].gain(Copper())
            self.players[i].shuffle()
            self.players[i].draw(5)
        self.currentPlayer: Player = self.players[0]

        self.trash: Cardbuffer = Cardbuffer()
        self.supply: Supply = Supply([], self.playerCount)

        self.turnCount: float = 0.0

    def makeTurn(self) -> None:
        self.turnCount += 1 / self.playerCount
        turn = Turn()
        inPlay: InPlayBuffer = InPlayBuffer()
        self.currentPlayer.makeTurn(turn, inPlay, self.log)

        

    def reset(self) -> None:
        pass



