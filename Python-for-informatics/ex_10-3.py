import string
file_name = raw_input("Enter a file: ")
connect = open(file_name)

letters = dict()
for line in connect:
	line = line.translate(None, string.punctuation)
	line = line.translate(None, string.digits)
	line = line.strip()
	line = line.lower()
	words = line.split()
	if len(words) == 0 : continue
	for word in words:
		word = list(word)
		for letter in word:
			letters[letter] = letters.get(letter, 0) + 1

for letter, count in letters.items():
	print letter, "\t", count
