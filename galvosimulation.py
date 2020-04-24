from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import math

fig = plt.figure()
ax = Axes3D(fig)

totalx = 4.6
totaly = totalx
dist = 5
multiplier = 20
ratio = dist/40


def galvo(a, b):
    lx = -a
    ly = b

    thetaX = round(math.degrees((np.arctan(lx / (2 * dist)))), 4)
    thetaY = round(math.degrees((np.arctan(ly / (2 * dist)))), 4)
    mechthetaX = thetaX / 2
    mechthetaY = thetaY / 2
    dim = 2

    print("X mech-angle: ", mechthetaX, "X scan-angle: ", thetaX)
    print("Y mech-angle: ", mechthetaY, "Y scan-angle: ", thetaY)

    # Define y mirror
    X, Y = np.meshgrid([-dim / 4, dim / 4], [-dim * ratio, dim * ratio])
    Z = (5/dist * Y * (mechthetaY/100 + .45))
    #print(5/dist*Y)

    # Define x mirror
    X2, Y2 = np.meshgrid([-dim / 8, dim / 8], [-dim * (2 * ratio), dim * (2 * ratio)])
    Z2 = (X2 * (mechthetaX/100 + .45))

    # Plot y mirror.
    sf = ax.plot_surface(X, Y + (dist * .1), Z + .5, color='gray', alpha=.5, linewidth=0, zorder=1)  # y mirror
    # Plot x mirror
    sf1 = ax.plot_surface(X2, Y2 + (dist * .1), Z2 - .5, color='blue', alpha=.5, linewidth=0, zorder=3)  # x mirror

    sf._facecolors2d = sf._facecolors3d
    sf._edgecolors2d = sf._edgecolors3d
    sf1._facecolors2d = sf1._facecolors3d
    sf1._edgecolors2d = sf1._edgecolors3d
    ax.legend([sf, sf1], [[thetaX, '\N{DEGREE SIGN}'], [thetaY, '\N{DEGREE SIGN}']])

    return sf, sf1


ax.set_xlim(-2.5, 2.5)
ax.set_ylim(0, dist)
ax.set_zlim(-2.5, 2.5)
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
    sf, sf1 = galvo(line[0]*multiplier, line[1]*multiplier)
    plt.plot([line[0]*multiplier], dist, [line[1]*multiplier], 'b,')
    # print("X =", (line[0]), "Y =", (line[1]), "Z =", 0)
    fig.canvas.draw()

plt.show()
f.close()

