import random

START, END = 1, 20

def hello_name(name):
    return str('hello ' + name)

def get_random_number():
    """Get a random number between START and END,
    returns int"""
    return random.randint(START, END)


def print_header():
    print('--------------------------------')
    print('          PyTest App')
    print('--------------------------------')
    print()


def main():
    print_header()
    hello = hello_name('bob')

    print('Type: {} Message: {}'.format(type(hello), hello))

    ranint = get_random_number()
    print('Random Int: {}'.format(ranint))


if __name__ == '__main__':
    main()

