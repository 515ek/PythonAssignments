## Name: Vivek Babu G R
## Date: 26-07-2018
## Assignment: Sample 2
## Question: Python Program to Put Even and Odd elements in a List into Two Different Lists.
##############################################################################################
nl = list(input('Enter the elements of list \n').split(' '))
el = []
ol = []
for i in range(len(nl)):
	if i % 2 == 0:
		el.append(nl[i])
	else:
		ol.append(nl[i])
print(el)
print(ol)