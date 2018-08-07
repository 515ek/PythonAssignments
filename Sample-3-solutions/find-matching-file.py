## Name: Vivek Babu G R
## Date: 26-07-2018
## Assignment: Sample 3
## Question: Write a program find-large-files.py to find files recursively in a directory tree that are larger than given size. 
##			 The program should accept the directory and the size as command-line argument.
##			 The size can be also be specified with K, M and G suffix for KB, MB and GB respectively.
#################################################################################################################################
#!/usr/bin/python
import cat
import sys
import os
import re

#### Check for command line arguement for pattern ####
def get_pattern():
	if len(sys.argv) > 2:
		return sys.argv[2]
	else:
		print('Usage: python <script> <Dir_path> <pattern>\n')
		sys.exit()

def find_match_files(pname, pattern):
	for f in os.listdir(os.path.abspath(pname)):
		if os.path.isfile(os.path.join(pname,f)):
			if pattern.search(f):
				lfiles.append(os.path.join(pname,f))
		elif os.path.isdir(os.path.join(pname,f)):
			find_match_files(os.path.abspath(f),pattern)

pname = cat.get_path()
pattern = get_pattern()
reg_pattern = re.compile(pattern)
flist = os.listdir(pname)
lfiles = []
find_match_files(pname,reg_pattern)

for lf in lfiles:
	print(lf)