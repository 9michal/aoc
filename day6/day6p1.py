f = open("file.txt", "r")
file = f.readlines()
f.close()

allPlanets = set()
orbits = {}

for line in file:
    pt = line.split(')')
    pt1 = pt[0]
    pt2 = pt[1][:3] # '\n' at end: XXX\n
    allPlanets.add(pt1)
    allPlanets.add(pt2)
    orbits[pt2] = pt1  

orbitsSum = 0
for planet in allPlanets:
    while planet in orbits.keys():
        planet = orbits[planet]
        orbitsSum += 1

print(orbitsSum)