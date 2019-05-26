import random

START, END = 1, 20


def get_random_number():
    """Get a random number between START and END,
    returns int"""
    return random.randint(START, END)


class Game:
    """Number guess class, make it callable to initiate game"""

    def __init__(self):
        """Init _guesses, _answer, _win to set(), get_random_number(), False"""
        self._guesses = set()
        self._answer = get_random_number()
        self._win = False

    def guess(self):
        """Ask user for input, convert to int, raise ValueError outputting the following errors when applicable:
        'Please enter a number'
        'Should be a number'
        'Number not in range'
        'Already guessed'
        If all good return the int"""

        guess = input('Guess a number between {} and {}'.format(START, END))
        if not guess:
            raise ValueError('Please enter a number')
        try:
            guess = int(guess)
        except ValueError:
            raise ValueError('Should be a number')

        if guess not in range(START, END+1):
            raise ValueError('Number not in range')

        if guess not in self._guesses:
            raise ValueError('Already guessed')

        self._guesses.add(guess)
        return guess

    def _validate_guess(self, guess):
        pass


game = Game()
game