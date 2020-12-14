def amend(value, mask):
	out = value
	maskbits = list(map(lambda x: (len(mask) - (x[0] + 1), x[1]), filter(lambda x: x[1] != "X", enumerate(mask))))
	for p, b in maskbits:
		if (b == "1"):
			out = out | 1 << p
		else:
			out = out & ~(1 << p)
	return out

line = "mem[28709] = 2381953"	
print(int(line[line.find("[") + 1:line.find("]")]))

mask = ""
memory = {}
for line in open("input14.txt").readlines():
	if (line.startswith("mask")):
		_, newmask = line.split("=")
		mask = newmask.strip()
	elif (line.startswith("mem")):
		memadd = int(line[line.find("[") + 1:line.find("]")])
		value = int(line.split("=")[1].strip())
		memory[memadd] = amend(value, mask)
		
print(sum(memory.values()))

def setbit(v, b):
	return v | 1 << b
	
def clearbit(v, b):
	return v & ~(1 << b)
	
def amendAllFloaters(value, floaters):
	#print(f"v: {value}, f: {floaters}")
	if floaters == []:
		yield value
	else:
		yield from amendAllFloaters(setbit(value, floaters[0]), floaters[1:])
		yield from amendAllFloaters(clearbit(value, floaters[0]), floaters[1:])
	
	
def getFloaters(mask):
	return list(map(lambda x: (len(mask) - (x[0] + 1)), filter(lambda x: x[1] == "X", enumerate(mask))))

def applyMask(val, mask):
	return val | int(mask.replace("X", "0"), 2)
	
mask = "000000000000000000000000000000X1001X"
val = 42

memory = {}

for line in open("input14.txt").readlines():
	if (line.startswith("mask")):
		_, newmask = line.split("=")
		mask = newmask.strip()
	elif (line.startswith("mem")):
		memadd = int(line[line.find("[") + 1:line.find("]")])
		value = int(line.split("=")[1].strip())
		for m in amend(AllFloaters(applyMask(memadd, mask), getFloaters(mask)):
			memory[m] = value

print(sum(memory.values()))
