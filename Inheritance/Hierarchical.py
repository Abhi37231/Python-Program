class person:
    def __init__(self,name):
        self.name = name

class Employee(person):
    
    def role(self):
        print(self.name," works as employee")

class  Intern(person):
    def role(self):
        print(self.name,"is an intern")


emp = Employee("Abhinandan")
emp.role()

intern = Intern("Ganesh")
intern.role()