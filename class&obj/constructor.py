class Car:
    # default constructor
    def __init__(self):
        print("Default Constructor Called")

    def display(self, name, model, colour):
        # assign values to object
        self.name = name
        self.model = model
        self.colour = colour

        print("Name: ", self.name)
        print("Model: ", self.model)
        print("Colour: ", self.colour)


# creating object
obj = Car()
obj.display("Range-Rover", "M360", "White")
