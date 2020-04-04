from collections import Counter, defaultdict, OrderedDict
import datetime
from array import array

# Counter counts the name of times of each items and puts in a dictionary
# Turns list into dictionary to keep count
# li = [1, 2, 3, 4, 5, 6, 7, 7]
# print(Counter(li))

dictionary = defaultdict(lambda: 5, {'a': 1, 'b': 2})
print(dictionary['a'])
print(dictionary['c'])
# default dictionary gives a default value if something doesn't exist

# ordered dict maintains orders
d = OrderedDict()
d['a'] = 1
d['b'] = 2

d2 = OrderedDict()
d2['b'] = 2
d2['a'] = 1

# will return false cause not input in same order
# ordered dict will put the entries in order
# although dictionaries are ordered after 3.7
print(d2 == d)

print(datetime.time(5, 45, 2))
print(datetime.date.today())

# list vs arrays
# lists are dynamic -> can increase/decrease
# arrays are static
# array type code -> can only take a certain type line in other languages
 