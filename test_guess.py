from guess import get_random_number
import random
from unittest.mock import patch


@patch.object(random, 'randint')
def test_get_random_number(m):
    m.return_value = 17
    assert get_random_number() == 17