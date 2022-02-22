"""
The file to manipulate the content of the file or write in the file

"""

import os 
import sys
import fileinput

file_name = "index.rst"

open_file = open(file_name, 'r+')

for i in open_file:
	print(i)