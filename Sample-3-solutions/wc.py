## Name: Vivek Babu G R
## Date: 26-07-2018
## Assignment: Sample 3
## Question: Write a program wc.py that takes filename as argument and counts number of lines, words and chars in file.
#########################################################################################################################
#!/usr/bin/python
import cat

fname = cat.get_file()
fd = cat.open_file(fname,'r')
cc = 0
wc = 0
lc = 0

for ch in fd.read():
	cc += 1
cat.close_file(fd)

fd = cat.open_file(fname,'r')
for line in fd.readlines():
	for word in line.split(' '):
		wc += 1
	lc += 1
cat.close_file(fd)
print(lc,wc,cc)