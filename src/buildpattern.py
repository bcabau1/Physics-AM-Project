import os

from matplotlib import pyplot as plt
import math

global file


class LineBuilder:

    def __init__(self, line):
        self.line = line
        self.xs = list(line.get_xdata())
        self.ys = list(line.get_ydata())
        self.cid = line.figure.canvas.mpl_connect('button_press_event', self)
        global file
        file = input("Enter file name: ")
        self.f = open(file, 'w+')
        self.btw = float(input("Distance between points(.002 = 20 microns): "))
        if self.btw > 1:
            self.btw = 0.002

    def __call__(self, event):
        if plt.get_current_fig_manager().toolbar.mode != '': return
        # print('click', event)
        if event.inaxes != self.line.axes: return
        self.npx = list()
        self.npy = list()
        self.npx.append(float(self.xs[-1]))
        self.npy.append(float(self.ys[-1]))
        self.xs.append(event.xdata)
        self.ys.append(event.ydata)

        self.dist = math.sqrt(((self.npx[0] - self.xs[-1]) ** 2) + ((self.npy[0] - self.ys[-1]) ** 2))
        self.npts = int(self.dist // self.btw) - 1
        if self.npts == 0:
            self.npts = 1
        self.stepx = (self.xs[-1] - self.npx[0]) / self.npts
        self.stepy = (self.ys[-1] - self.npy[0]) / self.npts
        self.a = self.npx[0] + self.stepx
        self.b = self.npy[0] + self.stepy
        for d in range(self.npts):
            self.npx.append(self.a)
            self.npy.append(self.b)
            self.a = self.stepx + self.a
            self.b = self.stepy + self.b

        print("X: ", end=" ")
        print(self.npx)
        print("Y: ", end=" ")
        print(self.npy)

        # write to file

        for i in range(len(self.npx)):
            #   self.f.write("2HM X =" + str(self.npx[i]) + " Y =" + str(self.npy[i]) + "\n")
            self.f.write(str(self.npx[i]) + ";" + str(self.npy[i]) + "\n")

        self.line.set_data(self.xs, self.ys)
        self.line.figure.canvas.draw()


fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_title('Micron-scaled Pattern Drawing')
ax.set_xlabel('centimeter(s)')
ax.set_ylabel('centimeter(s)')
line, = ax.plot([0], [0], linestyle=':')  # empty line
linebuilder = LineBuilder(line)
plt.grid(True)
plt.show()


def handle_close(evt):
    file.close()


fig.canvas.mpl_connect('close_event', handle_close)

