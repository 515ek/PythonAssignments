## Name: Vivek Babu G R
## Date: 26-07-2018
## Assignment: Sample 1
## Question: Python Program to Count the Number of Vowels in a String.
########################################################################
str1 = input('Enter the string\n')
Vowels = ['a','A','e','E','i','I','o','O','u','U']
count = 0
for ch in str1:
	if ch in Vowels:
		count += 1
print(count)

