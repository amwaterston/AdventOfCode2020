commands = list(map(lambda x: x.strip(), open("input12.txt").readlines()))

sp_position = (0, 0)
wp_position = (10, 1)

directions = {
	"N": (0, 1),
	"S": (0, -1),
	"E": (1, 0),
	"W": (-1, 0)
}

facings = {
	0: "E",
	90: "S",
	180: "W",
	270: "N"
}

def move(position, direction, amount):
	return (position[0] + direction[0] * amount, position[1] + direction[1] * amount)
	
for c in commands:
	d = c[:1]
	p = int(c[1:])
	
	print(c)
	print(f"moving waypoint from {wp_position}")
	if d in directions:
		wp_position = move(wp_position, directions[d], p)
	elif d == "R":
		for _ in range(0, p, 90):
			wp_position = (wp_position[1], wp_position[0] * -1)
	elif d == "L":
		for _ in range(0, p, 90):
			wp_position = (wp_position[1] * -1, wp_position[0])
	elif (d == "F"):
		print(f"moving ship from {sp_position}")
		sp_position = move(sp_position, wp_position, p)
		print(f"moving ship from {sp_position}")
	print(f"moving waypoint to {wp_position}")				
print(sp_position)
print(abs(sp_position[0]) + abs(sp_position[1]))
		
