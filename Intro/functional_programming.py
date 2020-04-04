# Make pure functions - don't interact with outside world
# Methods live inside class
# Functional programming (don't combine data with functions)

from functools import reduce

my_list = [1, 2, 3, 4, 5, 6]
your_list = [10, 20, 30, 40, 50, 60]
their_list = [6, 5, 4, 3, 2, 1]


def multiply_by2(li):
    new_list = []
    for item in li:
        new_list.append(item * 2)
    return new_list


def mult(item):
    return item * 2


def only_odd(item):
    return item % 2


def accumulator(acc, item):
    print(acc, item)
    return acc + item


# map, filter, zip, and reduce
# my_list doesn't change (pass function or use lambda)
print(list(map(lambda x: x * 2, my_list)))

print(my_list)

print(list(filter(lambda x: x % 2, my_list)))

# takes two iterables and zips together into tuples
# can do with multiple lists
print(list(zip(my_list, your_list, their_list)))

# the 0 is sets the first value, or can ignore
print(reduce(lambda x, y: x + y, my_list, 10))
# print((reduce(accumulator, my_list, 0)))

# lambda functions
# anonymous functions - don't need to name because using once

a = [(0, 2), (9, 9), (4, 3), (10, -1)]

a.sort(key=lambda x: x[1])
print(a)

# LIST COMPREHENSIONS - UNIQUE TO PYTHON
# [param for param in iterable]

a_list = [char for char in 'hello']
b_list = [num for num in range(0, 100)]
c_list = [num ** 2 for num in range(0, 100)]
d_list = [num ** 2 for num in range(0, 100) if num % 2 == 0]
print(a_list)
print(b_list)
print(c_list)
print(d_list)

# way to quickly create lists in python

# can do set and dictionary comprehensions

# able to do set comprehensions/simliar to list
my_set = {char for char in 'hello'}

# dictionary comprehensions
my_dict = {key: value ** 2 for key, value in enumerate(range(0, 100)) if value%2==0}

other_dict = {num:num*2 for num in [1,2,3]}
print(my_dict)


dup_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
duplicates = list(set([x for x in dup_list if dup_list.count(x) > 1]))
print(duplicates)
