file = open('file.txt', 'r')
ints = file.read().strip()
ints = [int(x) for x in ints]
n = len(ints)
iterations = 100

p = [0, 1, 0, -1]

def ten(n): 
    return abs(n) % 10

for i in range(iterations):
    for j in range(n):
        
        