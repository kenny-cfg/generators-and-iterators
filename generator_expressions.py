my_list = [1, 3, 6, 10]

# NOTE: we square each term using list comprehension
new_list = [x ** 2 for x in my_list]

# NOTE: same thing can be done using a generator expression
# generator expressions are surrounded by parenthesis () !
generator = (x ** 2 for x in my_list)

if __name__ == '__main__':
    print(new_list)
    print(generator)

    # use next() or for loop to get items from generator

    for i in generator:
        print(i)