#!/usr/bin/python
## Name: Vivek Babu G R
## Date: 26-07-2018
## Assignment: Sample 3
## Question: Write a program ls.py that takes path to a directory as command-line argument and prints all the files in that directory.
##			 When no argument is specified, it should list the files in the current directory.
########################################################################################################################################

import cat
import os

pname = cat.get_path()

print(os.listdir(pname))