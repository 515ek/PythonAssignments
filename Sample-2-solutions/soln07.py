## Name: Vivek Babu G R
## Date: 26-07-2018
## Assignment: Sample 2
## Question: Python Program to find union and intersection of lists without repetition.
#########################################################################################
l1 = list(input('Enter the elements of list 1\n').split(' '))
l2 = list(input('Enter the elements of list 2\n').split(' '))
il = list(set(l1).intersection(set(l2)))
print(il)