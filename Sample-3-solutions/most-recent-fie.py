## Name: Vivek Babu G R
## Date: 26-07-2018
## Assignment: Sample 3
## Question: Write a program most-recent-file.py to find the most recently modified file in the given directory. 
##			 The program should accept the directory name as command-line argument and print path to the file (not just filename) that is most recently modified file.
########################################################################################################################################################################
import cat
import os

pname = cat.get_path()

flist = os.listdir(pname)
mrfile = ''
mtimes = 0
for f in flist:
	if os.path.isfile(f):
		if mtimes < os.path.getmtime(f):
			mtimes = os.path.getmtime(f)
			mrfile = os.path.abspath(f)
print(mrfile)