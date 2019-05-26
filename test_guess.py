import pytest

from guess import get_random_number, Game
import random
from unittest.mock import patch


@patch.object(random, 'randint')
def test_get_random_number(m):
    m.return_value = 17
    assert get_random_number() == 17


@patch("builtins.input", side_effects=[11, '12', 'bob', 12, 5, -1, 21, 7, None])
def test_guess(inp):
    game = Game()
    # good
    # already guessed 11
    with pytest.raises(ValueError):
        game.guess()
#    assert game.guess() == 11
    assert game.guess() == 12
    # not a number
    with pytest.raises(ValueError):
        game.guess()
    # already guessed 12
    with pytest.raises(ValueError):
        game.guess()
    # good
    assert game.guess() == 5
    # out of range values
    with pytest.raises(ValueError):
        game.guess()
    with pytest.raises(ValueError):
        game.guess()
    # good
    assert game.guess() == 7
    # user hit enter
    with pytest.raises(ValueError):
        game.guess()
