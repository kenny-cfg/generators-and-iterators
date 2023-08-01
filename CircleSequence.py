class CircleSequence:

    def __init__(self, iterable, number_to_return):
        self.iterable = iterable
        self.number_to_return = number_to_return
        pass

    def __iter__(self):
        self.index = 0
        self.number_returned = 0
        return self

    def __next__(self):
        if self.number_returned >= self.number_to_return:
            raise StopIteration('The end')
        if self.index >= len(self.iterable):
            self.index = 0
        return_value = self.iterable[self.index]
        self.index += 1
        self.number_returned += 1
        return return_value