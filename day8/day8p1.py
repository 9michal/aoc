file = open("file.txt", "r")

ints = file.read()
file.close()

x, y = 6, 25
size = x * y

listOfLayers = []

for i in range(0, len(ints)-1, size):
	listOfLayers.append(ints[i:i + size])

zeroLayer = list(layer.count("0") for layer in listOfLayers)
zeroLayerIndex = zeroLayer.index(min(zeroLayer))

print(listOfLayers[zeroLayerIndex].count('1') * listOfLayers[zeroLayerIndex].count('2'))