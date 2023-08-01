class OddNumbers:
    def __iter__(self): # Sets up the iteration when it starts
        self.num = 1
        return self

    def __next__(self): # Returns the next number in the sequence
        next_number = self.num
        self.num += 2
        return next_number


if __name__ == '__main__':
    sequence = OddNumbers()
    for number in sequence:
        print(number)
    # is equivalent to
    iterable = iter(sequence)
    while True:
        try:
            print(next(sequence))
        except StopIteration:
            break
    # is equivalent to
    iterable = sequence.__iter__()
    while True:
        try:
            print(sequence.__next__())
        except StopIteration:
            break