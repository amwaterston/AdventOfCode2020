rulestrings = open("input7.txt").readlines()

rules = {}

for rulestring in rulestrings:
	container, contents = rulestring.strip().replace("bags", "").replace("bag", "").split(" contain ")
	container = container.strip()
	if "no other" in contents:
		contents = []
	else:
		contents = list(map(lambda x: (int(x.strip()[:2].strip()), x.strip()[2:].strip()), contents[:-1].split(",")))
	rules[container] = contents
	

def traverse(current_rule):
	#print(current_rule)
	if (current_rule == "shiny gold"):
		return True
	elif current_rule in rules:
		for (_, rule) in rules[current_rule]:
			#print(f"testing rule: {rule}")
			if (traverse(rule)):
				#print("Found one")
				return True
		return False
	else:
		#print("end of line")
		return False
	
count = 0
for r in rules.keys():
	print ("starting new rule")
	if (traverse(r)):
		count += 1
	
print(count)

def bagcount(current_rule):
	if (len(rules[current_rule]) == 0):
		return 0
	t = 0
	for (c, rule) in rules[current_rule]:
		print (f"{c}: {rule}")
		t += c + c * bagcount(rule)
	return t
	
print(bagcount("shiny gold"))
