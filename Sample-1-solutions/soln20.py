## Name: Vivek Babu G R
## Date: 26-07-2018
## Assignment: Sample 1
## Question: Python Program to Take in Two Strings and Display the Larger String without Using Built-in Functions.
####################################################################################################################
str1 = input('Enter the string\n')
str2 = input('Enter the string\n')
l1 = 0
l2 = 0
for c in str1:
	l1 += 1
for c in str2:
	l2 += 1
if l1 < l2:
	print(str2)
else:
	print(str1)