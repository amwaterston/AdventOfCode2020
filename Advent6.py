print(sum(map(lambda x: len(set(x.replace("\n", ""))), open("input6.txt").read().split('\n\n'))))
print(sum(map(lambda x: len(set.intersection(*list(map(lambda y: set(y), x.split('\n'))))), open("input6.txt").read().split('\n\n'))))

