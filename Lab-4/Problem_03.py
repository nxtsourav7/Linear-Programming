# Problem 3 Solution :
import numpy as np
import matplotlib.pyplot as plt

# Calculate the Points for x = 0 then y and y = 0 then x
A = (0, 8)
B = (2, 0)
C = (0, 15)
D = (9, 0)
E = (0, 9)
F = (10, 0)

# Plot points
plt.plot(*A, 'ro', label='A(0, 8)')
plt.plot(*B, 'ro', label='B(2, 0)')
plt.plot(*C, 'go', label='C(0, 15)')
plt.plot(*D, 'go', label='D(9, 0)')
plt.plot(*E, 'bo', label='E(0, 9)')
plt.plot(*F, 'bo', label='F(10, 0)')

# Draw lines
plt.plot([A[0], B[0]], [A[1], B[1]], label='8x + 2y = 16')
plt.plot([C[0], D[0]], [C[1], D[1]], label='5x + 3y = 45')
plt.plot([E[0], F[0]], [E[1], F[1]], label='9x + 10y = 90')

# Plot feasible region
x = np.linspace(0, 20,200)
y1 = (16 - 8*x) / 2
y2 = (45 - 5*x) / 3
y3 = (90 - 9*x) / 10
plt.fill_between(x, y1, np.minimum(y2, y3), where=(y2 >= 0) & (y3 >= 0) & (y1 <= np.minimum(y2, y3)), color='yellow', alpha=0.35)

# Plot settings
plt.xlabel('X')
plt.ylabel('Y')
plt.xlim(0, 15)
plt.ylim(0, 15)
plt.xticks(np.arange(0, 16, step=1))
plt.yticks(np.arange(0, 16, step=1))
plt.title('Feasible Region for Linear Programming Problem')
plt.grid()
plt.legend()
plt.axis() # Set aspect ratio to square
plt.show()