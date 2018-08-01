## Name: Vivek Babu G R
## Date: 26-07-2018
## Assignment: Sample 1
## Question: Cumulative sum of a list [1, 2, 4, …] is defined as  [1, 3, 7, . . .] Write a function cumulative_sum() to compute cumulative sum of a list
##########################################################################################################################################################
def cumulative_sum(l):
	cumulative_sum_list = []
	for i in range(0,len(l)):
		cumulative_sum_list.append(sum(l[0:i+1]))
	print(cumulative_sum_list)

l = list(map(int,input('Enter the List of Numbers\n').split(' ')))
cumulative_sum(l)
