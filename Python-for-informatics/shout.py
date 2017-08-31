file = raw_input("Enter a filename: ")

try:
    fin = open(file)
except:
    print "File cannot be opened."
    exit()

for line in fin:
    print line.upper()
