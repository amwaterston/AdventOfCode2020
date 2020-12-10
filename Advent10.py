adapters = list(map(int, open("input10.txt").readlines()))

adapters.sort()
print (adapters)

c1 = 0
c3 = 0
for i in range(1, len(adapters)):
	if adapters[i] - adapters[i-1] == 1:
		c1+=1
	else:
		c3+=1
		
if adapters[0] == 1:
	c1+=1
else:
	
	c3+=1
		
print((c3+1)*c1)

# part 2

adapters = [0] + adapters

runs = []
currentrun = 0
for i in range(1, len(adapters)):
	if (adapters[i] - adapters[i-1] == 1):
		currentrun += 1
	elif (currentrun != 0):
		runs.append(currentrun + 1)
		currentrun = 0
		
if (currentrun != 0):
	runs.append(currentrun + 1)
		
print(runs)

def countruns(c, t, arr):
	if (c > t):
		return 0
	if (c == t):
		#print (f"FOUND {arr}")
		return 1
	runs = 0
	#print (range(c + 1, c + 4))
	for i in range(c + 1, c + 4):
		runs += countruns(i, t, arr + [i])
	return runs

total = 1
for r in runs:
	total *= countruns(1, r, [1])
	
print(total)

