"""
Find all the pythagorean triplets sum to 100000


3^2 + 4^2 = 5^2

"""

def find_pythagorean_triplet(num:int)->int:
	"""
	The function gives the pythagorean triplets

	Arguments:
		num (int) -> the number to which find the triplets 

	Returns:
		triplets (int) -> the triplet numbers


	"""

	triplet_lst = []

	for i in range(1,num+1):

		a = i*i

		for j in range(i,num+1):

			b = j*j

			for c in range(j,num+1):

				d = c*c

				if a + b == d:
					
					triplet_lst.append((i,j,c))

	if len(triplet_lst) == 0:
		return "No triplet found"

	return triplet_lst


print(find_pythagorean_triplet(1))

