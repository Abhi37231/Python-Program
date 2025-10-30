import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 35]

# Create a simple line plot
plt.plot(x, y, marker='o')

# Add labels and title
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title("Simple Line Plot Example")

# Show the graph
plt.show()