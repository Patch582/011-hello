
def hello_name(name):
    return str('hello ' + name)


def print_header():
    print('--------------------------------')
    print('          PyTest App')
    print('--------------------------------')
    print()


def main():
    print_header()
    hello = hello_name('bob')

    print('Type: {} Message: {}'.format(type(hello), hello))


if __name__ == '__main__':
    main()

