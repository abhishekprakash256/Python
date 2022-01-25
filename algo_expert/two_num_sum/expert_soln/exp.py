new_dict_0 = {"A": 1 , "B" : 2 , "C" : 3}

new_dict_1 = { 0 : "A"  , 1:"B" , 2:"C"}

new_dict_1.update({3:"D"})
for i in range(len(new_dict_1)):

	print(new_dict_1[i])

if new_dict_1[5]:
	print("yes")