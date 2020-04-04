# VARIABLES

iq = 190  # stored as binary representation
user_age = iq / 4
print(iq)
print(user_age)

# assigning a variable is called binding


# BestPractices for Variables
# snake_case
# start with lowercase or underscore
# letters, numbers, underscores
# Case sensitive
# Don't overwrite keywords - eg. print
# Make variables descriptive

# different due to case sensitive
_user_iq3 = 0
_user_IQ3 = 0

# underscore signifies private variable

# ALL CAPITAL IS A CONSTANT
PI = 3.14

# two underscore is called Dunder, meant to be left alone

a, b, c = 1, 2, 3

# augmented assignment operator

some_value = 5
some_value = some_value * 2
print(some_value)

# STRINGS

print(type("Hello"))

long_string = '''
This
is
a
long
string
'''

print(type(long_string))

first_name = 'Alex'
last_name = 'Erling'
full_name = first_name + ' ' + last_name
print(full_name)

# type conversion
print(type(str(100)))

# string concatenation
# only works with strings unless you convert type

# Escape Sequence - \    \n == new line \t == tab

weather = 'it\'s sunny'
print(weather)

name = 'Johnny'
age = 55

# adding f to beginning for formatted string
print(f'Hi {name}. You are {age} years old')

# Other format options
print('Hi {}. You are {} years old'.format('Johnny', '55'))
print('Hi {}. You are {} years old'.format(name, age))
print('Hi {new_name}. You are {age} years old'.format(new_name='Sally', age=100))

# 12 month contracts - convert full time
# security operation center
# writing modular software/migrating existing software
# python/javascript

# string[start:stop:stepover]

print(name[0])
print(name[:])
print(name[-1: -6])
print(name[3:4])
print(name[-5:])
print(name[2::-1])

# immutability - they can't be changed
# selfish = '01234567
# selfish[0] - 'str' object doesnt support item assignment
# can only change and reassign the value
# have to create new shelf space

# Python has methods (like all languages) that only a string can perform
quote = 'to be or not to be'
quote.capitalize()
# can either create or destroy strings - methods create new strings
# you can determine whether to assign or not

# BOOLEANS
# True or False

name = 'Erling'
is_cool = True
print(bool(1))

# Simple Guess Your Age

# birth_year = input('What year were you born?')
#
# age = 2020 - int(birth_year)
# print(f"Your age is: {age}")
#

# username = input('What is your username')
# password = input('What is your password')
# pass_length = len(password)
# hidden_password = '*' * pass_length

# print(f'{username}, your password, {hidden_password} is {pass_length} long')

# List - Data Structure
li = [1, 2, 3, 4, 5]
amazon_cart = ['notebooks', 'gadgets', 'sunglasses']
new_cart = amazon_cart[:]
# colon makes a copy/not modify


matrix = [[1, 0, 1], [0, 1, 0], [1, 0, 1], [100, 1, 100]]

print(matrix)
print(len(matrix[0]))
# List actions - insert, append, pop -- an index, remove -- a specific value, clear -- empty's out list
# insert and append, remove modify list in place

# index('d', 0, 2) - gets index of object it finds, can select what section to look at
# Python Keyword to search array - in -- returns true or false

# count - count how many times an item occurs e.g. basket.count('d')
# sorts a list (sorts in place) /// different that sorted(value) which doesnt modify in place - produces new array
# .copy / .reverse -- reverses the basket in place (switches index)

# range(start, stop, increment)
print(list(range(0, 100, 2)))

# .join - joins iterable item
sentence = ' '
new_sentence = sentence.join(['hi', 'my', 'name', 'is', 'JoJo'])
# or ' '.join()
print(new_sentence)

# list unpacking
d, e, f, *other, g = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(d)
print(e)
print(f)
print(other)
print(g)

# Dictionary - Hash Table //type of data structure (key,value) unordered key value pair(not next to each other in memory
# List sorted
dictionary = {
    'a': 1,
    'b': 2
}

# to access the dict - dictionary[key] -- returns a value
# keys can be containers or lists, sets, etc.
# dictionary keys can be strings, and integers, and Bool, scalar objects - dict key needs to be immutable

# Dictionary Methods
# Dictionary.Get - returns Value or None  get(value, default value if doesn't exist)
# Dictionary can use  for example print(keys in dictionary.keys | values in dictionary.values
# Or Dictionary.items --> (Returns a tuple)
# Dict.clear  - clears dictionary
# Dict.copy = copy dictionary
# user.pop('key') - removes from dict
# user.popitem -  randomly pops off an item
# user.update(key: with a value)


# Tuple - lists that are immutable, immutable lists
# can't sort or reverse
# Why do we need to use a tuple - few benefits if you don't need to change the list, it provides indication
# that it doesn't need to be changed. less flexible than a list. slightly faster than list
my_tuple = (1, 2, 3, 4, 5, 5, 5)
new_tuple = my_tuple[1:2]
print(new_tuple)
# tuples with single items show a comma (2,)

x, y, z, *other = (1, 2, 3, 4, 5)
print(x)
print(y)
print(other)

# Tuple Methods are Count (instances of a specific element) and Index - index finds value of index
print(my_tuple.count(5))

# sets are unordered connections of unique objects
my_set = {1, 2, 3, 4, 5}
your_set = {4, 5, 6, 7, 8, 9, 10}
print(1 in my_set)
print(len(my_set))

# set objects don't support indexing

# IMPORTANT SET METHOD
# Difference - tells you the difference
# print(my_set.difference(your_set))
# print(my_set)
# # Discard
# print(my_set.discard(4))
# print(my_set)
# # Difference_update - difference are removed
# my_set.difference_update(your_set)
# print(my_set)
# Intersection - shows which are in both
# print(my_set.intersection(your_set))
# print(my_set & your_set)
# isdisjoint - are those two circles overlapping - true if sets have nothing in common
print(my_set.isdisjoint(your_set))
# issubset - is my set inside the other set
my_set.issubset(your_set)
# issuperset - is your set inside my set - encompasses everything that is had
my_set.issuperset(your_set)
# Union
print(my_set.union(your_set))  # joins sets and removes duplicates - returns a new set
print(my_set | your_set)  # same as union
