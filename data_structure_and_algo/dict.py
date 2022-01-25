#----------------decleration of dictionary in python----------------------------------#

my_dict = {'name': "tom", 'age' : 7 , 'class': 'first'}

#------------printing the values from the table----------------------------------#
print(my_dict['name'], my_dict['age'])

#----------------------manipulation of the values in the dictionary-----------#

my_dict['age']= 8

print(my_dict['name'], my_dict['age'])

#------------------------deleting the value in the dictionary--------------------#

del my_dict['name']


print(my_dict)

#-------------------------------new decleration of dictionary------------------------#

new_dict = dict() #decleration of the dictionary 

new_dict = {'dave' : 100, "tom" : 565}


print(new_dict)

print(new_dict['dave'])

#---------------------------------nested dictionaries---------------------------------#

nest_dict = {"Employee": { "Name" : "Tom" , "ID": "565AGH3", "Salary": 5000 }}

print(type(nest_dict))


print(nest_dict["Employee"]["Name"])     #accessing the nsested elements


#-------------------------operations in the dictionaries--------------------------#


print(nest_dict.values())

print(nest_dict.keys())

#print(nest_dict.get("Name"))

my_dict = {'name': "tom", 'age' : 7 , 'class': 'first'}

for i in my_dict:
	print(i)


for i in my_dict.values():
	print(i)


for i in my_dict.keys():
	print(i)



for i in my_dict.items():
	print(i)


my_dict.pop("name")

print(my_dict)


