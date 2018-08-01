## Name: Vivek Babu G R
## Date: 26-07-2018
## Assignment: Sample 1
## Question: Python Program to Calculate the Number of Digits and Letters in a String.
########################################################################################
str1 = input('Enter the string\n')
ncount = 0
acount = 0
for c in str1:
	if c.isalpha():
		acount += 1
	elif c.isdigit():
		ncount += 1

print('number of Letters in a String :',acount)
print('number of Digits in a String :',ncount)