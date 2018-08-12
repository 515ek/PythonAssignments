#!/usr/bin/python
## Name: Vivek Babu G R
## Date: 11-08-2018
## Assignment: Sample 1
#######################################################################################################
import random

## Question 1: Python Program to Exchange the Values of Two Numbers Without Using a Temporary Variable.
def soln1(a,b):
    return (b,a)

## Question 2: Python Program to Check Whether a Number is Positive or Negative.
def soln2(n):
    return n > 0

## Question 3: Python Program to Print all Numbers in a Range Divisible by a Given Number.
## [ if range is from 1 to 20 and number is 4, then the result should be 4, 8, 12, 16 and 20. ]
def soln3(m,n,num):
    return [x for x in range(m,n+1) if x % num == 0]

## Question 4: Python Program to Read Two Numbers and Print Their Quotient and Remainder.
def soln4(a,b):
    return ((a // b) , (a % b))

## Question 5: Python Program to Print Odd Numbers Within a Given Range.
def soln5(m,n):
    return [x for x in range(m,n) if x % 2 == 0]

## Question 6: Python Program to Find the Sum of Digits in a Number.
def soln6(num):
    return sum([int(x) for x in str(num)])

## Question 7: Python Program to Find the Smallest Divisor of an Integer.
def soln7(num):
    for i in range(2,num+1):
        if num % i == 0:
            return i

## Question 8: Python Program to Read a number n and Compute n+nn+nnn.
def soln8(n):
    return int(n+int(str(n)*2)+int(str(n)*3))

## Question 9: Python Program to Reverse a Given Number.
def soln9(num):
    return int(''.join([x for x in str(num)].__reversed__()))

## Question 10: Python Program to Calculate the Average of Numbers in a Given List.
def soln10(ls):
    return sum(ls)/len(ls)

## Question 11: Python Program to Count the Number of Digits in a Number.
def soln11(num):
    return len(str(num))

## Question 12: Python Program to Check if a Number is a Palindrome.
def soln12(num):
    return len([(x,x) for x in range(len(str(num))) if str(num)[x] == str(num)[-(1+x)]]) == len(str(num))

## Question 13: Python Program to print the number of occurrence of a sub string in a given string.
def soln13(s,ss):
    return s.count(ss)

## Question 14: Python program to print the lowest index in the string where substring sub is found within the string.
def soln14(str1,sstr):
    return str1.find(sstr)

## Question 15: Python Program to return true if all characters in the string are alphabetic and there is at least one other character, False.
def soln15(str1):
    return str1.isalpha()

## Question 16: Python Program to Replace all Occurrences of ‘a’ with $ in a String.
def soln16(str1,st,st2):
    return ''.join([x if x != st else st2 for x in str1])

## Question 17: Python Program to Count the Number of Vowels in a String.
def soln17(str1):
    return len([x for x in str1 if x.lower() in 'aeiou' ])

## Question 18: Python Program to Take in a String and Replace Every Blank Space with Hyphen.
def soln18(str1):
    return '-'.join(str1.split(' '))

## Question 19: Python Program to find the length of string without using any built-in functions.
def soln19(str1):
    count = 0
    for ch in str1:
        count += 1
    return count

## Question 20: Python Program to Take in Two Strings and Display the Larger String without Using Built-in Functions.
def soln20(str1,str2):
    l1 = 0
    l2 = 0
    for c in str1:
        l1 += 1
    for c in str2:
        l2 += 1
    return l1 <= l2

## Question 21: Python Program to Calculate the Number of Upper Case Letters and Lower Case Letters in a String.
def soln21(str1):
    ucount = 0
    lcount = 0
    for c in str1:
        if c.isupper():
            ucount += 1
        else:
            lcount += 1
    return (ucount,lcount)

## Question 22: Python Program to Calculate the Number of Digits and Letters in a String.
def soln22(str1):
    ncount = 0
    acount = 0
    for c in str1:
        if c.isalpha():
            acount += 1
        elif c.isdigit():
            ncount += 1
    return (acount,ncount)

## Question 23: Python Program to check whether a full pattern (not sub string) is present in the given sentence.
def soln23(str1,pattern):
    return [ch for ch in str1.split(' ') if ch == pattern ] != []

## Question 24: Cumulative sum of a list [1, 2, 4, …] is defined as  [1, 3, 7, . . .] Write a function cumulative_sum() to compute cumulative sum of a list
def cumulative_sum(l):
	cumulative_sum_list = []
	for i in range(0,len(l)):
		cumulative_sum_list.append(sum(l[0:i+1]))
	return cumulative_sum_list

def soln24(l):
    return cumulative_sum(l)

## Question 25: Write a program to generate 10 random integers.
def soln25():
    return [random.randint(1,100) for x in range(10)]

## Question 26: Write a program to generate 10 random integers between 1 to 20 (both inclusive).
def soln26():
    return [random.randint(1,20) for x in range(10)]

## Question 27: Write a program to generate 5 random integers between 1 to 20 such that numbers should be unique.
def soln27():
    return random.sample(range(1,20), 5)

## Question: Write a program to generate 10 random numbers between 1 to 100 such that there should one number between 1 to 10 one number between 11 to 20 etc.
def soln28():
    return [random.randint((10*i)+1,10*(i+1)) for i in range(0,10)]