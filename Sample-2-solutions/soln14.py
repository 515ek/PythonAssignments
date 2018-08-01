## Name: Vivek Babu G R
## Date: 26-07-2018
## Assignment: Sample 2
## Question: Python Program to Generate a Dictionary that Contains Numbers (between 1 and n) in the Form (x,x*x).
###################################################################################################################
n = int(input('Enter the value of n\n'))
gdict = {i : i*i for i in range(1, n)}
print(gdict.items())