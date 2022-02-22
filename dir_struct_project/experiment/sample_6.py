"""
The use of the seedir
"""


import seedir as sd

files = "./test_dir"


#printout is false for the not printing the cmd output
x = sd.seedir(files, printout= False)

from os import listdir

from os.path import isfile, join

mypath = "test_dir"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

print(onlyfiles)