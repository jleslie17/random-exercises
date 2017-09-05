file_name = raw_input("Enter file name: ")

connect = open(file_name)
hours = dict()

for line in connect:
	line = line.strip()
	words = line.split()
	if len(words) == 0 or words[0] != "From" : continue
	time = words[5]
	time = time.split(":")[0]
	hours[time] = hours.get(time, 0) + 1

counts = []
for hour, count in hours.items():
	counts.append( (hour, count) )

counts.sort()
for i in range(len(counts)):
	print counts[i][0], "\t", counts[i][1]
