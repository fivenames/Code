'''
This is a docstring, a way to document the code, usually used for official documentation and can be extracted out with tools to make official documentation.
'''

''' GLOBAL VARIABLE '''

balance = 0

def main():

    names = ['alice', 'bob', 'bob']
    name = set()

    for i in range(3):
        name.add(names[i])
# A set cannot have duplicated data

def deposit(n):
    global balance
    balance += n
# define the variable as global in order to change its data locally inside a funtion, in C, however, this is not necessary.
# define the variable in main will not work as well as it is created locally inside main. Deeper explaination refer to C notes.

''' ARGUMENT PARSER '''

import argparse

# create parser object, the optional parameter will be shown when run 'python programme.py -h'.
parser = argparse.ArgumentParser(description='A description of how this programme works.')
# add command-line argument option, the optional param 'default' will make the int after -n to be 1 if -n is not passed
parser.add_argument('-n', default=1, help='What -n means.', type=int)

# No need to import sys as the module does it for you.

# Create args object containing all the arg options.
args = parser.parse_args()
# args.n will return the integer after the '-n' arg.

''' UNPACKING '''

def addition(a, b, c):
    return a + b + c

num = [1, 2, 3]
# The * will unpack the list into individual values.
total = addition(*num)

num = {'a' : 1, 'b' : 2, 'c' : 3}
# This will pass in the key and values as key=value: add(a=1, b=2, c=3).
total = addition(**num)

# Unpacking only works for list and dict, and only if they contain the exact number of param that the function expects

# *param_name, means the function can take in a variable number of positional args, while **param_name means the function can take in a variable number of named args.
def f(*args, **kwargs):
    # Postional args means values separated with commas like a list.
    print('', args)
    # Named args is values with names defined, like a dict.
    print('', kwargs)

''' LIST & DICT COMPREHENSION '''

# map() function usage in dna.py

def main():
    yell('This', 'is', 'cs50', ' ', '&&&')

def yell(*words):
    # This list comprehension is equivalent to a loop, calling .upper to each element and append into a new list(if the element is all alphanumeric).
    uppercased = [word.upper() for word in words if word.isalnum()]
    print(*uppercased)

# Similar to map(), filter() also calls the given function to every element in an iterable. However, it expects the given function to be return a bool.
# filter() will calls the function on every element and remove those elements in the list that has a False return value from the given funtion.
def is_valid():
    if ...:
        return True
    else:
        return False

words = ['sdahdhu', 'abc250', 'What', 'Hello', 'cs50']
words = filter(is_valid, words)


names = ['alice', 'bella', 'charlie']

# List of dicts
details = [{'name' : name, 'gender' : 'female'} for name in names]
# One dict
detail = {name : 'female' for name in names}

''' ENUMERATE '''

# enumerate() takes in an iterables and return the index of each element
for i, name in enumerate(names):
    ...

''' GENERATORS '''

# If data is too large to be return at once, generator can be used to return the data in smaller sections.

# for example:
# def sheep(n=100000000):
#     flock = []
#     for i in range(n):
#         flock.append('$' * i)
#     return flock

# In order to continue the loop (as returning will quit the function instantly), yield can be used so that values are returned while the function is kept running.
def sheep(n):
    for i in range(n):
        yield '$' * i

# yield actually returns an iterator which steps over one element at a time if looped, similar to the 'reader' iterator obejct created when csv.reader()||csv.DictReader() is called.
for s in sheep(n):
    print(s)

''' END OF CS50P '''