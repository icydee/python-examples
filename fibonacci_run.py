#!/usr/local/bin/python3

# Test script for fibonacci routines

from fibonacci import fib_recursive,fib_dynamic,fib_optimize,fib_exception

index = input('Give the index: ')

for test in [fib_dynamic, fib_optimize, fib_recursive]:
    try:
        fib = test(float(index))
        print ("FIB %s = %s" % ( index, fib ))
    except fib_exception:
        print ("Input must be a positive integer")

