file_name = raw_input("Enter file name: ")

connect = open(file_name)
addresses = dict()

for line in connect:
	line = line.strip()
	words = line.split()
	if len(words) == 0 or words[0] != "From" : continue
	addresses[words[1]] = addresses.get(words[1], 0) + 1

counts = []
for address, count in addresses.items():
	counts.append( (count, address))

counts.sort(reverse = True)
for i in range(len(counts)):
	count, address = counts[i]
	counts[i] = (address, count)

print counts[0][0], counts[0][1]