# EVERYTHING IS AN OBJECT
# OOP is a way to think about the code and maintain it
# Creates instances of classes


class BigObject:
    # code
    pass


# instantiation of an object
obj1 = BigObject()
obj2 = BigObject()
obj3 = BigObject()


class PlayerCharacter:  # should be singular name
    # Objects are Camel Case
    # Class Object Attribute // Not dynamic/can't modify
    membership = True

    def __init__(self, name='anonymous', age=0):  # constructor/initialization method
        self._name = name
        self._age = age

    def shout(self):
        print(f'my name is {self._name}')

    # pass the class as cls
    @classmethod
    def adding_things(cls, num1, num2):
        return cls('Teddy', num1 + num2)

    @staticmethod  # doesn't have access to the class
    def adding_things2(num1, num2):
        return num1 + num2

    def what_is_self(self):
        return self

    def speak(self):
        print(f'my name is {self._name}, and I am {self.age} years old')
    #


# we can use static method if we don't care about the state
# we use class method if we do care and want to modify

# encapsulation is the bundling fo data with the methods that operate on the data
# Hides values or state of a structured data object inside a class, preventing
# unauthorized parties' direct access to them


player1 = PlayerCharacter("Tom", 20)
player2 = PlayerCharacter("John", 117)

print(player1._name)
print(player1.membership)
print(player2._name)
player1.shout()

# @ is a decorator
# You can use a class method without instantiating the class
# A method on the actual class
# Some cases where class method, can use cls to instantiate an object
player3 = PlayerCharacter.adding_things(20, 6)
print(player3.what_is_self())

# Through the process of abstraction, a programmer hides all
# but the relevant data about an object in order to reduce complexity and increase efficiency.

# Shouldn't be able to directly access data/
player1._name = "!!!!"
player1.speak = "Boooo"
print(player1._name)  # this is bad
print(player1.speak)  # this is bad


# No true private variables in python
# Can add underscore (means you shouldn't touch it) to show its private

# Dunder Method - built into python (wouldn't write our own)
# Encapsulation/Abstraction/Inheritance
# Inheritance to have common shared functionality
# Polymorphism

# Diff types of users
# Wizards
# Archers
# Can use inheritance, pass the parent class


class User:
    def sign_in(self):
        print("Logged in")

    def attack(self):
        print("Do nothing")


# Will get overridden by the
# Polymorphism - ability to redefine methods for different objects


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power
        # One way User.__init__(self, email)
        # Super is a keyword that refers to the superclass (class above)

    #        super().__init__(email)

    def attack(self):
        User.attack(self)
        print(f'attack with power of {self.power}')


class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrow = num_arrows

    # super().__init__(email)

    def attack(self):
        print(f'attack with arrows: arrows left - {self.num_arrow}')

    def run(self):
        print("Run really fast")


class HybridBorg(Archer, Wizard):
    def __init__(self, name, power, arrows):
        Archer.__init__(self, name, arrows)
        Wizard.__init__(self, name, power)


# things gets complicated with multiple inheritance

hb1 = HybridBorg("Borg", 50, 100)
# tricky with multiple inheritance

wizard1 = Wizard('Gandalf', 50)
archer1 = Archer("Robin", 500)
print(wizard1.sign_in())
wizard1.attack()
archer1.attack()

# can check instances
print(isinstance(wizard1, object))
print(isinstance(wizard1, Wizard))
# Wizard inherits from object base class

# Introspection
# dir gives all methods and attributes on an instance/object
print(dir(wizard1))


# Dunder Methods -- inherited from base object class
# Allows us to use python specific functions on classes


class Toy:
    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.my_dict = \
            {
                'name': 'Yoyo',
                'has_pets': False
            }

    # str is only modified on specific object we are using
    def __str__(self):
        return f'{self.color}'

    def __len__(self):
        return 5

    def __call__(self):
        print("yes??")

    def __getitem__(self, item):
        return self.my_dict[item]


action_figure = Toy('red', 0)
print(action_figure.__str__())
print(str(action_figure))
print(len(action_figure))
print((action_figure()))  # change calling the function
print(action_figure['name'])  # changing getting an item


class SuperList(list):  # list becomes parent class
    def __len__(self):
        return 1000


super_list1 = SuperList();
print(len(super_list1))
super_list1.append(5)
print(super_list1[0])
print(issubclass(SuperList, list))


# Everything inherits from base object class

# METHOD RESOLUTION ORDER - know which method to run
class A:
    num = 10


class B(A):
    pass


class C(A):
    num = 1


class D(B, C):
    pass


# If things are common between attribute, how do you know
print(D.num)
print(D.mro())  # shows ordering


class X:
    pass


class Y:
    pass


class Z:
    pass


class A(X, Y):
    pass


class B(Y, Z):
    pass


class M(B, A, Z): # order from passing in parameters
    pass

# it is left to right, depth-first
# [<class '__main__.M'>, <class '__main__.B'>, <class '__main__.A'>,
# <class '__main__.X'>, <class '__main__.Y'>, <class '__main__.Z'>, <class 'object'>]
# Shouldn't run into complicated code like this then


print(M.mro())

