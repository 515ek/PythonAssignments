## Name: Vivek Babu G R
## Date: 26-07-2018
## Assignment: Sample 2
## Question: Python Program to Check if a Given Key Exists in a Dictionary or Not.
####################################################################################
sam_dict = {'a': 1, 'b': 2, 'c': 3}
print(sam_dict)
key = input('Enter key to search in above Dictionary\n')

if sam_dict.get(key,-1) != -1:
	print('Key',key,'is present in Dictionary')
else:
	print('Key',key,'is not present in Dictionary')