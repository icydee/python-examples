#!/usr/local/bin/python3

# Test script for fibonacci routines

from fibonacci import fib_recursive,fib_dynamic,fib_optimize,fib_exception
from fibonacci_class import Fibonacci

index = input('Give the index: ')

for test in [fib_dynamic, fib_optimize, fib_recursive]:
    try:
        fib = test(float(index))
        print ("FIB %s %s = %s" % ( test, index, fib ))
    except (fib_exception, ValueError):
        print ("Input must be a positive integer")


c_fib = Fibonacci()
fib = c_fib.calc(float(index))
print ("Class FIB %s" % ( fib ))

d_fib = Fibonacci()
fib = d_fib.calc(float(index))
print ("CLASS FIB %s" % fib)