import random

map = []
randomints = []

#Generate random number of tiles: the length of the array is how many rows, each number in each index is the number of tiles for that row
for t in range(random.randint(7,15)):
 		randomints.append(random.randint(2,12))
print(randomints)
print(len(randomints))

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
			if x <= (round(length-1)/2) - round(randomints[t]/2) - 1:
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
	f.write(str(row) + "\n")

j = 1
for i in range(30,59):
	row = []
	length = (i+(i+1) - (4 * j))
	j += 1
	for x in range(0,length):
		if x == 0 or x == (length - 1):
			row.append("/")
		elif i <= (31 + (round(len(randomints)/2) -2)) and t < len(randomints):
			if x <= (round(length-1)/2) - round(randomints[t]/2) -1:
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
	f.write(str(row) + "\n")
