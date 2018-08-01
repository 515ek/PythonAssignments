## Name: Vivek Babu G R
## Date: 26-07-2018
## Assignment: Sample 3
## Question: Write a function unique to find all the unique elements of a list.
#################################################################################
ls = input('enter the elements of the list\n')
def unique(ls):
	unls = []
	for l in ls:
		if l not in unls:
			unls.append(l)
	return unls

print(unique(ls))