import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Coefficients
m1 = 2
m2 = 3
m3 = 4
c = 5

# Create a grid of points
x1_vals = np.random.uniform(-10, 10, 1000)
x2_vals = np.random.uniform(-10, 10, 1000)
x3_vals = np.random.uniform(-5, 5, 1000)

# Compute y
y_vals = m1 * x1_vals + m2 * x2_vals + m3 * x3_vals + c

# 3D scatter plot with x3 as color
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
sc = ax.scatter(x1_vals, x2_vals, y_vals, c=x3_vals, cmap='plasma')

# Add colorbar for x3
cbar = plt.colorbar(sc)
cbar.set_label('x3 value')

# Labels
ax.set_xlabel('x1')
ax.set_ylabel('x2')
ax.set_zlabel('y')
ax.set_title('y = m1*x1 + m2*x2 + m3*x3 + c (x3 shown as color)')

plt.show()
