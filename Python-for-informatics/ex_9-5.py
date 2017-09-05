file_name = raw_input("Enter file name: ")

connect = open(file_name)
domains = dict()

for line in connect:
    line = line.strip()
    words = line.split()
    if len(words) == 0 or words[0] != "From" : continue
    address = words[1]
    domain = address.split("@")[1]


    domains[domain] = domains.get(domain, 0) + 1

print domains

for line in connect:
	