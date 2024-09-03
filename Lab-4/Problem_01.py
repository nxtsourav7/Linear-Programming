# Problem 1 Solution :
import numpy as np
import matplotlib.pyplot as plt

# Calculate the Points for x1=0 then x2 and x2=0 then x1
A = (0, 6)
B = (5, 0)
C = (0, 20)
D = (20, 0)

# Plot points
plt.plot(*A, 'ro', label='A(0, 6)')
plt.plot(*B, 'ro', label='B(5, 0)')
plt.plot(*C, 'bo', label='C(0, 20)')
plt.plot(*D, 'bo', label='D(20, 0)')

# Draw lines
plt.plot([A[0], B[0]], [A[1], B[1]], label='12x_1 + 10x_2 = 60')
plt.plot([C[0], D[0]], [C[1], D[1]], label='4x_1 + 4x_2 = 80')

# Plot feasible region
x1 = np.linspace(0, 25, 400)
x2_line1 = (60 - 12*x1) / 10
x2_line2 = (80 - 4*x1) / 4
plt.fill_between(x1, x2_line1, 0, where=(x2_line1 >= 0), color='gray', alpha=0.5)
plt.fill_between(x1, x2_line2, 24, where= (x2_line2 <= 24), color='lightgreen', alpha=0.5)

# Plot settings
plt.xlim(0, 24)
plt.ylim(0, 24)
plt.xticks(np.arange(0, 25, step=1))
plt.yticks(np.arange(0, 25, step=1))
plt.xlabel('x_1')
plt.ylabel('x_2')
plt.title('Feasible Region for Linear Programming Problem')
plt.grid()
plt.legend()
plt.axis() # Set aspect ratio to square
plt.show()