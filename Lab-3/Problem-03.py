'''Problem Statement: Plot the line 4x + 5y = 20
and shade the region where 4x + 5y <= 20.'''

# Problem 3 Solution: Constraints & Inequalities

import numpy as np
import matplotlib.pyplot as plt

# Define the range of x values
x = np.linspace(0, 10, 400)
# Solve for y
y = (20 - 4*x) / 5

# Plot the line 4x + 5y = 20
plt.plot(x, y, '-b', label='4x + 5y = 20')
# Fill the region where 5x + 4y <= 20 and y >= 0
plt.fill_between(x, y, color='orange',label='4x + 5y <= 20', alpha=0.30, where=(y >= 0))

# Add labels and legend
plt.xlabel('X')
plt.ylabel('Y')
plt.legend(loc='upper right')
plt.title('Constraint: 4x + 5y <= 20')

# Set x and y limit
plt.xlim(0, 10)
plt.ylim(0, 10)

# Show plot
plt.grid(True)
plt.show()