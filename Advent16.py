inputtext = open("input16.txt").read()

validationtext, mytickettext, othertickettext = inputtext.split("\n\n")

ordered_constraints = []
validations = {}
for vtext in validationtext.split('\n'):
	print(vtext)
	name, constrainttext = vtext.split(":")
	constraints = []
	for ct in constrainttext.split(" or "):
		min, max = ct.split("-")
		constraints.append((int(min), int(max)))
		ordered_constraints.append((int(min), "("))
		ordered_constraints.append((int(max), ")"))
	validations[name] = constraints
	
combined_constraints = []
ordered_constraints.sort(key = lambda x: x[0])
open = 0
c = -1
for n, b in ordered_constraints:
	if b == "(":
		if open == 0:
			c = n
		open += 1
	elif b == ")":
		open -= 1
		if open == 0:
			combined_constraints.append((c, n))

badtickets = []
goodtickets = []
for ticket in othertickettext.strip().split('\n')[1:]:
	ticket_numbers = list(map(int, ticket.split(",")))
	badTicket = False
	for n in ticket_numbers:
		#print(f"tick: {n}")
		badNumber = True
		for cmin, cmax in combined_constraints:
			#print(f"testing {n} against {cmin, cmax}")
			if n >= cmin and n <= cmax:
				#print ("good")
				badNumber = False
			else:
				badTicket = True
		if badNumber:
			badtickets.append(n)
	if not badTicket:
		goodtickets.append(ticket_numbers)

print(badtickets)
print(sum(badtickets))

print(goodtickets)

def conforms_to_constraints(ticket_number, validation):
	for cmin, cmax in validations[validation]:
		if (ticket_number >= cmin and ticket_number <= cmax):
			return True
	return False
	
	
valid = {}

for col in range(len(goodtickets[0])):
	for v in validations:
		validation_holds = True
		for ticket in goodtickets:
			if (not conforms_to_constraints(ticket[col], v)):
				validation_holds = False
				break
		if (validation_holds):
			valid[col] = valid.get(col, [])
			valid[col].append(v)
					
print (f"there are {len(validations)} validations")
for v in valid:
	print (f"col {v} fits {len(valid[v])} items {valid[v]}")
	
assigned = {}

row_and_validations = [(k, v) for k, v in valid.items()]
row_and_validations.sort(key = lambda x: len(x[1]))
for r, vl in row_and_validations:
	for v in vl:
		if not v in assigned.keys():
			print(f"{r} assigned to {v}")
			assigned[v] = r
			
total = 1
for k in assigned.keys():
	if k.startswith("departure"):
		total *= int(mytickettext.strip().split(",")[assigned[k]])
		
print(total)
