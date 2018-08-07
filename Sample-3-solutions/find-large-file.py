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

#### Check for command line arguement for pathname ####
def get_size():
	if len(sys.argv) > 2:
		return sys.argv[2]
	else:
		print('Usage: python <script> <Dir_path> <size>\n')
		sys.exit()

def get_bytes(gsize):
	if gsize[-1] == 'K':
		return int(gsize[:-1])*1024
	elif gsize[-1] == 'M':
		return int(gsize[:-1])*1024*1024
	elif gsize[-1] == 'G':
		return int(gsize[:-1])*1024*1024*1024
	else:
		return int(gsize)

def find_large_files(pname, gsize):
	for f in os.listdir(os.path.abspath(pname)):
		if os.path.isfile(os.path.join(pname,f)):
			if os.path.getsize(os.path.join(pname,f)) >= gsize:
				lfiles.append(os.path.join(pname,f))
		elif os.path.isdir(os.path.join(pname,f)):
			find_large_files(os.path.abspath(f),gsize)

pname = cat.get_path()
gsize = get_size()
gsize = get_bytes(gsize)

flist = os.listdir(pname)
lfiles = []
find_large_files(pname,gsize)

for lf in lfiles:
	print(lf)