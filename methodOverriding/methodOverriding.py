class Animal:
    def sound(self):
        print("Animal makes sounds")
        
class Dog(Animal):
    # Overriding the parent method
    def sound(self):
        print("Dog Barks")

        
# Create objects
a = Animal()
d = Dog()

# Call methods
a.sound()
d.sound()