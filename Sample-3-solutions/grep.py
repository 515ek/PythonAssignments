## Name: Vivek Babu G R
## Date: 26-07-2018
## Assignment: Sample 3
## Question: Write a program grep.py that takes a pattern and a filename as command-line argument and prints all the lines in the file that contain given pattern.
####################################################################################################################################################################
import cat
import re

def find_match_lines(fd, pattern):
	mat = []
	for line in fd.readlines():
		if pattern.search(line):
			mat.append(line)
	return (mat,pattern)

def grep():
	names = cat.get_files(2)
	pattern = names[0]
	fd = cat.open_file(names[1], 'r')
	reg_pattern = re.compile(pattern)
	return find_match_lines(fd,reg_pattern)

if __name__ == '__main__':
	grep()