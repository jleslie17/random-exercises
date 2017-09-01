file_name = raw_input("Enter a file name: ")

connect = open(file_name)

count = 0
for line in connect:
    line = line.strip()
    words = line.split()
    if len(words) == 0 or words[0] != "From" : continue
    print words[1]
    count += 1

print "There were %d lines with the word 'From' as the first word." % count
