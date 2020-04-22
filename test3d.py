from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import time

fig = plt.figure()
ax = Axes3D(fig)

dim = 1
angle = 0.5  # <-- This is the variable

# Define x,y plane.
X, Y = np.meshgrid([-dim / 200, dim / 200], [-dim / 4, dim / 4])
Z = (4 * Y * angle) / 200

# Define inclined plane.
X2, Y2 = np.meshgrid([-dim / 200, dim / 200], [-dim / 4, dim / 4])
Z2 = (X2 * angle)

# Plot x,y plane.
ax.plot_surface(X, Y + .5, Z + .01, color='gray', alpha=.5, linewidth=0, zorder=1)
# Plot top half of inclined plane.
ax.plot_surface(X2, Y2 + .5, Z2 - .01, color='blue', alpha=.5, linewidth=0, zorder=3)

ax.set_xlim(-.06, .06)
ax.set_ylim(0, 5)
ax.set_zlim(-.06, .06)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

file = input("Enter pattern file name: ")
f = open(file)
arr = [[], []]
plt.show(block=False)
for line in f:
    if line == '':
        break
    line = line.strip()
    line = line.split(';')
    line = list(map(float, line))
    plt.plot([line[0]], 5, [line[1]], 'b,')
    arr[0].append(line[0])
    arr[1].append(line[1])
    print("X =", (line[0]), "Y =", (line[1]), "Z =", 0)
    fig.canvas.draw()

plt.show()
f.close()
