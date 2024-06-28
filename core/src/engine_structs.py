from enum import Enum


Phase = Enum('Phase', ['Action', 'Buy', 'CleanUp'])
   

class Turn:
    def __init__(self) -> None:
        self.phase: Phase = Phase.Action
        self.actions: int = 1
        self.buys: int = 1
        self.coins: int = 0
        self.potions: int = 0


class PlayerController:
    pass





