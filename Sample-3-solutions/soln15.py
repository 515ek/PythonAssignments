## Name: Vivek Babu G R
## Date: 26-07-2018
## Assignment: Sample 3
## Question: Write a function group(list, size) that take a list and splits into smaller lists of given size.
###############################################################################################################
#!/usr/bin/python
ls = input('enter the elements of the list\n').split(' ')
size = int(input('enter the size to split the list\n'))
def group(ls, size):
	lgrp = []
	while len(ls) > size:
		lgrp.append(ls[:size])
		ls = ls[size:]
	else:
		lgrp.append(ls)
	return lgrp

lgroup = group(ls,size)

for l in lgroup:
	print(l)