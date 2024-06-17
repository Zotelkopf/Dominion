from card_models import *
from core.lib.src.card_models import Set

# Basic Supply Cards

class Potion(Treasure):
    def __init__(self) -> None:
        super().__init__('Trank', 4, 0, Set.Alchemy)

    def getSupplyCount(self, playerCount: int) -> int:
        return 16

class Copper(Treasure):
    def __init__(self) -> None:
        super().__init__('Kupfer', 0, 1, Set.Baseset)
    
    def getSupplyCount(self, playerCount: int) -> int:
        return 60 - 7 * playerCount
    
class Silver(Treasure):
    def __init__(self) -> None:
        super().__init__('Silber', 3, 2, Set.Baseset)

    def getSupplyCount(self) -> int:
        return 40
    
class Gold(Treasure):
    def __init__(self) -> None:
        super().__init__('Gold', 6, 3, Set.Baseset)

    def getSupplyCount(self) -> int:
        return 30
    
class Platinum(Treasure):
    def __init__(self) -> None:
        super().__init__('Platin', 9, 5, Set.Baseset)

    def getSupplyCount(self) -> int:
        return 12

class Curse(Curse):
    def __init__() -> None:
        super().__init__('Fluch', 0, Set.Baseset)

class Estate(Victory):
    def __init__(self) -> None:
        super().__init__('Anwesen', 2, 1, Set.Baseset)

class Duchy(Victory):
    def __init__(self) -> None:
        super().__init__('Herzogtum', 5, 3, Set.Baseset)

class Province(Victory):
    def __init__(self) -> None:
        super().__init__('Provinz', 8, 6, Set.Baseset)

class Colony(Victory):
    def __init__(self) -> None:
        super().__init__('Kolonie', 11, 10, Set.Prosperity)

# Kingdom Cards - Base Set

class Cellar(Action):
    def __init__() -> None:
        super().__init__('Keller', 2, Set.Baseset)

class Chapel(Action):
    def __init__() -> None:
        super().__init__('Kapelle', 2, Set.Baseset)

class Moat(Action, Reaction):
    def __init__() -> None:
        super().__init__('Burggraben', 2, Set.Baseset)

class Village(Action):
    def __init__() -> None:
        super().__init__('Dorf', 3, Set.Baseset)

class Workshop(Action):
    def __init__() -> None:
        super().__init__('Werkstatt', 3, Set.Baseset)

class Gardens(Victory):
    def __init__() -> None:
        super().__init__('Gärten', 4, 0, Set.Baseset)

class Moneylender(Action):
    def __init__() -> None:
        super().__init__('Geldleiher', 4, Set.Baseset)

class Remodel(Action):
    def __init__() -> None:
        super().__init__('Umbau', 4, Set.Baseset)

class Smithy(Action):
    def __init__() -> None:
        super().__init__('Schmiede', 4, Set.Baseset)

class ThroneRoom(Action):
    def __init__() -> None:
        super().__init__('Thronsaal', 4, Set.Baseset)

class Bureaucrat(Action, Attack):
    def __init__() -> None:
        super().__init__('Bürokrat', 4, Set.Baseset)

class Milita(Action, Attack):
    def __init__() -> None:
        super().__init__('Miliz', 4, Set.Baseset)

class CouncilRoom(Action):
    def __init__() -> None:
        super().__init__('Ratsversammlung', 5, Set.Baseset)

class Festival(Action):
    def __init__() -> None:
        super().__init__('Jahrmarkt', 5, Set.Baseset)

class Laboratory(Action):
    def __init__() -> None:
        super().__init__('Laboratorium', 5, Set.Baseset)

class Library(Action):
    def __init__() -> None:
        super().__init__('Bibliothek', 5, Set.Baseset)

class Market(Action):
    def __init__() -> None:
        super().__init__('Markt', 5, Set.Baseset)

class Mine(Action):
    def __init__() -> None:
        super().__init__('Mine', 5, Set.Baseset)

class Witch(Action, Attack):
    def __init__() -> None:
        super().__init__('Hexe', 5, Set.Baseset)

class Chancellor(Action):
    def __init__() -> None:
        super().__init__('Kanzler', 3, Set.Baseset1)

class Woodcutter(Action):
    def __init__() -> None:
        super().__init__('Holzfäller', 3, Set.Baseset1)

class Feast(Action):
    def __init__() -> None:
        super().__init__('Festmahl', 4, Set.Baseset1)

class Spy(Action, Attack):
    def __init__() -> None:
        super().__init__('Spion', 4, Set.Baseset1)

class Thief(Action, Attack):
    def __init__() -> None:
        super().__init__('Dieb', 4, Set.Baseset1)

class Adventurer(Action):
    def __init__() -> None:
        super().__init__('Abenteurer', 6, Set.Baseset1)

class Harbringer(Action):
    def __init__() -> None:
        super().__init__('Vorbotin', 3, Set.Baseset2)

class Merchant(Action):
    def __init__() -> None:
        super().__init__('Händlerin', 3, Set.Baseset2)

class Vassal(Action):
    def __init__() -> None:
        super().__init__('Vasall', 3, Set.Baseset2)

class Poacher(Action):
    def __init__() -> None:
        super().__init__('Wilddiebin', 4, Set.Baseset2)

class Sentry(Action):
    def __init__() -> None:
        super().__init__('Torwächterin', 5, Set.Baseset2)

class Bandit(Action, Attack):
    def __init__() -> None:
        super().__init__('Banditin', 5, Set.Baseset2)

class Artisan(Action):
    def __init__() -> None:
        super().__init__('Töpferei', 6, Set.Baseset2)
