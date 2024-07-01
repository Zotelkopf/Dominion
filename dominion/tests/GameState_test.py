import pytest
from src.engine.game_state import GameState, PlayerCountError


def testPlayerCountLimits() -> None:
    with pytest.raises(PlayerCountError):
        GameState(['A'])
    with pytest.raises(PlayerCountError):
        GameState(['A', 'B', 'C', 'D', 'E'])

