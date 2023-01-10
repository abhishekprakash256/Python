test = "mystring"

"""
new_str = ""

test.strip()

print(test[0:len(test) - 1])
last_piece = test[len(test)-1]
print(last_piece)

x = "x"
print(x+last_piece)

"""


def fact(nums):
	if nums == 1 or nums == 0:
		return 1
	else:
		return nums*fact(nums - 1) 

print(fact(5))

lst = [1,2,3,4]


def cal_sum(lst):
	if len(lst) == 0:
		return 0
	else:
		return lst[len(lst)-1]+cal_sum(lst[0:len(lst)-1])
print(cal_sum(lst))


def cal_prod(lst):
	if len(lst) == 1:
		return lst[0]
	else:
		return lst[len(lst)-1]*cal_prod(lst[0:len(lst)-1])

print(cal_prod(lst))