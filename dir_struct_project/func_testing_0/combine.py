"""
the experimentation for the combiunation of the all the functionality
"""
#imports 
import json 
import subprocess
import shutil
import os

"""
steps to genrate the doc

Algo : 

	read the json and get the data 
	start the subprocess of the thread for sphix-qucik start
		replace the value in the commands
	run the sphinx-apidoc command with variables in placed
	get the files from the directory store it
	change the extension from py to rst
	make the files with rst file with files name 
	modify the conf.py file
		uncomment the path 
		insert the theme
		edit the extension in that
	modify the index.rst file
	command make clean
	command make html
"""


#reading the json file

config_file = open("project_config.json")

#loading the data as dictionary 
data = json.load(config_file)

#getting the data , print(data['repo_details'][0]['project_name'])

#start the subrpocess of the sphinx-quick start

first_cmd = ""
second_cmd = data['repo_details'][0]['project_name']
third_cmd = data['repo_details'][0]['author']
fourth_cmd = data['repo_details'][0]['version']
fifth_cmd = ""

"""
command = "sphinx-quickstart"

#-----------------start the subprocess -------------------------------------------------------------------

#opening the commands
p = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True, universal_newlines=True)  

#giving the input
output, err = p.communicate(input="{}\n{}\n{}\n{}\n{}\n".format(first_cmd, second_cmd,third_cmd,fourth_cmd,fifth_cmd))

#print(output[output.rfind(" "):-1])  # -1 to strip the final newline

#-------------------------------------------------------end the subprocess----------------------------------------------------

#-----------------------get the files from the directory-------------------------------------------------------------
"""

# the list of varibale length 
code_files = os.listdir(data['repo_details'][0]['code_dir'])

for i in code_files:
	#creation of the file
	f = open(i.split(".")[0]+".rst", "w")
	#copying the content of the file to another
	shutil.copyfile('template.rst',i.split(".")[0]+".rst")

