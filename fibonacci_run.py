#!/usr/local/bin/python3

# Test script for fibonacci routines

from fibonacci import fib_recursive,fib_dynamic,fib_optimize,fib_exception

index = int(input('Give the index: '))
print ("Dynamic   :"+str(fib_dynamic(index)))
print ("Optimize  :"+str(fib_optimize(index)))
print ("Recursive :"+str(fib_recursive(index)))
