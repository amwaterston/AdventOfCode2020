starting_numbers = [1,20,8,12,0,14]
numbers = {}

for i, n in enumerate(starting_numbers[:-1]):
    numbers[n] = i

n = starting_numbers[-1]

for i in range(len(starting_numbers) - 1, 30000000 - 1):
    last_instance_of_n = numbers.get(n, i)
    numbers[n] = i
    n = i - last_instance_of_n

print(n)