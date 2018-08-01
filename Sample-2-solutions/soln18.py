## Name: Vivek Babu G R
## Date: 26-07-2018
## Assignment: Sample 2
## Question: Write a function is_empty(my_dict) that takes a dictionary my_dict and returns True if my_dict is empty and False otherwise.
###########################################################################################################################################
def is_empty(my_dict):
	if len(my_dict.keys()) == 0:
		return True
	else:
		return False

sam_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print(sam_dict)
empty_dict = {}
print(empty_dict)
n = int(input('choice between 1 & 2 dictionaries to check if it\'s empty\n'))
if n == 1:
	print(is_empty(sam_dict))
elif n == 2:
	print(is_empty(empty_dict))