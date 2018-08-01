## Name: Vivek Babu G R
## Date: 26-07-2018
## Assignment: Sample 1
## Question: Python Program to Print Odd Numbers Within a Given Range.
########################################################################
m,n = map(int,input('Enter the range\n').split(' '))
for x in range(m,n+1):
	if x % 2 == 1:
		print(x,end=' ')
print('\n')