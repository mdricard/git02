import math


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def multiply_two(a, b):
    return a * b

def Whats_e(x):
    return math.exp(x)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Homer J Simpson')
    print('Stop eating doughnuts they are bad for you')
    print('Lisa its your birthday')
    print(multiply_two(3, 40))
    print('x = 1')
    print("exp(x) ", Whats_e(1))

    for letter in 'Python':  # First Example
        print('Current Letter :', letter)

    fruits = ['banana', 'apple', 'mango']
    for fruit in fruits:  # Second Example
        print('Current fruit :', fruit)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
