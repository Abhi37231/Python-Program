class person:
    def __init__(self,name):
        self.name = name

class Empolyee(person):
    
    def show_role(self):
        print(self.name,"is an employee")

class manager(Empolyee):
    def deparment(self, dept):
        print(self.name,"manages",dept,"deparment")

mgr = manager("Abhinandan")
mgr.show_role()
mgr.deparment()
