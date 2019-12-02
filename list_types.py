#!/usr/local/bin/python3
#
# List Types in Python.
#
#           ordered mutable duplicates  indexed  ref
# List      YES     YES     YES         NO          [ "one", "two" ]
# Tuple	    YES     NO      YES         NO          ( "one", "two" )
# Set       NO      YES     NO          NO          { "one", "two" }
# Dictionar NO      YES     NO          YES         { "name": "value"}

# List methods
print("###### list method ########")
# len()         - Returns the length of the list
fruits = ['apple', 'banana', 'cherry']
print(len(fruits));

# append()      - Add elements to the end of a list
print("append")
fruits = ['apple', 'banana', 'cherry']
fruits.append("orange")
print(fruits);

# clear()       - Empty the list
print("clear")
fruits = ['apple', 'banana', 'cherry']
fruits.clear()
print(fruits);

# copy()        - Returns a copy
print("copy")
one = ['one','two']
two = one.copy()
one.clear()
print(two);

# count()       - Returns number of elements with the specified value
print("count")
fruits = ['apple', 'banana', 'cherry', 'banana']
print(fruits.count('banana'));

# extend()      - Add the elements of a list (or any iterator) to the end of the list
one = ['one','two']
one.extend(('three','four'))
print(one)

# index()       - Returns the index of the first element with the specified value
print("index")
fruits = ['apple', 'banana', 'cherry', 'banana']
print(fruits.index('banana'));

# insert()      - Add an element at the specified position
print("insert")
fruits = ['apple', 'banana', 'cherry']
fruits.insert(1, 'kiwi')
print(fruits);

# pop()         - Remove an element at the specified position
print("pop")
fruits = ['apple', 'banana', 'cherry']
foo = fruits.pop(1)
print(fruits);
print("result "+foo)

# remove()      - Remove the item with the specified value
print("remove")
fruits = ['apple', 'banana', 'cherry']
fruits.remove('banana')
print(fruits);

# reverse()     - Reverses the order of the list
print("reverse")
fruits = ['apple', 'banana', 'cherry']
fruits.reverse()
print(fruits);

# sort()        - Sorts the list
print("sort")
fruits = ['one', 'two', 'three']
fruits.sort()
print(fruits);

print("##### tuple methods ######")
print("count")
numbers = ('one', '2', 'three', 2)
print(numbers.count('2'))

print("index")
numbers = ('one', '2', 'three', 2)
print(numbers.index(2))

print("##### set methods #####")
print("add")
print("clear")
print("copy")
print("difference")
print("difference_update")
print("discard")
print("intersection")
print("intersection_update")
print("isdisjoint")
print("issubset")
print("issuperset")
print("pop")
print("remove")
print("symmetric_difference")
print("symmetric_difference_update")
print("union")
print("update")

print("##### dictionary methods #####")
print("clear")
print("copy")
print("fromkeys")
print("get")
print("items")
print("keys")
print("pop")
print("popitem")
print("setdefault")
print("update")
print("values")





