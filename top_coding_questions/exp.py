mapper = {"e":1,"r":1,"t":1,"u":1}

word = "elly"

"""
for i in word:
	if i in mapper:
		mapper[i] = mapper[i] +1
print(mapper)
"""

mapper2 = {"u":2,"r":2,"t":1,"e":1}

mapper3 = {"u":1,"t":2,"r":1,"e":1}

if mapper == mapper3:
	print(True)
else:
	print(False)