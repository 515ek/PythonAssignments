## Name: Vivek Babu G R
## Date: 26-07-2018
## Assignment: Sample 3
## Question: Write a program files-only.py to find only file and not sub directories. Pass directory name as command line argument.
#####################################################################################################################################
import cat
import os

pname = cat.get_path()

flist = os.listdir(pname)

for f in flist:
	if os.path.isfile(f):
		print(os.path.abspath(f))