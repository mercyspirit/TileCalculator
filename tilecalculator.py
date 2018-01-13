def find_cost(num_tiles, cost):
	return num_tiles*cost

def find_numtiles(width, height, w, l):
	floor = width*height*12
	tile_size = w*l
	return (floor/tile_size)

while True:
	try:
		width = int(input("Input width of floor in feet: "))
		break
	except:
		print("Not a number, try again.")
		continue

while True:
	try:
		height = int(input("Input height of floor in feet: "))
		break
	except:
		print("Not a number, try again.")
		continue

while True:
	try:
		w = int(input("Input tile width in inches: "))
		break
	except:
		print("Not a number, try again.")
		continue

while True:
	try:
		l = int(input("Input tile length in inches: "))
		break
	except:
		print("Not a number, try again.")
		continue

while True:
	try:
		cost = float(input("Input cost of each tile: $"))
		break
	except:
		print("Not a number, try again.")
		continue

print("Floor width: %d feet" % width)
print("Floor height: %d feet" % height)
print("Tile width: %d inches" % w)
print("Tile length: %d inches" % l)
print("Cost per tile: $%.2f" % cost)
num_tiles = find_numtiles(width, height, w, l)
print("Number of tiles needed: %d tiles" % num_tiles)
print()
print("Total cost: $%.2f" % find_cost(num_tiles, cost))