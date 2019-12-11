from itertools import permutations

file = open("file.txt", "r")

ints = file.readline()
ints = ints.split(",")
file.close()

ints = [int(x) for x in ints]

def icode(p, tin, ints):
    i = 0
    tc = 0
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
            if tc == 0:
                ints[ints[i + 1]] = p
            else:
                ints[ints[i + 1]] = tin
            tc += 1
            i += 2

        elif (instruction == 4):
            i1 = ints[i + 1] if full[2] == '1' else ints[ints[i + 1]]
            thrust = i1
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
    return thrust


maxThrust = 0
for one in permutations([0, 1, 2, 3, 4]):   # one - one permutation
    thrust = 0                              # thrust - thrust of permutation
    for p in one:                           # p - one digit in permutation
        thrust = icode(p, thrust, ints)
    maxThrust = max(maxThrust, thrust)

print(maxThrust)