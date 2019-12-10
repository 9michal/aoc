file = open("/home/michal/Desktop/AOC/day9/file.txt", "r")

ints = file.readline()
ints = ints.split(",")
file.close()

ints = [int(x) for x in ints] + [0] * 1000
relative = 0
i = 0

while str(ints[i])[:-3:-1] != '99':     # DE (last two numbers) in opcode is not 99
    full = str(ints[i]).zfill(5)        # zfill is for 0 at the begining of string
    instruction = int(full[3:])         # E

    if (instruction in [1, 2, 4, 5, 6, 7, 8, 9]):
        if full[2] == '1':
            i1 = i + 1
        elif full[2] == '2':
            i1 = ints[i + 1] + relative
        elif full[2] == '0':
            i1 = ints[i + 1]

    if (instruction in [1, 2, 5, 6, 7, 8]):
        if full[1] == '1':
            i2 = i + 2
        elif full[1] == '2':
            i2 = ints[i + 2] + relative
        elif full[1] == '0':
            i2 = ints[i + 2]

    if (instruction in [1, 2, 7, 8]):
        if full[0] == '2':
            i3 = ints[i + 3] + relative
        elif full[0] == '0':
            i3 = ints[i + 3]

    if (instruction == 1):
        ints[i3] = ints[i1] + ints[i2]
        i += 4   

    elif (instruction == 2):
        ints[i3] = ints[i1] * ints[i2]
        i += 4

    elif (instruction == 3):
        if full[2] == '0' or full[2] == '1':
            ints[ints[i + 1]] = 1
        elif full[2] == '2':
            ints[ints[i + 1] + relative] = 1
        i += 2

    elif (instruction == 4):
        print(ints[i1])
        i += 2

    elif (instruction == 5):
        if (ints[i1] != 0):
            i = ints[i2]
        else:
            i += 3

    elif (instruction == 6):
        if (ints[i1] == 0):
            i = ints[i2]
        else:
            i += 3

    elif (instruction == 7):
        ints[i3] = 1 if ints[i1] < ints[i2] else 0
        i += 4

    elif (instruction == 8):
        ints[i3] = 1 if ints[i1] == ints[i2] else 0
        i += 4

    elif (instruction == 9):
        relative += ints[i1]
        i += 2