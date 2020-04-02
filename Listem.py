import matplotlib.pyplot as plt1
global scale

file1 = input("Enter the same file name: ")
f1 = open(file1)
file2 = input("Final file name: ")
f2 = open(file2, "w")
global scale
scale = int(input("Adjust scale of pattern(>= 1): "))
if scale < 1:
    scale = 100000
arr = [[], []]

for line1 in f1:
    if line1 == '':
        break
    line1 = line1.strip()
    line1 = line1.split(';')
    line1 = list(map(float, line1))
    line1[0] = line1[0] * scale
    line1[1] = line1[1] * scale
    arr[0].append(line1[0])
    arr[1].append(line1[1])
    print("2HM X =", int(line1[0]), "Y =", int(line1[1]))
    f2.write("2HM X =" + str(int(line1[0])) + " Y =" + str(int(line1[1]))+"\n")

fig1 = plt1.figure()
ax1 = fig1.add_subplot(111)
ax1.set_xlabel('micrometer(s)')
ax1.set_ylabel('micrometer(s)')
plt1.plot([arr[0]], [arr[1]], 'g.')
plt1.axis('image')
plt1.show()

f1.close()
f2.close()