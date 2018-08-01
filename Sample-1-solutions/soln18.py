## Name: Vivek Babu G R
## Date: 26-07-2018
## Assignment: Sample 1
## Question: Python Program to Take in a String and Replace Every Blank Space with Hyphen.
############################################################################################
str1 = input('Enter the string\n')
str2 = ''
for s in str1.split(' '):
	if str2 != '':
		str2 = str2 + '-' + s
	else:
		str2 += s
print(str2)