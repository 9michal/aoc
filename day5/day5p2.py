file = open("file.txt", "r")

ints = file.read()
ints = ints.split(",")

file.close()

for i in range(len(ints)):
    ints[i] = int(ints[i])

i = 0
while str(ints[i])[:-3:-1] != '99':     # DE (last two numbers) in opcode is not 99
    full = str(ints[i]).zfill(5)        # zfill is for 0 at the begining of string
    instruction = int(full[3:])         # E

    if (instruction == 1):
        i1 = ints[i + 1] if full[2] == '1' else ints[ints[i + 1]]
        i2 = ints[i + 2] if full[1] == '1' else ints[ints[i + 2]]
        i3 = ints[i + 3]
        ints[i3] = i1 + i2
        i += 4
        
    elif (instruction == 2):
        i1 = ints[i + 1] if full[2] == '1' else ints[ints[i + 1]]
        i2 = ints[i + 2] if full[1] == '1' else ints[ints[i + 2]]
        i3 = ints[i + 3]
        ints[i3] = i1 * i2
        i += 4

    elif (instruction == 3):
        ints[ints[i + 1]] = 5 #input 5
        i += 2

    elif (instruction == 4):
        i1 = ints[i + 1] if full[2] == '1' else ints[ints[i + 1]]
        print(i1)
        i += 2

    elif (instruction == 5):
        i1 = ints[i + 1] if full[2] == '1' else ints[ints[i + 1]]
        i2 = ints[i + 2] if full[1] == '1' else ints[ints[i + 2]]
        if (instruction == 5 and i1):
            i = i2
        else:
            i += 3

    elif (instruction == 6):
        i1 = ints[i + 1] if full[2] == '1' else ints[ints[i + 1]]
        i2 = ints[i + 2] if full[1] == '1' else ints[ints[i + 2]]
        if (instruction == 6 and not i1):
            i = i2
        else:
            i += 3

    elif (instruction == 7):
        i1 = ints[i + 1] if full[2] == '1' else ints[ints[i + 1]]
        i2 = ints[i + 2] if full[1] == '1' else ints[ints[i + 2]]
        i3 = ints[i + 3]
        ints[i3] = i1 < i2
        i += 4

    elif (instruction == 8):
        i1 = ints[i + 1] if full[2] == '1' else ints[ints[i + 1]]
        i2 = ints[i + 2] if full[1] == '1' else ints[ints[i + 2]]
        i3 = ints[i + 3]
        ints[i3] = i1 == i2
        i += 4



