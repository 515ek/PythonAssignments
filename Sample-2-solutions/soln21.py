## Name: Vivek Babu G R
## Date: 26-07-2018
## Assignment: Sample 2
## Question: Write a function make_cipher_dict(alphabet) that takes a string of unique characters and returns a randomly-generated cipher dictionary 
##			 for the characters in alphabet. You should use the shuffle() method in the random module to ensure that your returned cipher dictionary is random.
#################################################################################################################################################################
import random
def make_cipher_dict(alphabet):
	al_key = []
	al_val = []
	c_dict = {}
	for ch in alphabet:
		al_key.append(ch)
		al_val.append(ch)
	random.shuffle(al_val)
	for i in range(len(al_key)):
		c_dict[al_key[i]] = al_val[i]
	return c_dict

alphabet = input("Enter the alphabet to create cipher dictionary\n")
print(make_cipher_dict(alphabet))