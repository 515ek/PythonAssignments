## Name: Vivek Babu G R
## Date: 26-07-2018
## Assignment: Sample 2
## Question: Write a function make_dict(key_value_list) that takes a list of tuples key_value_list 
##			 where each tuple is of the form (key, value) and returns a dictionary with these keys and corresponding values.
##############################################################################################################################
def make_dict(kvl):
	my_dict = {}
	for k,v in kvl:
		my_dict[k] = v
	return my_dict
key_value_list = [(str(i), i*2) for i in range(10)]
print(key_value_list)
print(make_dict(key_value_list))