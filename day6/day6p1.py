# orbits = {}
# f = open('file.txt')
# f = list(f.readlines())

# for o in f:
# 	n1, n2 = o.rstrip().split(')')
# 	orbits[n2] = n1


# def count(orbits, node):
# 	allOrb = 0
# 	curr_node = node
# 	while orbits.get(curr_node) != None:
# 		curr_node = orbits.get(curr_node)
# 		allOrb += 1
# 	return allOrb

# allOrbits = 0
# for node in orbits.keys():
# 	allOrbits += count(orbits, node)

# print(allOrbits)