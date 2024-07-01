import pytest
from src.engine import card_models, card_structs, cards, game_state


def testPlayerCountLimits():
    with pytest.raises(game_state.PlayerCountError):
        game_state.GameState(['A'])
    with pytest.raises(game_state.PlayerCountError):
        game_state.GameState(['A', 'B', 'C', 'D', 'E'])

