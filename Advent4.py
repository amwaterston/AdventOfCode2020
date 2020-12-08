import re
inputstring = ""
with open("input4.txt") as fp:
	inputstring = fp.read()

#byr (Birth Year) - four digits; at least 1920 and at most 2002.
#iyr (Issue Year) - four digits; at least 2010 and at most 2020.
#eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
#hgt (Height) - a number followed by either cm or in:
	#If cm, the number must be at least 150 and at most 193.
	#If in, the number must be at least 59 and at most 76.
#hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
#ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
#pid (Passport ID) - a nine-digit number, including leading zeroes.
#cid (Country ID) - ignored, missing or not.

expectedKeys = [
"byr", #(Birth Year)
"iyr",  #(Issue Year)
"eyr",  #(Expiration Year)
"hgt",  #(Height)
"hcl",  #(Hair Color)
"ecl",  #(Eye Color)
"pid",  #(Passport ID)
"cid"]  #(Country ID)

def intCheck(s, min, max):

	if (int(s) < min or int(s) > max): 
		#print (f"{min} <= {int(s)} <= {max}")
		#print("NO")
		return False
	return True
	
def checkcreds(h):
	if not intCheck(h["byr"], 1920, 2002): return False
	if not intCheck(h["iyr"], 2010, 2020): return False
	if not intCheck(h["eyr"], 2020, 2030): return False
	
	height = h["hgt"]
	print(f"{height}, {height[:-2]}")
	if height.endswith("in"):
		if (not (intCheck(height[:-2], 59, 76))): return False
	elif height.endswith("cm"):
		if (not (intCheck(height[:-2], 150, 193))): return False
	else: return False
	
	#print (h["hcl"])
	hclre = re.compile("#[0-9a-f]{6}")
	if not (len(h["hcl"]) == 7 and hclre.match(h["hcl"])): return False
	
	ec = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
	if not h["ecl"] in ec: 
		#3print (f"eye colour fail: {h['ecl']}")
		return False
	#else:
		#print (f"eye colour success: {h['ecl']}")
	
	pidre = re.compile("[0-9]{9}")
	if not (len(h["pid"]) == 9 and pidre.match(h["pid"])): return False
	
	return True
	
passportstrings = list(map(str, inputstring.strip().split('\n\n')))

passports = []
goodp = 0

for p in passportstrings:
	kvs = re.split(' |\n',p)
	h = {}
	for kv in kvs:
		(k, v) = kv.split(':')
		h[k] = v
	missingkeys = set(expectedKeys) - set(h.keys())
	if (len(missingkeys) == 0 or (len(missingkeys) == 1 and missingkeys.pop() == 'cid')):
		if (checkcreds(h)): goodp += 1
		
	passports.append(h)
	
print (goodp)
#print(passports)
