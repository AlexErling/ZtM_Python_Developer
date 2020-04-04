range(100)
list(range(100))


def make_list(num):
    result = []
    for i in range(num):
        result.append(i * 2)
    return result


my_list = make_list(100)
print(list(range(1000000)))


# my list lives in memory
# range is a generator and doesn't take space

# remember key terms - a list is an iterable
# iterable any object that you can loop through
# has the Dunder __iter__ method__
# Generators are iterable - not all iterables are generators


def generator_function(num):
    for i in range(num):
        yield i * 2
        # only held one item in memory
        # uses keyword yield to become a generator
        # yield pauses the function, when we do something to it (next)
        # only keeps most recent value in generator


for item in generator_function(1000):
    print(item)

g = generator_function(100)
print(next(g))


# next can be called until range expires


def special_for(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(iterator)
            next(iterator)
        except StopIteration:
            break


special_for([1, 2, 3])


# Create our own generator
class MyGen:
    current = 0

    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __iter__(self):
        return self

    def __next__(self):
        if MyGen.current < self.last:
            num = MyGen.current
            MyGen.current += 1
            return num
        raise StopIteration


# gen = MyGen(0, 100)
# for i in gen:
#     print(i)


def fib_gen(num):
    a = 0
    b = 1

    for i in range(0, num):
        yield a
        b, a = a + b, b  # way to avoid temp


#        temp = a
#        a = b
#        b = temp + b

for x in fib_gen(100):
    print(x)
