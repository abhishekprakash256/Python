"""
run a sample python program and capture the output from the other program

"""

import os
import subprocess

import time

#runining through the system os command 
#os.system("python3 add.py")

#p1 = subprocess.run(['python3','add.py'],capture_output = True, text=True)

import subprocess

values = ((1,2),(2,3))

first = 1
second = 2
third = 3

command = "python add.py"

"""
for first, second in values: 
    # lazy use of universal_newlines to prevent the need for encoding/decoding
    p = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True, universal_newlines=True)  
    output, err = p.communicate(input="{}\n{}\n".format(first, second))
    # stderr is not connected to a pipe, so err is None
    print(first, second, "->", end="")
    # we just want the result of the command
    print(output[output.rfind(" "):-1])  # -1 to strip the final newline
"""


p = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True, universal_newlines=True)  
output, err = p.communicate(input="{}\n{}\n{}\n".format(first, second,third))
# stderr is not connected to a pipe, so err is None
print(first, second,third, "->", end="")
# we just want the result of the command
print(output[output.rfind(" "):-1])  # -1 to strip the final newline