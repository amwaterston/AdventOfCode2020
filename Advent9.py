numbers = list(map(int, open('input9.txt').readlines()))

def isASum(sum, numbers):
	for i in range(0, len(numbers)):
		for j in range(i + 1, len(numbers)):
			if (numbers[i]) + numbers[j] == sum:
				return True
	return False
	
target = 0
for i in range(25, len(numbers)):
	if not isASum(numbers[i], numbers[i-25:i]):
		target = numbers[i]
		print(target)
		break;
		
s = 0
e = 2
while True:	
	window = sum(numbers[s:e])
	if (window == target):
		print (min(numbers[s:e]) + max(numbers[s:e]))
		break;
	elif (window < target):
		e += 1
	elif (window > target):
		s += 1
