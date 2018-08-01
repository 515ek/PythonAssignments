## Name: Vivek Babu G R
## Date: 26-07-2018
## Assignment: Sample 1
## Question: Python Program to Calculate the Number of Upper Case Letters and Lower Case Letters in a String.
###############################################################################################################
str1 = input('Enter the string\n')
ucount = 0
lcount = 0
for c in str1:
	if c.isupper():
		ucount += 1
	else:
		lcount += 1

print('number of Uppercase Letters :',ucount)
print('number of Lowercase Letters :',lcount)