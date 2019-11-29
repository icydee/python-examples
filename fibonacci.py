#!/usr/local/bin/python3

# Python 2.6 script to calculate fibonacci number

class fib_exception(Exception):
    pass

def fib_recursive(n):
    if n <= 0 or n != int(n) :
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
def fib_dynamic(n):
    if n <= 0 or n != int(n):
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

def fib_optimize(n):
    a = 0
    b = 1
    if (n <= 0):
        raise fib_exception()
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2,n+1):
            c = a + b
            a = b
            b = c
        return c

# Note than 'range' in python2 returns a list (calculated in one go)
# xrange creates an iterator (each number generated when needed)
# python3 'range' is python2 'xrange' ie an iterator

#index = int(input('Give the index: '))
#print ("Recursive :"+str(fib_recursive(index)))
#print ("Dynamic   :"+str(fib_dynamic(index)))
#print ("Optimize  :"+str(fib_optimize(index)))
