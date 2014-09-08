#! /usr/bin/python

import os

# opening tasks text file
ifile = open('PATH TO TASK LIST.txt','rU')

print '\nTasks'
print '--------------------------------------'

# creating an empty array.  this will be populated with all the tasks.
tasks = []

# Reading each line in my tasks file and using the .split function to tell python where my file is delimited.  My tasks file is pipe delimited but you may use another delimiter.
for line in ifile:
	tasks.append(line.split('|'))

# Print each line of the array
for j in tasks:
	print j[0] + '\t' + j[1]

# Creating my input variable
op = input('\nInput task number:  ')

# Converting the op (option) variable to a string since below I will be matching to the number from my task lists which is a string
sop = str(op)

# After receiving the input, the application loops through the array again and if sop mataches the task number (k[0] - the first field in the tasks list), then the app executes the command.

for k in tasks:
	if k[0] == sop:
		os.system(k[2])


