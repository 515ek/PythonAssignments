## Name: Vivek Babu G R
## Date: 26-07-2018
## Assignment: Sample 2
## Question: Python Program to Remove the Given Key from a Dictionary.
########################################################################
sam_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print(sam_dict)
key = input('Enter key to Remove in above Dictionary\n')

if key in sam_dict.keys():
	sam_dict.pop(key)
	print(sam_dict)
else:
	print('Invalid Key')