"""
experimentation with the sphinx cmd input
"""
#the imports
import subprocess


#the main command 
command = "sphinx-quickstart"

#the inputs

first_cmd = ""
second_cmd = "ProjectName"
third_cmd = "Author"
fourth_cmd = "1"
fifth_cmd = ""

#opening the commands
p = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True, universal_newlines=True)  

#giving the input
output, err = p.communicate(input="{}\n{}\n{}\n{}\n{}\n".format(first_cmd, second_cmd,third_cmd,fourth_cmd,fifth_cmd))

#make clean and make html

