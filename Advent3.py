inputstring = ""
with open("input3.txt") as fp:
	inputstring = fp.read()

map = list(map(str, inputstring.strip().split('\n')))

def getAt(map, x, y):
    print (f"checking map {x}, {y}")
    if (y >= len(map)):
        return ' '
    m = map[y][x % len(map[y])]
    #print (m)
    return m

def traverse(map, xo, yo):
    t, x, y = 0, 0, 0
    #x = 0
    #y = 0
    while(getAt(map, x, y) != ' '):
        if (getAt(map, x, y) == '#'):
            t += 1
        x += xo
        y += yo

    return t

print(traverse(map, 1, 1) * traverse(map, 3, 1) * traverse(map, 5, 1) * traverse(map, 7, 1) * traverse(map, 1, 2))
