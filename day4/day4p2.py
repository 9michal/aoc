def twoDigits(x):
	v = False
	x = str(x)
	for i in range(0,5):
		if(x[i] == x[i + 1]):
			if(i < 4):
				if(x[i] != x[i + 2]):
					if(i > 0):
						if(x[i] != x[i - 1]):
							v = True
					else:
						v = True
			else:
				if(x[i] != x[i - 1]):
					v = True
	return v

def notDecrease(x):
	v = True
	x = str(x)
#	if list(x) == sorted(x):
#		v = False
	for i in range(5):
		if x[i+1] < x[i]:
			v = False
			break
	return v

numOfPasswords = 0
for i in range(193651, 649730): # Your puzzle input is 193651-649729.
	if twoDigits(i) & notDecrease(i):
		numOfPasswords = numOfPasswords + 1

print(numOfPasswords)