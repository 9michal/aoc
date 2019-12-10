f1 = open("path1.txt", "r")
f2 = open("path2.txt", "r")

p1 = f1.read()
p2 = f2.read()

path1 = p1.split(",")
path2 = p2.split(",")


class  Point:
	def __init__(self, x, y):
		self.px = x
		self.py = y

	def sumofcoords(self):
		return abs(self.px) + abs(self.py)


def move(line):
	x, y = 0, 0
	pointslist = []
	for m in line:
		direction = m[0]
		steps = int(m[1:])
		for _ in range(steps):
			if direction == 'R':
				x = x + 1
			elif direction == 'L':
				x = x - 1
			elif direction == 'U':
				y = y + 1
			elif direction == 'D':
				y = y - 1
			p = Point(x, y)
			pointslist.append(p)
	return pointslist


list1 = move(path1)
list2 = move(path2)

set1 = set((p.px, p.py) for p in list1)
inter = [p for p in list2 if (p.px, p.py) in set1]

maxint = 1000000
for i in inter:
	addcoords = i.sumofcoords()
	if addcoords < maxint:
		maxint = addcoords

print(maxint)


