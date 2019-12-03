#!/usr/local/bin/python3
#
# Create a fibionnaci iterator

import time

class IterateFibonacci:
    def __iter__(self):
        self.minus_2 = 0
        self.minus_1 = 1
        return self

    def __next__(self):
        x = self.minus_2 + self.minus_1
        self.minus_2 = self.minus_1
        self.minus_1 = x
        return self.minus_2

myclass = IterateFibonacci()
myiter = iter(myclass)

#for a in range(20):
#    print(next(myiter))

for a in myclass:
    print(a)
    time.sleep(1)
