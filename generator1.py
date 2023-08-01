# A simple generator function
def my_gen():
    n = 1
    print('This is printed first')
    # Generator function contains yield statements
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n


class GeneratorClassEquivalent:
    def __iter__(self):
        self.n = 1

    def __next__(self):
        if self.n == 1:
            print('This is printed first')
        if self.n == 2:
            print('This is printed second')
        if self.n == 3:
            print('This is printed third')
        number_to_return = self.n
        self.n += 1
        return number_to_return


if __name__ == '__main__':
    g = my_gen()
    next(g)
    next(g)
    next(g)

    # this will throw an error
    # next(g)