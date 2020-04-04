import shopping.more_shopping.shopping_cart as shop
from utility import multiply, divide
import sys
import pyjokes

# from shopping.more_shopping import shopping_cart
print(__name__)
print(divide(1,2))
print(multiply(3,1))
print(shop.buy("apple"))
print(max([1,2,3]))  # can override existing functions

print(pyjokes.get_joke())

if __name__ == '__main__':
    print("Please run this")

print(sys.argv)