class Car:

  increase = 1.5	
  def __init__(self, name, model):
    self.name = name
    self.model = model
  def sample_fun(self):   #pass self in it
  	print("do something")
  def new_price(self):
  	price = price * increase	  


car_1 = Car("TATA","model s")

print(car_1.name)
print(car_1.__dict__)
print(Car.__dict__)