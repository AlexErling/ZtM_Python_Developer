#BREAKING THE FLOW

#Conditionals allows us to skip lines
is_old = True
is_licensed = True

if is_old and is_licensed:
    print('you are old enough to drive and you have a license')
elif is_licensed:
    print('you can drive now!')
else: #else is a catch all
    print('you are not of age!')


#Truthy and Falsy - values are evaluated to truth and false
#bool("Hello") is a Truthy value
#bool("") is a Falsy value
#bool(0) is a Falsy value
#bool(5) is a Truthy value


#Ternany Operator
#Feature as of 2.4

# condition_if_true if condition else condition if false
is_friend = True

can_message = "message allowed" if is_friend == True else "not allowed to message"
print(can_message)


#Short Circuiting
is_Friend = True
is_User = False
print(is_Friend or is_User)

#Logical operators - and/or > < == <= >= !=
print(4 > 5)
print(4 < 5)
print(4 == 5)
print('a' > 'b')
print(1 < 2 < 4 > 3)

#and or not
print(not(True))
print(not True)

a = 1
b = 1.0
c = "1"
d = "1"
# == check for equality in value
#keyword is actually checks if location if memory the same
print(True is True)
print(a is b)
print(c is d)
print ([1,2,3] is [1,2,3]) #data structure is in different memory space
#is is stricter, checking for exact thing


#For Loops
# for item in iterable:
for item in [1,2,3,4,5]:
    for x in ['a', 'b', 'c']:
        print(item, x)

#iterable - object or collection that can be iterated over
#can be a list,dictionary,tuple,set,string
#iterated -> one by one check each item in the collection

user = {
    'name': 'Golem',
    'age': 5006,
    'can_swim': False
}

for item in user:
    print(item)

for item in user.items():
    print(item)

for item in user.values():
    print(item)

for key,value in user.items():
    print(key, value)

# counter
my_list = [1,2,3,4,5,6,7,8,9,10]

print(sum(my_list))
counter = 0
for item in my_list:
    counter += item
print(counter)

#range produces a sequence of integers from start to stop
#range(100) - from 0 to 99 - a special type of object
for number in range (0, 10):
    print('email: email list')

for _ in range(10, 0, -1):
    print(_)

##ENUMERATE - gives us index counter and the item at index

for char in enumerate("Hello"):
    print(char)

for i,char in enumerate(list(range(100))):
    print (i, char)
    if char == 50:
      print(f'index of 50 is: {i}')

j = 0
while j < 50:
    print(j)
    j += 1
    break #breaks a while loop
else:  #else will not print if a break
    print('Finished')

#while vs for?? for loops are simpler, but while loops can be more powerful
#while loop is better when you don't know the exact amount of loops

# while True:
#     response = input('say something: ')
#     if(response == 'bye'):
#         break

#can break out of for loop as well
#continue is a keyword to keep continuing through loop
#continue goes back to loop
#break - breaks out of current enclosing loop
#pass - skips over pass to next line - great way to have a placeholder

for item in [1,2,3]:
    pass #great placeholder


##CREATE A SIMPLE GUI
picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

#have to give end option to print so its not a new line
#iterate over picture
    # if 0 -> print ''
    # if 1 -> print *
fill  = '$'
empty = ' '
for row in picture:
    for pixel in row:
        print(fill, end='') if pixel else print(empty, end='')
        #if pixel: #truthy value
         #   print('*', end='')
        #else:
        #   print(' ', end='')
    print('')

#think about best practices to make code more concise

#Checking duplicates in a list
some_list = ['a', 'b', 'c', 'd', 'd', 'm', 'n', 'n']

duplicates = []
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)

print(duplicates)

#def - about to define a function
#use any name except for keywords

#can set a default parameter if nothing is put in
#default parameters can help to keep it safe
def say_hello(name='Darth Vader'):
    print(f'Hello {name}')

#Have to call function to use
say_hello("Alex")

##ARGUMENTS VS PARAMETERS

# def function(parameters)
#you pass the arguments to the function
#arguments == actual values you provide to a function
#arguments are required to be in proper position

#keyword arguments - explicit set the arguments
say_hello(name = "John")
#should just use proper position

def new_sum(num1, num2):
    return num1 + num2

print(new_sum(4,5))
total = new_sum(5, 5)
#Should do one thing really well.
#Should return something.

#can have a function inside a function but you need to call it
#can have nested functions, have to be careful that your function returns something
#or it will return none
def another_sum(num1, num2):
    def another_func(n1, n2):
        return n1 + n2
    return another_func(num1, num2)

other_total = another_sum(4, 9)
print(other_total)

#Methods vs Functions
#Method has to be owned by something (what is left of the dot)
#Both method and functions allows us to take actions and do something

#allows us to comment inside the functions to see what it does
def test(a):
    """
    :param a: Dumb Variable
    :return:  Doesn't do anything
    """
    print(a)
    return None

#Think of ways to clean up code (just use boolean evaluator)
def is_even(num):
    return num % 2 == 0

# *args **kwargs -- arguments and key work arguments

#unlikely to use all
def super_func(name, *args, i='hi', **kwargs): #allows you to do multiple arguments
    #args get passed as a tuple
    total = 0
    print(kwargs)
    for items in kwargs.values():
        total += items
    return sum(args) + total

print(super_func('Andy', 1, 2, 3, 4, 5, num1=5, num2=10))
#keyword args - you can add keywords to args which get put in as a dictionary

#Rule: params, *args, default parameters, **kwargs


def highest_even(li):
    evens = []
    for item in li:
        if item % 2 == 0:
            evens.append(item)
    return max(evens)

print(highest_even([10,2,3,4,8,11,20]))

#Understand scope - what variables do I have access to?
#difference between global and function scope
#Scope who has access to who

#1 - Local
#2 - Parent
#3 - Global
#4 - Built in Python Functions

total = 0
#print(globals())
#Can access a global in a function using a global keyword
#Have to declare you are using in the function
##May be better to do a dependency injection, by passing it as an argument
def count():
    global total
    total += 1
    return total

print(count())

#nonlocal - allows you to modify an outer scope that isn't necessarily global
#best practice would be to avoid global and nonlocal
def outer():
    x="local"
    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)

    inner()
    print("outer:", x)

outer()

