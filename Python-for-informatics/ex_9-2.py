file_name = raw_input("Enter file to anayse: ")

connect = open(file_name)

counts = dict()
for line in connect:
    line = line.strip()
    words = line.split()
    if len(words) == 0 or words[0] != "From" : continue
#    print words[2]
    day = words[2]
#    if day not in counts:
#        counts[day] = 1
#    else:
#        counts[day] += 1
#    counts.get(words[2], 1)
    counts[day] = counts.get(day, 0) + 1
    print day
print counts

