This is a simple command line utility written in Python.  It simply reads a pipe delimited text file with task ids (unique number), task name, and the command to be executed.

For example:
>>0|modify task list|vim ~/tasks.txt
>>1|check the weather|python weather.py

*weather.py is custom python app using forecast.io to display the forecast in the terminal*

The utility reads all lines and displays them in the terminal, then prompts you for a number.  When you enter the task number and press enter, the command is executed.