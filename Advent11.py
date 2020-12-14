maplines = list(map(lambda x: x.strip(), open("input11.txt").readlines()))
height = len(maplines)
width = len(maplines[0])

class Seat:
	def __init__(self):
		self.isOccupied = False
		self.willBeOccupied = False
	
		self.adjacentseats = []
	
	def update(self):
		self.willBeOccupied = self.isOccupied
		occCount = 0
		for s in self.adjacentseats:
			if s.isOccupied:
				occCount += 1
		if not self.isOccupied and occCount == 0:
			self.willBeOccupied = True
		elif self.isOccupied and occCount >= 5:
			self.willBeOccupied = False
			
	def tick(self):
		if (self.isOccupied == self.willBeOccupied):
			return False
		else:
			self.isOccupied = self.willBeOccupied
			return True
	
class SeatMap:
	def __init__(self):
		self.seatmap = {}
	
	def populateSeatList(self, lines):
		for y in range(height):
			for x in range(width):
				if (lines[y][x] == "L"):
					self.seatmap[(x, y)] = Seat()
		for y in range(height):
			for x in range(width):
				if (lines[y][x] == "L"):
					adseats = self.findLineOfSightSeats(x, y, lines)
					for s in adseats:
						self.seatmap[(x, y)].adjacentseats.append(self.seatmap[s[0], s[1]])
					#print (f"counted {len(self.seatmap[(x, y)].adjacentseats)} adjacent seats")
						
		
					
	def findAdjacents(self, x, y, lines):
		seats = []
		diffs = [(1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]
		for d in diffs:
			cy = y + d[1]
			cx = x + d[0]
			if cx >= 0 and cy >= 0 and cx < width and cy < height and lines[cy][cx] == "L":
				seats.append((cx, cy))
		return seats
		
	def findLineOfSightSeats(self, x, y, lines):
		seats = []
		diffs = [(1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]
		for d in diffs:
			cy = y + d[1]
			cx = x + d[0]
			while (cx >= 0 and cy >= 0 and cx < width and cy < height):
				if (lines[cy][cx] == "L"):
					seats.append((cx, cy))
					break
				cy = cy + d[1]
				cx = cx + d[0]
		return seats
	
	def countOccupiedSeats(self):
		c = 0
		for s in self.seatmap.values():
			if s.isOccupied:
				c += 1
		return c
		
	def tick(self):
		for s in self.seatmap.values():
			s.update()
		changed = False;	
		for s in self.seatmap.values():
			changed = changed | s.tick()
		
		return changed
		
	def print(self):
		for y in range(height):
			out = ""
			for x in range(width):
				if (x, y) in self.seatmap:
					if self.seatmap[(x, y)].isOccupied:
						out += "#"
					else:
						out += "L"
				else:
					out += "."
			print(out)
	
sm = SeatMap()
sm.populateSeatList(maplines)
while sm.tick():
	True
print (sm.countOccupiedSeats())
