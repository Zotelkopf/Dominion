from engine_structs import *


class Engine:
    def __init__(self) -> None:
        self.trashPile = Cardbuffer()
        self.supply = Supply()

        self.gameover = False

        self.players = []

