class Employee:
	"default employee class"
	empCount = 0
	
	def __init__(self, name, salary):
		self.name = name
		self.salary = salary
		Employee.empCount += 1
	
	def displayCount(self):
		print("Total number of employees: %s") % Employee.empCount
		
	def displayEmployee(self):
		print "Name: ", self.name, ", ", "Salary:", self.salary
		
employee1 = Employee("Louis", 3000)
employee2 = Employee("Harvey", 90000)
employee3 = Employee("Mike", 2300)
employee1.age = 45

employee1.displayEmployee()
print employee1.age
employee2.displayEmployee()
employee3.displayEmployee()


print "Total number of employees: %s" % Employee.empCount
print Employee.__doc__
print Employee.__name__
print Employee.__module__
print Employee.__bases__
print Employee.__dict__