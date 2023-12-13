def square_numbers(nums):
    for i in nums:
        if i % 2 == 0:
            yield (f"{i} -> {i * i}")
        
my_nums = square_numbers([1,2,3,4,5,6])
# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums))

# for val in my_nums:
    # print(val)

# (expression for item in iterable condition)
square_nums = (x * x for x in range(1, 10) if x % 2 == 0)

for sq in square_nums:
    print(sq)