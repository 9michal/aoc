import math

file = open("mass.txt", "r")
f = file.readlines()

fsum = 0
arr_len = len(f)
for i in range(arr_len):
    mass = int(f[i])
    fuel = math.floor(mass/3) -2
    fsum = fsum + fuel
print(fsum)
file.close()