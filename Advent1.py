inputstring = ""
with open("input1.txt") as fp:
	inputstring = fp.read()
	
#inputstring = "1,0,0,0,99"

rawinputs = list(map(int, inputstring.strip().split('\n')))
print(rawinputs)

length = len(rawinputs)

for a in range(0, length):
    for b in range(a, length):
        for c in range(b, length):
            if (rawinputs[a] + rawinputs[b] + rawinputs[c] == 2020):
                print (rawinputs[a] * rawinputs[b] * rawinputs[c])
