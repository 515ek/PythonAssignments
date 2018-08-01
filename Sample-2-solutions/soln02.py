## Name: Vivek Babu G R
## Date: 26-07-2018
## Assignment: Sample 2
## Question: Python Program to Find the Second Largest Number in a List.
##########################################################################
nl = list(map(int,input('Enter the Numbers\n').split(' ')))
nl.remove(max(nl))
print(max(nl))