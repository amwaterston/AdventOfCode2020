starting_grid = open("input17.txt").readlines()


class Grid:
	def __init__(self):
		self.grid = [{}, {}]
		self.minx = 0
		self.miny = 0
		self.minz = 0
		self.maxx = 0
		self.maxw = 0
		self.maxy = 0
		self.maxz = 0
		self.maxw = 0
		flip = 0
		
	def setxyzw(self, x, y, z, w):
		self.grid[self.flip][(x, y, z, w)] = "#"
		self.minx = min(self.minx, x-1)
		self.miny = min(self.miny, y-1)
		self.minz = min(self.minz, z-1)
		self.minw = min(self.minw, w-1)
		self.maxx = max(self.maxx, x+1)
		self.maxy = max(self.maxy, y+1)
		self.maxz = max(self.maxz, z+1)
		self.maxw = max(self.maxw, w+1)
		
	def setotherxyzw(self, x, y, z, w):
		self.grid[(self.flip + 1) % 2][(x, y, z, w)] = "#"
		self.minx = min(self.minx, x-1)
		self.miny = min(self.miny, y-1)
		self.minz = min(self.minz, z-1)
		self.minw = min(self.minw, w-1)
		self.maxx = max(self.maxx, x+1)
		self.maxy = max(self.maxy, y+1)
		self.maxz = max(self.maxz, z+1)
		self.maxw = max(self.maxw, w+1)
	
	def countNeighbours(self, cell):
		x, y, z, w = cell
		#print(f"checking {x, y, z}")
		n = 0
		for i in range(-1,2):
			for j in range(-1,2):
				for k in range(-1,2):
					for l in range(-1,2):
						if i == 0 and j == 0 and k == 0 and l == 0:
							continue
						#print(f"checking {x + i, y + j, z + k}")
						if (x+i, y+j, z+k, w+l) in self.grid[self.flip]:
							n += 1
		return n
	
	def tick(self):
		self.grid[(self.flip + 1) % 2] = {}
		for x in range(self.minx, self.maxx + 1):
			for y in range(self.miny, self.maxy + 1):
				for z in range(self.minz, self.maxz + 1):
					for w in range(self.minw, self.maxw + 1):
						n = self.countNeighbours((x, y, z, w))
						#print (f"{x, y, z} has {n} active neighbours")
						if (n == 2 or n == 3) and (x, y, z, w) in self.grid[self.flip]:
							#print(f"(x, y, z) stays on")
							self.setotherxyzw(x, y, z, w)
						elif n == 3 and (x, y, z, w) not in self.grid[self.flip]:
							#print(f"(x, y, z) turns on")
							self.setotherxyzw(x, y, z, w)
		self.flip = (self.flip + 1) % 2
	
	def printgrid(self):
		for z in range(self.minz, self.maxz+1):
			for y in range(self.miny, self.maxy+1):
				line = ""
				for x in range(self.minx, self.maxx+1):
					line = line + self.grid[self.flip].get((x, y, z), ".")
				print (line)
			print ("--")
			
		print(f"total cubes: {len(self.grid[self.flip])}")

	def loadgrid(self, starting_grid):
		self.minx = 0
		self.miny = 0
		self.minz = 0
		self.minw = 0
		self.maxx = len(starting_grid) - 1
		self.maxy = len(starting_grid[0]) - 1
		self.maxz = 0
		self.maxw = 0
		self.flip = 0
		self.grid = [{}, {}]
		for y, line in enumerate(starting_grid):
			for x, cell in enumerate(starting_grid[y].strip()):
				if (cell == "#"):
					self.setxyzw(x, y, 0, 0)

g = Grid()
g.loadgrid(starting_grid)
g.printgrid()
for _ in range(6):
	g.tick()
g.printgrid()
