file_name = raw_input("Enter file name: ")

connect = open(file_name)

addresses = dict()

for line in connect:
    line = line.strip()
    words = line.split()
    if len(words) == 0 or words[0] != "From" : continue
    address = words[1]
    addresses[address] = addresses.get(address, 0) + 1

print addresses
