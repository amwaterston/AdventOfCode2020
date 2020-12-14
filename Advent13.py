earliest, busids = open("input13.txt").readlines()

earliest = int(earliest)
rawbusids = list(map(lambda x: int(x.strip()) if x.strip() != "x" else -1, busids.split(',')))
print(earliest)
print(rawbusids)
busids = [b for b in rawbusids if b > 0]
ts=earliest
found = False
while(not found):
	for b in busids:
		if(ts % b == 0):
			print((ts-earliest) * b)
			found = True
			break
	ts += 1
	
offsetbusids = []
for b in range(len(rawbusids)):
	if rawbusids[b] != -1:
		offsetbusids.append((b, rawbusids[b]))
		
print(offsetbusids)
t = 1
ts = 1
for offset, busid in offsetbusids:
	print(f"o: {offset}, b: {busid}")
	while((t + offset) % busid != 0):
		t += ts
	ts *= busid
	print (f"ts = {ts}")
	
print(t)



