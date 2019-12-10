file = open("data.txt", "r")

ints = file.read()
ints = ints.split(",")

file.close()

for i in range(len(ints)):
    ints[i] = int(ints[i])

n = len(ints)

for i in range(0, n-1, 4):
    i1 = ints[i]
    i2 = ints[i+1]
    i3 = ints[i+2]
    i4 = ints[i+3]
    # i1 = 1: add i2 and i3, i1 = 2: multiply i2 and i3
    # save in i4
    if (i1 == 1):
        ints[i4] = ints[i2] + ints[i3]
    elif (i1 == 2):
        ints[i4] = ints[i2] * ints[i3]
    elif (i1 == 99):
        break
 
print(ints[0])