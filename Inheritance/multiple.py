class person:
    def __init__(self,name):
        self.name = name
class job:
    def __init__(self,salary):
        self.salary = salary

class employee(person,job):
    def __init__(self,name, salary):
        person.__init__(self,name)
        job.__init__(self,salary)
    def details(self):
        print("Name: ",self.name)
        print(self.name,"Earns",self.salary)
            

emp = employee("Abhinandan",60000)
emp.details()

          