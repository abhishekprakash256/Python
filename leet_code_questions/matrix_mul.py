#make a matrix multiplication program that take input and multiply the matrix on command 

mat1 = []
mat2 = []
sum = 0

#m =number of rows , n = number of cloumns
m1 = int(input(("Enter the number of rows of first matrix:- ")))
n1 = int(input(("Enter the number of column of first matrix:- ")))
m2 = int(input(("Enter the number of rows of second matrix:- ")))
n2 = int(input(("Enter the number of column of second matrix:- ")))

#taking the value input and storing in the first matrix

for i in range(0, m1):  
	row1=[]             #initializing the new row and clearing it
	for j in range(0 , n1):
		print("Enter the value of " + str(i) + " row " + str(j) + " column of the first matrix")
		val = int(input())
		row1.append(val)         #first appending 
	mat1.append(row1)	   #second time appending to store the value


#taking the value input and storing in the first matrix
for i in range(0, m2):  
	row2=[]             #initializing the new row and clearing it
	for j in range(0 , n2):
		print("Enter the value of " + str(i) + " row " + str(j) + " column of the second matrix")
		val_2 = int(input())
		row2.append(val_2)         #first appending 
	mat2.append(row2)	   #second time appending to store the value


#--------------------------------initilization of the blank matrix------------------------------#

mat3= []                 ##the blank matrix initilization 
for i in range(0,m1):
	row3=[]
	for j in range(0,n2):
		row3.append(0)
	mat3.append(row3)	


#-------------------------------------main logic for the calulation part--------------------------------------------#

#-----------------------------------calculation happens if only n1 == m2 ------------------------------------------#


if (n1 == m2):

	#iteration of the row of first matrix A
	for i in range(len(mat1)):
		#iteration of the column of matrix B
		for j in range(len(mat2[0])):
			#iteration of the rows of the B
			for k in range(len(mat2)):
				mat3[i][j] += mat1[i][k] * mat2[k][j]

else:

	print("Can't perform the calculation mismatch the number of rows and cloumns")


#printing of the first matrix 		
for i in range(0,m1):
	for j in range(0,n1):
		if (i < m1 ):
			print(mat1[i][j], end =" ")
		
	print(" ")				

#printing of the second matrix
for i in range(0,m2):
	for j in range(0,n2):
		if (i < m2):
			print(mat2[i][j], end = " ")

	print(" ")		


for i in mat3:
	print(i)










