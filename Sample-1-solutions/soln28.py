## Name: Vivek Babu G R
## Date: 26-07-2018
## Assignment: Sample 1
## Question: Write a program to generate 10 random numbers between 1 to 100 such that there should one number between 1 to 10 one number between 11 to 20 etc.
################################################################################################################################################################
import random

rl = []
for i in range(0,10):
	rl.append(random.randint((10*i)+1,10*(i+1)))
print(rl)