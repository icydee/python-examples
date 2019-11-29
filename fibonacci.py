#!/usr/local/bin/python3

# Python 2.6 script to calculate fibonacci number
# Raises exception if invalid input is given

class fib_exception(Exception):
    pass

def fib_recursive(input):
    n = int(input)
    if n <= 0 or n != input :
        raise fib_exception()
    elif n==1 :
        # first in series
        return 1
    elif n==2 :
        # second in series
        return 1
    else :
        # return sum of two previous
        return fib_recursive(n-2)+fib_recursive(n-1)

fib_array = [0,1]
def fib_dynamic(input):
    n = int(input)
    if n <= 0 or n != input:
        raise fib_exception()
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    elif n<=len(fib_array):
        return fib_array[n-1]
    else:
        temp_fib = fib_dynamic(n-2)+fib_dynamic(n-1)
        fib_array.append(temp_fib)
        return temp_fib

# optimise for size
def fib_optimize(input):
    n = int(input)
    a = 0
    b = 1
    if n <= 0 or n != input:
        raise fib_exception()
    if n == 1:
        return b
    else:
        for i in range(2,n+1):
            c = a + b
            a = b
            b = c
        return c

