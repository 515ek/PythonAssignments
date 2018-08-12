#!/usr/bin/python
## Name: Vivek Babu G R
## Date: 11-08-2018
## Assignment: Sample 2
#############################################################################################
##########
import random
## Question 1: Python Program to Find the Largest Number in a List.
def soln01(ls):
    return max(ls)

## Question 2: Python Program to Find the Second Largest Number in a List.
def soln02(ls):
    return max([x for x in ls if x < max(ls)])

## Question 3: Python Program to Put Even and Odd elements in a List into Two Different Lists.
def soln03(ls):
    return ([ls[x] for x in range(len(ls)) if x % 2 == 0 ],[ls[x] for x in range(len(ls)) if x % 2 != 0 ])

## Question 4: Python Program to check whether two lists are same.
def soln04(l1,l2):
    return l1 == l2

## Question 5: Python Program to Find the Union of Lists.
def soln05(l1,l2):
    return l1 + l2

## Question 6: Python Program to Find the Intersection of Lists.
def soln06(l1,l2):
    return [x for x in l1 if x in l2]

## Question 7: Python Program to find union and intersection of lists without repetition.
def soln07(l1,l2):
    return (list(set(l1).union(set(l2))), list(set(l1).intersection(set(l2))))

## Question 8: Python Program to Create a List of Tuples with the First Element as the Number and Second Element as the Square of the Number.
def soln08(ls):
    return [(x,x*x) for x in ls]

## Question 9: Python Program to Remove the Duplicate Items from a List.
def soln09(ls):
    return list(set(ls))

## Question 10: Python Program to Read a List of Words and Return the Length of the Longest One.
def soln10(ls):
    return max([len(x) for x in ls])

## Question 11: Python Program to Add a Key-Value Pair to the Dictionary.
def soln11(key,val,d):
    d[key] = val
    return d

## Question 12: Python Program to Concatenate Two Dictionaries Into One.
def soln12(d1,d2):
    d1.update(d2)
    return d1

## Question 13: Python Program to Check if a Given Key Exists in a Dictionary or Not.
def soln13(key,d):
    return d.get(key,False)

## Question 14: Python Program to Generate a Dictionary that Contains Numbers (between 1 and n) in the Form (x,x*x).
def soln14(n):
    return {x:x*x for x in range(1,n+1)}

## Question 15: Python Program to Sum All the Items in a Dictionary.
def soln15(d):
    return sum(d.values())

## Question 16: Python Program to Multiply All the Items in a Dictionary.
def soln16(d):
    vals = list(d.values())
    return [vals[x] * vals[x +1] for x in range(len(vals) - 1) ][-1]

## Question 17: Python Program to Remove the Given Key from a Dictionary.
def soln17(d,key):
    return d.pop(key,False)

## Question 18: Write a function is_empty(my_dict) that takes a dictionary my_dict and returns True if my_dict is empty and False otherwise.
def soln18(my_dict):
    return my_dict == {}

## Question 19: Write a function make_dict(key_value_list) that takes a list of tuples key_value_list where each tuple is of the form (key, value) and returns a dictionary with these keys and corresponding values.
def soln19(kv_list):
    return dict(kv_list)

## Question 20: A simple substitution cipher is an encryption scheme where each letter in an alphabet to replaced by a different letter in the same alphabet with the restriction that each letter's replacement is unique. The template for this question contains an example of a substitution cipher represented a dictionary CIPHER_DICTIONARY. Your task is to write a function encrypt(phrase,cipher_dict) that takes a string phrase and a dictionary cipher_dict and returns the results of replacing each character in phrase by its corresponding value in cipher_dict.Ex: encrypt("cat", CIPHER_DICT) should return ”km “
def encrypt(phrase,cip_dict):
    msg = ''
    for ch in phrase:
        msg += cip_dict[ch]
    return msg

def soln20(phrase):
    cip_dict = {'e': 'u', 'b': 's', 'k': 'x', 'u': 'q', 'y': 'c', 'm': 'w', 'o': 'y', 'g': 'f', 'a': 'm', 'x': 'j', 'l': 'n', 's': 'o', 'r': 'g', 'i': 'i', 'j': 'z', 'c': 'k', 'f': 'p', ' ': 'b', 'q': 'r', 'z': 'e', 'p': 'v', 'v': 'l', 'h': 'h', 'd': 'd', 'n': 'a', 't': ' ', 'w': 't'}
    return encrypt(phrase,cip_dict)

## Question 21: Write a function make_cipher_dict(alphabet) that takes a string of unique characters and returns a randomly-generated cipher dictionary for the characters in alphabet. You should use the shuffle() method in the random module to ensure that your returned cipher dictionary is random.
def make_cipher_dict(alphabet):
    al_key = []
    c_dict = {}
    for c in alphabet:
        al_key.append(c)
    al_val = list(al_key)
    random.shuffle(al_val)
    for i in range(len(al_key)):
        c_dict[al_key[i]] =al_val[i]
    return c_dict

def soln21(alphabet):
    return make_cipher_dict(alphabet)

## Question 22: Write a python code to generate grade using dictionary. Dictionary should have student names as keys (assuming names are unique) and subject_name and mark as value. There are 5 subjects for each student. Marks should be converted to grades (90 – 100 A+, 80-89 A etc).
def soln22(stu_dict):
    grades = {'A+':(90 , 100), 'A':(80 , 89), 'B':(70 , 79), 'C':(60 , 69), 'E':(50 , 59), 'F':(0 , 49)}
    for k,v in stu_dict.items():
        for key,val in v.items():
            for g,r in grades.items():
                if r[0] <= val <= r[1]:
                    stu_dict[k][key] = (val,g)
    return stu_dict