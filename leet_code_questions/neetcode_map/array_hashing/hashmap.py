"""
The implementation of the hash map in python ans methods
"""

#decleration of the hash map 

test1 = {0:["zero"],1:["one"],2:["two","seven"],3:["three"],4:["four","five","six"]}
test2 = dict()


main_lst = []
for k in test1.values():
	main_lst.append(k)

print(main_lst) 


#updating and adding the elements 

test2.update({0:["zero","one"]})
test2[1]= ["three","four"]

#accesing the elements 

print(test2.items())

print(test1.keys())

for val in test1:
	print(val)


#updating the elements

test1[3] = "eight"

print(test1)

test1.update({3:"three"})
print(test1)


#updating a val if key is present 

for a in test1:
	if a == 1:
		test1[a].append("twelve")
print(test1)
