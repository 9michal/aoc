file = open("file.txt", "r")

ints = file.read()
ints = ints.split(",")
file.close()

for i in range(len(ints)):
    ints[i] = int(ints[i])

n = len(ints)

def code(noun: int, verb: int):
    ints_copy = ints.copy()
    ints_copy[1] = noun
    ints_copy[2] = verb
    for i in range(0, n-1, 4):
        instruction = ints_copy[i]
        i2 = ints_copy[i+1]
        i3 = ints_copy[i+2]
        i4 = ints_copy[i+3]
        # i1 = 1: add i2 and i3, i1 = 2: multiply i2 and i3
        # save in i4
        if (instruction == 1):
            ints_copy[i4] = ints_copy[i2] + ints_copy[i3]
        elif (instruction == 2):
            ints_copy[i4] = ints_copy[i2] * ints_copy[i3]
        elif (instruction == 3):
            ints_copy[i2] = int(input("in: "))
        elif (instruction == 4):
            print(i2)
        elif (instruction == 99):
            break
    return ints_copy[0]

for i in range(100):
    for j in range(100):
        if code(i, j) == 19690720:
            print(100*i+j)