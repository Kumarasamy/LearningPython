class Dog(object):
	def __init__(self,name):
		self.name = name
		print self.name

class Cat():
	def __init__(self,name):
		self.name = name

class Person(object):
	def __init__(self,name):
		self.name = name
		self.pet = None

class Employee(Person):
	def __init__(self,name,salary):
		super(Employee,self).__init__(name)
		self.salary = salary

class Fish(object):
	pass

class Salamon(Fish):
	pass

rover = Dog("Rover")

satan = Cat("Satan")

mary = Person("Mary")

frank = Employee("Frank",1200000)

frank.pet = rover

flipper = Fish()

crouse = Salamon()
