'''Problem Statement: Plot the line y = 3 
and shade the region where y <= 3.'''

# Problem 2 Solution: Horizontal Constraints

import matplotlib.pyplot as plt

# Define y values
y = [3, 3]
# x values chosen to extend the line across the figure
x = [0, 10]

# Plot the line y = 3
plt.plot(x, y, 'r--', label='y = 3')
# Shade the region where y <= 3
plt.fill_between(x, y[0], color='blue', label='y <= 3', alpha=0.18)

# Add labels and legend
plt.xlabel('X')
plt.ylabel('Y')
plt.legend(loc='upper right')
plt.title('Vertical Constraint: y <= 3')

# Set x and y limit
plt.xlim(0, 10)
plt.ylim(0, 10)

# Show plot
plt.grid(True)
plt.show()