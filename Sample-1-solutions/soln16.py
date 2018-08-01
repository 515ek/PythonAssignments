## Name: Vivek Babu G R
## Date: 26-07-2018
## Assignment: Sample 1
## Question: Python Program to Replace all Occurrences of ‘a’ with $ in a String.
###################################################################################
str1 = input('Enter the string\n')
str2 = ''
if str1.find('a') != -1:
	for ch in str1:
		if ch == 'a':
			str2 += '$'
		else:
			str2 += ch
print(str2)