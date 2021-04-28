new_dict = {

"element_1" : 1,
"element_2" : 2,
"element_3" : 3,
"element_4" : 4
}


print(new_dict)                #print
print(new_dict["element_1"])    #element print
print(len(new_dict))             #len of dict

new_dict.update({"element_2": 5})      #updation of the element

new_dict ["elemenet_6"] = 6            #adding the new element
new_dict.update({"elemenet_7": 7}) 
print(new_dict.values())           #getting the values 
print(new_dict.items())            #getting the items
print(new_dict.popitem())          #removing the values
print(new_dict.get("element_1"))           #getting the values

for x in new_dict: #all elements print
	print(x)

for x in new_dict.values():
	print(x)
for x in new_dict.keys():
	print(x)

print()                              








