from matplotlib import pyplot as plt
import pylab as pl
import scipy as sp
import math
import mpl_toolkits.mplot3d as a3
import matplotlib.colors as colors

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d', proj_type='ortho')
dist = 5

ax.set_xlim(-.05, .05)
ax.set_ylim(0, dist)
ax.set_zlim(-.05, .05)

file = input("Enter pattern file name: ")
f = open(file)
arr = [[], []]
for line in f:
    if line == '':
        break
    line = line.strip()
    line = line.split(';')
    line = list(map(float, line))
    plt.plot([line[0]], 5, [line[1]], 'g.')
    arr[0].append(line[0])
    arr[1].append(line[1])
    print("2HM X =", (line[0]), "Y =", (line[1]))
    fig.canvas.draw()

plt.show()
f.close()
