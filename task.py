#! /usr/bin/python
v = "v2.0"

import os

# the app looks in the user's home directory for the task file
taskfile = str(os.environ['HOME']) + '/tasks.txt'

# opening tasks text file
ifile = open(taskfile,'rU')

b = '--------------------------------------------------------'
sp = (len(b)-9) * " "


print '\nTasks' + sp + v
print b
# creating an empty array.  this will be populated with all the tasks.
tasks = []

# Reading each line in my tasks file and using the .split function to tell python where my file is delimited.  My tasks file is comma delimited but you may use another delimiter.
for line in ifile:
	tasks.append(line.split(','))

for j in tasks:
    print j[0] + '\t' + j[1]

tasks_dict = dict()

for i in tasks:
    tasks_dict[i[0]] = [i[1],i[2]]

tac = "y"
taskid = ""

while tac =="y":
   taskid = raw_input("\nInput task number:  ")
   if tasks_dict.has_key(taskid) == True:
      tac = "n"
      taskcommand = tasks_dict[taskid][1]
   else:
      print "\nError!  You entered an incorrect paramenter.\n"
      ta = raw_input("Try again? (Y/N): ")
      tac = ta.lower()
      if tac != "y":
         print "\nNow Exiting.\n"
         quit()

print "\n" + b
os.system(taskcommand)
