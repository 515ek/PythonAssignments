#!/usr/bin/python
## Name: Vivek Babu G R
## Date: 26-07-2018
## Assignment: Sample 3
###################################################################################################################
import handle as h
#### 1: cat.py
def cat():
    fname = h.get_file()
    fd = h.open_file(fname,'r')
    res = fd.read()
    h.close_file(fd)
    return res

#### 2: cp.py simulate cp cmd
def cp():