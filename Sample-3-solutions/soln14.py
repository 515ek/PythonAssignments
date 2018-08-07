#!/usr/bin/python
## Name: Vivek Babu G R
## Date: 26-07-2018
## Assignment: Sample 3
## Question: Write a function dups to find all duplicates in the list.
########################################################################
ls = input('enter the elements of the list\n').split(' ')
def dups(ls):
	dups = []
	for i in range(len(ls)):
		if ls[i] in ls[i+1:] and ls[i] not in dups:
			dups.append(i)
	return dups

print(dups(ls))