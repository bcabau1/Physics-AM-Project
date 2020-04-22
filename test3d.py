from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import time

fig = plt.figure()
ax = Axes3D(fig)

totalx = .1
totaly = totalx
dist = 5

def galvo(a, b):
    lx = (totalx - float(a))
    ly = (totaly - float(b))
    thetaX = round((np.arctan(lx/2*dist)), 2)
    thetaY = round((np.arctan(ly/2*dist)), 2)

    dim = 2

    print("X angle: ", thetaX)
    print("Y angle: ", thetaY)

    # Define x,y plane.
    X, Y = np.meshgrid([-dim / 200, dim / 200], [-dim / 4, dim / 4])
    Z = (4 * Y * thetaX) / 200

    # Define inclined plane.
    X2, Y2 = np.meshgrid([-dim / 200, dim / 200], [-dim / 4, dim / 4])
    Z2 = (X2 * thetaY)

    # Plot x,y plane.
    sf = ax.plot_surface(X, Y + .5, Z + .01, color='gray', alpha=.5, linewidth=0, zorder=1)
    # Plot top half of inclined plane.
    sf1 = ax.plot_surface(X2, Y2 + .5, Z2 - .01, color='blue', alpha=.5, linewidth=0, zorder=3)
    return sf, sf1


ax.set_xlim(-.06, .06)
ax.set_ylim(0, dist)
ax.set_zlim(-.06, .06)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

file = input("Enter pattern file name: ")
f = open(file)
sf, sf1 = galvo(0, 0)
plt.show(block=False)
for line in f:
    if line == '':
        break
    sf.remove()
    sf1.remove()
    line = line.strip()
    line = line.split(';')
    line = list(map(float, line))
    sf, sf1 = galvo(line[0], line[1])
    plt.plot([line[0]], dist, [line[1]], 'b,')
    #print("X =", (line[0]), "Y =", (line[1]), "Z =", 0)
    fig.canvas.draw()

plt.show()
f.close()
