# @ is a decorator pattern
# *args, **kwargs gives us flexibility in the args

# decorators only available because they can act like variables

from time import time


def hello(func):
    func()
    print('helloooooooo')


def greet():
    print('still here!')


# del hello is deleting the reference
# greet is still pointing to the same memory location


# HOC - HIGHER ORDER FUNCTION
# a function that accepts another function

# def greet(func):
#     func()

# def greet2():
#   def func();
#       return 5
#   return func


def my_decorator(func):
    def wrap_func(*args, **kwargs):
        print('*************')
        func(*args, **kwargs)
        print("*************")

    return wrap_func


@my_decorator
def hellooo(greeting, emoji=":("):
    print(greeting, emoji)


@my_decorator
def bye():
    print('see ya later')


# decorator can actually be used on top to defining functions

hellooo("Hello")


# bye()

# can just add extra functionality by using a decorator
# essentialy just doing my_decorator(hellooo)
# or my_decorator(bye)
# easier just to do use @
# hectic to have to add additional monitors

def performance(func):
    def wrap_func(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        finish = time()
        print(f'Took {finish - start} s.')
        return result

    return wrap_func


@performance
def long_time():
    for i in range(1000000):
        i = i * 5

    return None


print(long_time())

# examples - #login, #auth - great use for decorators in django/flask
