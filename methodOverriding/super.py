class Animal:
    def sound(self):
        print("Animals make sounds")

class Dog(Animal):
    # Overriding the parent method
    def sound(self):
        super().sound()   # Call parent class method
        print("Dog barks")

# Create object
d = Dog()
d.sound()