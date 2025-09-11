# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def __str__(self):
#         return f"{self.name}({self.age})"
    
# p1 = Person("Abhinandan" , 20)

# print(p1)

# class sum:
#     num1 = int(input("Enter A: "))
#     num2 = int(input("Enter B: "))
    
#     sum = num1+num2
    
#     # print("Total: ",sum)

# s = sum()
# print(s,sum)
    
    
class myclass:
    def __init__ (self,name,age):
        self.name= name
        self.age= age
        
name = input("Enter name: ")
age = int(input("Enter age: "))
p = myclass(name , age)
print("Name: ",p.name)
print("Age: ", p.age)

