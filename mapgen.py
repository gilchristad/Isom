import random

map = []
randomints = []
randomoffset = []

#Generate random number of tiles: the length of the array is how many rows, each number in each index is the number of tiles for that row
for t in range(random.randint(15,25)):
 		randomints.append(random.randint(7,20))
 		randomoffset.append(random.randint(1,5))

print(randomints)
print(len(randomints))
print(randomoffset)


def map_gen():
	f = open("map.txt", "w")
	t = 0
	for i in range(0,30):
		flag = 0
		row = []
		length = i + (i + 1)
		for x in range(0,length):
			if x == 0 or x == (length - 1):
				row.append("/")
			elif i >= (30 - (len(randomints)/2)) and t < len(randomints):
				if x <= (round(length-1)/2) - (round(randomints[t]/2) - 1) - randomoffset[t]:
					row.append("*")
				elif x >= (round(length-1)/2) + round(randomints[t]/2):
					row.append("*")
				else:
					row.append("&")
					flag = 1
			else:
				row.append("*")
		if flag == 1:
			t += 1
			
		map.append(row)

	j = 1
	for i in range(30,59):
		row = []
		length = (i+(i+1) - (4 * j))
		j += 1
		for x in range(0,length):
			if x == 0 or x == (length - 1):
				row.append("/")
			elif i <= (31 + (round(len(randomints)/2) -2)) and t < len(randomints):
				if x <= (round(length-1)/2) - (round(randomints[t]/2) -1)  - randomoffset[t]:
					row.append("*")
				elif x >= (round(length-1)/2) + round(randomints[t]/2) + randomoffset[t]/2:
					row.append("*")
				else:
					row.append("&")
					flag = 1
			else:
				row.append("*")
		if flag == 1:
			t += 1
		map.append(row)
	f.write(str(map))
	
	return map