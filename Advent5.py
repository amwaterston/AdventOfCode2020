from functools import reduce

with open("input5.txt") as fp:
	inputstring = fp.read()

bps = list(map(str, inputstring.strip().split('\n')))

def midpoint(l, u):
	return int(((u-l) + 1) / 2) + l
	
def partition(bp):
	l = 0
	u = 127

	print (bp[:7])	
	for c in bp[:7]:
		if (c == "F"): u = midpoint(l, u)
		if (c == "B"): l = midpoint(l, u)
	row = l
	print (bin(row))

	l = 0
	u = 7
	print (bp[7:])
	for c in bp[7:]:
		if (c == "L"): u = midpoint(l, u)
		if (c == "R"): l = midpoint(l, u)
	col = l
	print (bin(col))
	return row * 8 + col
	
def seatid(bp):
	return int(f"0b{bp[:7].replace('F', '0').replace('B', '1')}", 2) * 8 +	int(f"0b{bp[7:].replace('L', '0').replace('R', '1')}", 2) 

m = 0	
seats = []
for bp in bps:
	sid = seatid(bp)
	m = max(m, sid)
	seats.append(sid)

for i in range(m):
	if i in seats:
		continue
	if (i - 1 in seats and i + 1 in seats):
		print (f"seat = {i}")
print (m)

print(reduce(lambda x,y:max(x,y),(map(lambda x:int(f"0b{x}",2),(map(lambda x: x.translate(str.maketrans("FBLR","0101")),open("input5.txt").readlines()))))))

print(reduce(lambda x,y:max(x,y),(map(lambda x:int(f"0b{x[:7]}",2)*8+int(f"0b{x[7:]}",2),(map(lambda x: x.translate(str.maketrans("FBLR","0101")),open("input5.txt").readlines()))))))

print(reduce(lambda x, y: max(x, y), (map((lambda x: int(f"0b{x[:7].replace('F','0').replace('B','1')}", 2)*8+int(f"0b{x[7:].replace('L','0').replace('R','1')}",2)), open("input5.txt").readlines()))))

print(max(map(lambda x: int(f"0b{x.translate(str.maketrans('FBLR','0101'))}", 2),open("input5.txt").readlines())))

