file = open("file.txt", "r")

ints = file.read()
file.close()

x, y = 25, 6
size = x * y

for i in range(size):
	for j in range(size):
		if ints[(j*size)+i] != "2":		# 2 is transparent, doesnt matter
			print("@" if ints[(j*size)+i] == "1" else " ", end="")
			break
	if (i+1) % x == 0:
		print()