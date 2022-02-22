"""
writing into the specific location in the file
"""
import os 

with open('index.rst', 'r') as file:
    # read a list of lines into data
    contents = file.readlines()


#one method
#for i in data:
#	print(i)

"""
data[12] = "   test.rst"
data[13]='\n'
data[14]='   test_1.rst'
data[15]='\n'

print(data[12])

with open('index.rst', 'w') as file:
    file.writelines( data )"""




contents.insert(12,"   test.rst\n")
contents.insert(13,"   test_0.rst\n")

f = open("index.rst", "w")
contents = "".join(contents)
f.write(contents)
f.close()




