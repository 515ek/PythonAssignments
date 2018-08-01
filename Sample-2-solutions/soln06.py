## Name: Vivek Babu G R
## Date: 26-07-2018
## Assignment: Sample 2
## Question: Python Program to Find the Intersection of Lists.
################################################################
l1 = list(input('Enter the elements of list 1\n').split(' '))
l2 = list(input('Enter the elements of list 2\n').split(' '))
il = []
for it in l1:
	if it in l2:
		il.append(it)
print(il)