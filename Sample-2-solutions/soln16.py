## Name: Vivek Babu G R
## Date: 26-07-2018
## Assignment: Sample 2
## Question: Python Program to Multiply All the Items in a Dictionary.
########################################################################
def prod(vals):
	prod = 1
	for val in vals:
		prod *= val
	return prod

sam_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print(sam_dict)
print(prod(sam_dict.values()))