#!/usr/local/bin/python3
#
# file handling
import os

filename = "my_demo_file.txt"

if (os.path.exists(filename)):
    os.remove(filename)

thisfile = open(filename,"w")
thisfile.write("Now the file has content")
thisfile.close

