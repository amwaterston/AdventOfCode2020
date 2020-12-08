program = list(map(lambda x: x.strip(), open("input8.txt").readlines()))

#print(program)

already_run = {}
instruction = 0
acc = 0

while (not instruction in already_run):
	already_run[instruction] = True
	(op, prm) = program[instruction].split(" ")
	if (op == "nop"):
		instruction = (instruction + 1)
	elif (op == "acc"):
		instruction = (instruction + 1)
		acc += int(prm)
	elif (op == "jmp"):
		instruction = (instruction + int(prm))
	else:
		print("uh oh")
		
print(acc)

def execute(ci, acc, switched, executed):
	if (ci == len(program)):
		print (f"Ended: {acc}")
		return True
	if (ci in executed):
		#print (f"Ended: {acc}")
		return False
	(op, prm) = program[ci].split(" ")
	#print (f"ci: {ci}, op: {op}, prm: {int(prm)}")
	if (op == "acc"):
		return execute(ci + 1, acc + int(prm), switched, executed + [ci])
	elif (op == "nop"):
		if not switched:
			execute(ci + int(prm), acc, True, executed + [ci])
		execute(ci + 1, acc, switched, executed + [ci])
	elif (op == "jmp"):
		if not switched:
			execute(ci + 1, acc, True, executed + [ci])
		execute(ci + int(prm), acc, switched, executed + [ci])

execute(0, 0, False, [])
