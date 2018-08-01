## Name: Vivek Babu G R
## Date: 26-07-2018
## Assignment: Sample 1
## Question: Python Program to Find the Sum of Digits in a Number.
####################################################################
num = int(input('Enter the number\n'))
nsum = 0
for i in str(num):
	nsum+= int(i)
print('Sum =',nsum)