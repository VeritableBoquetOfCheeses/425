favPizzas = ['wisconson six-cheese', 'meat lovers', 'alfredo chicken with bell pepper and bacon']

for pizza in favPizzas:
	print pizza

for index in range(len(favPizzas)):
	print favPizzas[index]

for index in range(1, 21):
	print index

nums = []
for index in range(0, 1000000):
	nums.append(index + 1)

nums = []
for index in range(0, 1000000):
	nums.append((index + 1) * 2)

print nums
