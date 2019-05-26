from hello_name import hello_name, get_random_number
import random
from unittest.mock import patch


def test_hello_name():
    assert hello_name('bob') == 'hello bob'
    assert hello_name('bob') == 'hello bob'


@patch.object(random, 'randint')
def test_get_random_number(m):
    m.return_value = 17
    assert get_random_number() == 17

