'''
make the custom data structure to store the profile of the employes
should have the add, modify , delete and update capabalities
'''

#create the employee class

class Employee:
	'''
	Employee: a class to store information for the employess

	'''
	def __init__(self,username, name,email):
		self.username = username
		self.name = name
		self.email = email
		#print("User created")


	def __repr__(self):
		return "User(username = '{}' , name = '{}' , email = '{}')".format(self.username , self.name , self.email)

	def __str__(self):
		return self.__repr__()



user_0 = Employee("username_0", "user_0", "email_0")

user_1 = Employee("username_1", "user_1", "email_1")

user_2 = Employee("username_2", "user_2", "email_2")

user_3 = Employee("username_3", "user_3", "email_3")


#make the custom data structure

class UserDatabase:
	'''
	the databse to store the user details
	'''

	def __init__(self):
		self.users = []

	def insert(self,user):
		i = 0 

		while i < len(self.users):

			if self.users[i].username > user.username:
				break
			i+=1

		self.users.insert(i, user)

	def find(self, username):
		
		for user in self.users:
			if user.username == username:
				return user
	
	def update(self,user):

		target = self.find(user.username)
		target.name, target.email = user.username, user.email  

	
	def list_all(self):
		return self.users
		


my_data = UserDatabase()

my_data.insert(user_0)

my_data.insert(user_1)

my_data.insert(user_2)

my_data.insert(user_3)


print(my_data.list_all())








