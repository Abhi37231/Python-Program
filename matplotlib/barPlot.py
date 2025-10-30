import matplotlib.pyplot as plt

# Data for the bar plot
categories = ['A', 'B', 'C', 'D', 'E']
values = [10, 20, 15, 25, 30]

# Create a bar plot
plt.bar(categories, values, color='skyblue')

# Add labels and title
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Simple Bar Plot Example')

# Show the plot
plt.show()
