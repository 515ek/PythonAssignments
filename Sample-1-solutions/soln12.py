## Name: Vivek Babu G R
## Date: 26-07-2018
## Assignment: Sample 1
## Question: Python Program to Check if a Number is a Palindrome.
###################################################################
def ispalindrome(num):
	rev_num = ''
	for n in str(num):
		rev_num = n + rev_num
	if num == int(rev_num):
		print('Given number is a Palindrome\n')
	else:
		print('Given number is not a Palindrome\n')

num = int(input('Enter a number\n'))
ispalindrome(num)