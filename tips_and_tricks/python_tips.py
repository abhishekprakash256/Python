"""
make use of the generator function

"""

my_lst_0 = [i for i in range(10)]

print(sum(my_lst_0))



my_lst_1 = (i for i in range(10))

print(sum(my_lst_1))

# dict trick 

my_dict = {"first": 1 , "second" : 2 , "third" : 3 , "fourth" : 4}

print(my_dict.get("zero"))


# the enumerate trick 

lst = [1,2,3,54,65,7,8,9]

lst_2 = [2,2,4,5,6,7,8,9]

for i in enumerate(lst):

	print(i)


#couting the number of the items in the list 

from collections import Counter

lst_2 = [2,2,4,5,6,7,8,9]
print(Counter(lst_2))

#the sting join 

str_lst = ["this", "is" , "test"]

new = " ".join(str_lst)

print(new)

# dictinoary merger

dict_0 = {"five":5, "six":6, "seven":7, "eight":8}

print({**my_dict, **dict_0})