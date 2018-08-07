## Name: Vivek Babu G R
## Date: 26-07-2018
## Assignment: Sample 3
## Question: Write a program copyfile.py to copy one file to another. It should accept two filenames as command-line arguments and copies the first one into the second.
##########################################################################################################################################################################
#!/usr/bin/python
import cat

files = cat.get_files(2)
print(files)
fd = cat.open_file(files[0],'r')
content = fd.read()
cat.close_file(fd)
fd = cat.open_file(files[1],'w')
fd.write(content)
print(len(content),'bytes written')