from engine_structs import *


class GameEngine:
    def __init__(self) -> None:
        self.trashPile = Cardbuffer()
        self.supply = Supply()

        self.gameOver = False

        self.players = []

