from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import math
import sys
import time

fig = plt.figure()
ax = Axes3D(fig)

totalx = 4.6
totaly = totalx
dist = float(input("Galvanometer mount distance from field(cm): "))
if dist < 1.2:
    dist = 1.2
multiplier = int(input("Pattern scale (1<=x<=50, 1 = .1 cm diameter, 50 = 5 cm diameter): "))
if multiplier > 50:
    multiplier = 50
ratio = dist / 40


def galvo(a, b):
    lx = -a
    ly = b

    thetaX = round(math.degrees((np.arctan(lx / (2 * dist)))), 4)
    thetaY = round(math.degrees((np.arctan(ly / (2 * dist)))), 4)
    mechthetaX = thetaX / 2
    mechthetaY = thetaY / 2
    dim = 2

    while abs(thetaX) <= 25:
        print("X mech-angle: ", mechthetaX, "X scan-angle: ", thetaX)
        print("Y mech-angle: ", mechthetaY, "Y scan-angle: ", thetaY)

        # Define y mirror
        X, Y = np.meshgrid([-dim / 4, dim / 4], [-dim * ratio, dim * ratio])
        Z = (5 / dist * Y * (thetaY / 100 + .45))
        # print(5/dist*Y)

        # Define x mirror
        X2, Y2 = np.meshgrid([-dim / 8, dim / 8], [-dim * (2 * ratio), dim * (2 * ratio)])
        Z2 = (X2 * (thetaX / 100 + .45))

        # Plot y mirror.
        sf = ax.plot_surface(X, Y + (dist * .1), Z + .5, color='gray', alpha=.5, linewidth=0, zorder=1)  # y mirror
        # Plot x mirror
        sf1 = ax.plot_surface(X2, Y2 + (dist * .1), Z2 - .5, color='blue', alpha=.5, linewidth=0, zorder=3)  # x mirror

        lxmirror = -((2 * .5) * np.tan(np.radians(thetaX))) #0.5 is distance between mirrors
        #print(thetaX)
        #print(lxmirror)
        vec3 = ax.plot([-2.5, 0], [(dist * .1), (dist * .1)], [0 - .5, 0 - .5], 'g:', linewidth=.9)
        vec2 = ax.plot([0, lxmirror], [(dist * .1), (dist * .1)], [0 - .5, 0 + .5], 'g:', linewidth=.9)
        vec1 = ax.plot([lxmirror, a], [(dist * .1), dist], [0 + .5, b], 'g:', linewidth=.9)

        sf._facecolors2d = sf._facecolors3d
        sf._edgecolors2d = sf._edgecolors3d
        sf1._facecolors2d = sf1._facecolors3d
        sf1._edgecolors2d = sf1._edgecolors3d
        ax.legend([sf, sf1], [[thetaX, '\N{DEGREE SIGN}'], [thetaY, '\N{DEGREE SIGN}']])

        return sf, sf1, vec1, vec2, vec3

    if abs(thetaX) > 25:
        sys.exit("Angle exceeds mechanical angle limit of +-12.5\N{DEGREE SIGN}. Please change scale of pattern or "
                 "distance from field.")


ax.set_xlim(-2.5, 2.5)
ax.set_ylim(0, dist)
ax.set_zlim(-2.5, 2.5)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

file = input("Enter pattern file name: ")
f = open(file)
sf, sf1, vec1, vec2, vec3 = galvo(0, 0)
plt.show(block=False)
for line in f:
    if line == '':
        break
    sf.remove()
    sf1.remove()
    l0 = vec1.pop()
    l1 = vec2.pop()
    l2 = vec3.pop()
    l0.remove()
    l1.remove()
    l2.remove()
    line = line.strip()
    line = line.split(';')
    line = list(map(float, line))
    sf, sf1, vec1, vec2, vec3 = galvo(line[0] * multiplier, line[1] * multiplier)
    plt.plot([line[0] * multiplier], dist, [line[1] * multiplier], 'g,')
    # print("X =", (line[0]), "Y =", (line[1]), "Z =", 0)
    plt.pause(.001)

    fig.canvas.draw()

plt.show()
f.close()
