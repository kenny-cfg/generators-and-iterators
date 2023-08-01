nums = [2, 4, 1, 9, 6]

nums_iter = iter(nums)

for number in nums_iter:
    print(number)


# while True:
#     try:
#         print(next(nums_iter))
#     except StopIteration:
#         print('End of list')
#         break