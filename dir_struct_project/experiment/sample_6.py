"""
The use of the seedir
"""
import seedir as sd

files = "./test_dir"

x = sd.seedir(files, printout= False)

print(x)
#print(x[1])

for i in x:
	print(i)