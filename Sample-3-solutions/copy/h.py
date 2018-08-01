## Name: Vivek Babu G R
## Date: 26-07-2018
## Assignment: Sample 3
## Question: Write a program head.py that takes a filename as command-line argument and prints the first 5 lines of it.
#########################################################################################################################
import cat

fname = cat.get_file()
fd = cat.open_file(fname,'r')
i = 0
while i < 5:
	print(fd.readline())
	i += 1

cat.close_file(fd)


