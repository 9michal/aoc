file = open('file.txt', 'r')
ints = file.read().strip()
ints = [int(x) for x in ints]
n = len(ints)
it = 100     # iterations

digits = [0, 1, 0, -1]

def ten(n): 
    return abs(n) % 10

for p in range(it):
    out = ''
    for i, c in range(n):
        