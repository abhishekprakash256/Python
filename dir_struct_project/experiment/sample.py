"""
The file to check for the subprocess and write in the file

"""

import os
import subprocess

x = "test_dir"

p1 = subprocess.run(['ls','test_dir'],capture_output = True,  text= True )


write = (p1.stdout)

#print(write)
f = open("myfile.txt", "w")
f.write(write)
f.close()
