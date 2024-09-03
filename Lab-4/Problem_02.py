# Problem 2 Solution :
import numpy as np
import matplotlib.pyplot as plt

# Calculate the Points for x1=0 then x2 and x2=0 then x1
A = (0, 8.33)
B = (5, 0)
C = (0, 24)
D = (40, 0)

# Plot points
plt.plot(*A, 'ro', label='A(0, 8.33)')
plt.plot(*B, 'ro', label='B(5, 0)')
plt.plot(*C, 'go', label='C(0, 24)')
plt.plot(*D, 'go', label='D(40, 0)')

# Draw lines
plt.plot([A[0], B[0]], [A[1], B[1]], label='20x_1 + 12x_2 = 100')
plt.plot([C[0], D[0]], [C[1], D[1]], label='3x_1 + 5x_2 = 120')

# Plot feasible region
x1 = np.linspace(0, 40, 400)
x2_line1 = (100 - 20*x1) / 12
x2_line2 = (120 - 3*x1) / 5
plt.fill_between(x1, np.minimum(x2_line1, x2_line2), 0, where=(x2_line1 >= 0) & (x2_line1 >= 0), color='lightgreen', alpha=0.5)

# Plot settings
plt.xlim(0, 40)
plt.ylim(0, 24)
plt.xticks(np.arange(0, 41, step=2))
plt.yticks(np.arange(0, 25, step=1))
plt.xlabel('x_1')
plt.ylabel('x_2')
plt.title('Feasible Region for Linear Programming Problem')
plt.grid()
plt.legend()
plt.axis() # Set aspect ratio to square
plt.show()