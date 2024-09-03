'''Problem Statement: Plot the line 3x - 4y = 0 
and shade the region where 3x - 4y <= 0.'''

# Problem 5 Solution: Constraints with Zero in R.H.S

import numpy as np
import matplotlib.pyplot as plt


# Define x range
x = np.linspace(0, 10, 400)
y = (3*x) / 4 # Solve for y

# Plot the line 3x - 4y = 0
plt.plot(x, y, 'r--', label='3x - 4y = 0')
# Shade the region where 3x - 4y <= 0
plt.fill_between(x, y, 10, color='lightgreen',  label='3x - 4y <= 0', alpha=0.4, where=(y <= x*3/4))

# Add labels and legend
plt.xlabel('X')
plt.ylabel('Y')
plt.legend(loc='lower right')
plt.title('Constraint: 3x - 4y <= 0')

# Set x and y limit
plt.xlim(0, 10)
plt.ylim(0, 10)

# Show plot
plt.grid(True)
plt.show()