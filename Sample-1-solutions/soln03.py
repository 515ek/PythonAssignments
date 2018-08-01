## Name: Vivek Babu G R
## Date: 26-07-2018
## Assignment: Sample 1
## Question: Python Program to Print all Numbers in a Range Divisible by a Given Number.
############ [ if range is from 1 to 20 and number is 4, then the result should be 4, 8, 12, 16 and 20. ]
###########################################################################################################
m,n = map(int,input('Enter the range\n').strip().split(' '))
num = int(input('Enter the Number\n'))
for x in range(m,n+1):
	if x % num == 0:
		print(x,end='  ')
print('\n')