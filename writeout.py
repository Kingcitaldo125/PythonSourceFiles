from random import choice
from sys import argv

strings = []

size = int(argv[1])

for i in range(size):
	gens = str([choice([0, 1]) for i in range(size)])
	strings.append('{' + gens[1:len(gens)-1] + '}')

with open('outfile.txt', 'w') as f:
	f.write("\tstd::vector<std::vector<int>> grid {\n")
	for s in strings:
		f.write("\t\t" + s + ",")
		f.write("\n")
	f.write("\t};")

	f.flush()
