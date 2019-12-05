import math
def main():
    fsum = 0
    file = open("mass.txt", "r")
    f = file.readlines()
    arr_len = len(f)
    for i in range(arr_len):
        mass = int(f[i])
        fuel = math.floor(mass/3) -2
        fsum = fsum + fuel
    print(fsum)
    file.close()

if __name__ == "__main__":
    main()