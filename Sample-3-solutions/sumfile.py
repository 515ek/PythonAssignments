## Name: Vivek Babu G R
## Date: 26-07-2018
## Assignment: Sample 3
## Question: Write a program sumfile.py that takes a filename as argument and prints sum of all numbers in that file.
##			 It is assumed that the file will only have one number in every line.
#######################################################################################################################
import cat

fname = cat.get_file()
fd = cat.open_file(fname,'r')
filesum = 0

for line in fd.readlines():
	for word in line.strip().split(' '):
		filesum += int(word)
cat.close_file(fd)
print(filesum)