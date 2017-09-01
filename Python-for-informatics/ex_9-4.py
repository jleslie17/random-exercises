file_name = raw_input("Enter file name: ")

connect = open(file_name)

addresses = dict()

for line in connect:
    line = line.strip()
    words = line.split()
    if len(words) == 0 or words[0] != "From" : continue
    address = words[1]
    addresses[address] = addresses.get(address, 0) + 1

top_value = 0
top_key = None
for key, value in addresses.items():
    if value > top_value:
        top_value = value
        top_key = key

print top_key, ":\t", top_value
