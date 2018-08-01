## Name: Vivek Babu G R
## Date: 26-07-2018
## Assignment: Sample 1
## Question: Python Program to check whether a full pattern (not sub string) is present in the given sentence.
################################################################################################################
str1 = input("Enter the string\n")
pattern = input("Enter the pattern to find in string\n")
for ch in str1.split(' '):
	if ch == pattern:
		print('Pattern present in the string')
		break
else:
	print('Pattern not present in the string')
