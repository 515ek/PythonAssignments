## Name: Vivek Babu G R
## Date: 26-07-2018
## Assignment: Sample 3
## Question: Write a program largest-file.py to find the largest file in the given directory.
##			 The program should accept the directory name as command-line argument and print path to the file (not just filename).
####################################################################################################################################
#!/usr/bin/python
import cat
import os

pname = cat.get_path()

flist = os.listdir(pname)
lfile = ''
lsize = 0
for f in flist:
	if os.path.isfile(f):
		if os.path.getsize(f) > lsize:
			lsize = os.path.getsize(os.path.join(pname,f))
			lfile = os.path.join(pname,f)
print(lfile,lsize)