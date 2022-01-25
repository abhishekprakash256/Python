#make the class and the instance variables 

class Employee:
    number_of_employee = 0
    def __init__(self,name, age, pay):
        self.name = name 
        self.age = age
        self.pay = pay
        Employee.number_of_employee +=1
    def printer(self):
        return self.name, self.age,self.pay

class Developer(Employee):
    def __init__(self,name,age,pay,prog_l):
        super().__init__(name,age,pay)
        self.prog_l = prog_l
    def printer(self):
        return  self.name, self.age,self.pay, self.prog_l

class Manager(Employee):
    def __init__(self,name,age,pay,employees= None):
        super().__init__(name,age,pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    

#print(Employee.number_of_employee)
emp_1 = Employee("Sam",26,100000)
emp_2 = Employee("Ram",23,384384)


dev_1 = Developer("Shiv",24,3445454,"PYP")


print(Developer.printer(dev_1))

'''
print(emp_1.__dict__)

print(emp_1.printer())

print(Employee.printer(emp_1))

print(Employee.number_of_employee)

print(help(Developer))'''