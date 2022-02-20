"""
Test the auto input with the python for sphinx
"""
import os
import subprocess
import time


first_comnd = subprocess.run(['sphinx-quickstart'],capture_output = True, text=True)

#strat the documentation
#os.system("sphinx-quickstart")

first_comd.stdin.write('\n')

print("in")

time.sleep(2)

print("in_1")

#second command 

first_comd.stdin.write('project_name\n')

time.sleep(2)

#third command

first_comd.stdin.write('author_name\n')

time.sleep(2)

#fourth command

first_comd.stdin.write('verison_\n')

time.sleep(2)

#five command 

first_comd.stdin.write('\n')


print(first_comd.stdout)