inputstring = ""
with open("input2.txt") as fp:
	inputstring = fp.read()

rawinputs = list(map(str, inputstring.strip().split('\n')))

def stringToPolicyAndPassword(i):
    (policy, password) = i.split(':')
    return (policy.strip(), password.strip())

def policyToParts(policy):
    (rng, char) = policy.split(' ')
    (min, max) = rng.split('-')
    return (int(min), int(max), char)

def assessPassword(password, policy):
    (min, max, character) = policy
    return (password[min-1] == character or password[max-1] == character) and not (password[min-1] == character and password[max-1] == character)
    #return (min <= password.count(character) and max >= password.count(character))

truecnt = 0
for i in rawinputs:
    (policy, password) = stringToPolicyAndPassword(i)
    if (assessPassword(password, policyToParts(policy))):
        truecnt = truecnt + 1

print(truecnt)
    
