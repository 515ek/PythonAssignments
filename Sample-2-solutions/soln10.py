## Name: Vivek Babu G R
## Date: 26-07-2018
## Assignment: Sample 2
## Question: Python Program to Read a List of Words and Return the Length of the Longest One.
###############################################################################################
nl = list(input('Enter the Words of list \n').split(' '))
lw = ''
for word in nl:
	if len(word) > len(lw):
		lw = word
print(len(lw))
