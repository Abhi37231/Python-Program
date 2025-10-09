class person:
    def __init__(self,name):
        self.name = name

class Empolye(person):
    def show_role(self):
        print(self.name,"is an empolye")
    
emp = Empolye("Abhinandan")
print("Name: ",emp.name)
emp.show_role()