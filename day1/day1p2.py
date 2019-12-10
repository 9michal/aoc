import math

def main():
    file = open("mass.txt", "r")
    f = file.readlines()

    fsum = 0
    arr_len = len(f)

    for i in range(arr_len):
        mass = int(f[i])
        fuel = math.floor(mass/3) -2
        fuel_total = fuel
        while (fuel > 0):
            fuel = math.floor(fuel/3) - 2
            if (fuel > 0):
                fuel_total = fuel_total + fuel
        fsum = fsum + fuel_total

    print(fsum)
    file.close()

if __name__ == "__main__":
    main()

