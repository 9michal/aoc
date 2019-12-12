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


def getPathToStart(startPlanet, ):
    listOfPlanets = []
    planet = startPlanet
    while planet in orbits.keys():
        planet = orbits[planet]
        listOfPlanets.append(planet)
    return listOfPlanets

pathSAN = getPathToStart('SAN')
pathYOU = getPathToStart('YOU')
intersect = [x for x in pathSAN if x in pathYOU]
intersectFirst = intersect[0]

def pathL(startPlanet, inter):
    planet = startPlanet
    pathLength = 0
    while planet in orbits.keys() and planet != inter:
        planet = orbits[planet]
        pathLength += 1
    return pathLength

pathSANtoYOU = pathL('SAN', intersectFirst) + pathL('YOU', intersectFirst) - 2 # -2 because "Between the objects they are orbiting - not between YOU and SAN."
print(pathSANtoYOU)