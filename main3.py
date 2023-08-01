class EvenNumbers:

    def __iter__(self):
        self.num = 0
        return self

    def __next__(self):
        next_num = self.num
        self.num += 2
        return self.num

for number in EvenNumbers():
    print(number)

# run code
#
# evens = EvenNumbers()
# even_iter = iter(evens)
#
# print(next(even_iter))
# print(next(even_iter))
# print(next(even_iter))
# print(next(even_iter))