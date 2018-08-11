## Name: Vivek Babu G R
## Date: 26-07-2018
## Assignment: Sample 2
## Question: Write a python code to generate grade using dictionary. Dictionary should have student names as keys (assuming names are unique) 
##			 and subject_name and mark as value. There are 5 subjects for each student. Marks should be converted to grades (90 – 100 A+, 80-89 A etc).
#########################################################################################################################################################
stu_dict = {'stu1':{'s1':81, 's2':78, 's3':89, 's4':75, 's5':86}, 'stu2':{'s1':84, 's2':58, 's3':79, 's4':65, 's5':76}, 'stu3':{'s1':91, 's2':88, 's3':79, 's4':85, 's5':66}}
print(stu_dict)
grades = {'A+':(90 , 100), 'A':(80 , 89), 'B':(70 , 79), 'C':(60 , 69), 'E':(50 , 59), 'F':(0 , 50)}

for k,v in stu_dict.items():
	for key, val in v.items():
		for g, r in grades.items():
			if r[0] <= val <= r[1]:
				stu_dict[k][key] = (val, g)

print(stu_dict)