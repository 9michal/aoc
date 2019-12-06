nf = open("file.txt", "r")

file = nf.readlines()

f = {}				# dict with string and list of strings
o = { 'COM': 0 }	# dict with string and int

for line in file:
	x, y = line.split(')')
	if x not in f:
		f[x] = []	# new list for every object
	f[x].append(y)




nf.close()