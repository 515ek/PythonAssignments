## Name: Vivek Babu G R
## Date: 26-07-2018
## Assignment: Sample 1
## Question: Python Program to Find the Smallest Divisor of an Integer.
#########################################################################
num = int(input('enter the Integer\n'))
for i in range(2,num+1):
	if num % i == 0:
		print(i)
		break