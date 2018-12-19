import random

map = [[]]
randomints = []
for t in range(random.randint(7,15)):
		randomints.append(random.randint(2,12))
print(randomints)

for i in range(0,30):
	print(i + (i + 1))
j = 1
for i in range(30,59):
	print(i+(i+1) - (4 * j))
	j += 1