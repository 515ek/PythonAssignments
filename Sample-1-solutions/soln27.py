## Name: Vivek Babu G R
## Date: 26-07-2018
## Assignment: Sample 1
## Question: Write a program to generate 5 random integers between 1 to 20 such that numbers should be unique.
################################################################################################################
import random

rl = random.sample(range(1,20), 5)

'''#########Basic Method using randint()#########
rl = []
i = 0 
while i < 5:
	rn = random.randint(1,20)
	if rn not in rl:
		rl.append(rn)
		i += 1 
##############################################'''
print(rl)