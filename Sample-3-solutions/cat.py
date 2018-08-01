## Name: Vivek Babu G R
## Date: 26-07-2018
## Assignment: Sample 3
## Question: Write a program cat.py that takes a filename as command-line argument and prints all the contents of that file.
##############################################################################################################################
import sys
import os

#### Check for command line arguement ####
def get_file():
	if len(sys.argv) > 1:
		return sys.argv[1]
	else:
		print('Usage: python <script> <filename>\n')
		sys.exit()

#### Check for command line arguement for pathname ####
def get_path():
	if len(sys.argv) > 1:
		return sys.argv[1]
	else:
		print('Usage: python <script> <Dir_path>\n')
		sys.exit()

#### Check for command line arguements for file names ####
def get_files(num):
	if len(sys.argv) >= num+1:
		return [sys.argv[f] for f in range(1,num+1)]
	else:
		print('Usage: python <script>','<filename> '*num,'\n')
		sys.exit()

#### Check for presense of given file and open if True else give instruction ####
def open_file(fname, mode):
	try:
		fd = open(fname,mode)
		return fd
	except IOError:
		print("File not present in pwd \\ give abs path of file:",fname)
		sys.exit()
	except Exception as e:
		print(e)
		sys.exit()

#### UD Function to close the file ####
def close_file(fd):
	fd.close()

#### Function to simulate 'cat' command ####
def cat():
	fname = get_file()
	fd = open_file(fname,'r')
	print(fd.read())
	close_file(fd)

if __name__ == '__main__':
	cat()