'''Problem Statement: Plot the line x = 5 
and shade the region where x >= 5.'''

# Problem 1 Solution: Vertical Constraints

import matplotlib.pyplot as plt

# Define x values
x = [5, 5]
# y values chosen to extend the line across the figure
y = [0, 10]

# Plot the line x = 5
plt.plot(x, y, 'c--', label='x = 5')
# Shade the region where x >= 5
plt.fill_betweenx(y, 5, 10, color='yellow', label='x >= 5', alpha=0.35)

# Add labels and legend
plt.xlabel('X')
plt.ylabel('Y')
plt.legend(loc='upper left')
plt.title('Vertical Constraint: x >= 5')

# Set x and y limit
plt.xlim(0, 10)
plt.ylim(0, 10)

# Show plot
plt.grid(True)
plt.show()

