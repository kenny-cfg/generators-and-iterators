import itertools


def all_number_generator():
    number = 0
    while True:
        yield number
        number += 1


all_number_generator_with_itertools = itertools.count(start=0, step=1)

even_number_generator = (2 * x for x in all_number_generator())

even_number_square_generator = (x ** 2 for x in even_number_generator)

if __name__ == '__main__':
    sequence = all_number_generator()
    print(next(sequence))
    print(next(sequence))
    print(next(sequence))
    print(next(sequence))
    print(next(sequence))
