import os
import re

file = input("Enter file name: ")
f = open(file)
file1 = input("Write to file name: ")
f1 = open(file1, "w")
line = f.readline()

for line in f:
    line = f.readline()
    if line == '':
        break
    line = line.strip()
    line = line.split(';')
    line = list(map(float, line))
    line[0] = line[0] * 1000
    line[1] = line[1] * 1000
    print("2HM X =",int(line[0]), "Y =", int(line[1]))
    f1.write("2HM X ="+ str(int(line[0]))+ " Y ="+ str(int(line[1]))+"\n")
    # commands for x/y stage go here
    # wait until check location before next command

f.close(), f1.close()