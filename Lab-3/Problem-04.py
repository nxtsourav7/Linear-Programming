'''Problem Statement: Plot the line 0.5x + 0.25y = 2.5 
and shade the region where 0.5x + 0.25y <= 2.5.'''

# Problem 4 Solution: Constraints with Decimal Points

import numpy as np
import matplotlib.pyplot as plt

# Define the range of x values
x = np.linspace(0, 10, 400)
y = 10 - 2*x  # Solve for y

# Plot the line 0.5x + 0.25y = 2.5
plt.plot(x, y, '-b', label='0.5x + 0.25y = 2.5')
# Fill the region where 0.5x + 0.25y <= 2.5 and y >= 0
plt.fill_between(x, y, color='grey',label='0.5x + 0.25y <= 2.5', alpha=0.30, where=(y >= 0))

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