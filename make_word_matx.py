from random import randrange
from sys import argv

make_word = lambda x: "".join([chr(randrange(ord('A'), ord('Z') + 1)) for i in range(x)])

def make_word_matx(size):
	matxx = []
	for i in range(size):
		matxx.append(make_word(size))
	return matxx

with open("out.txt", "w") as f:
	for i in make_word_matx(int(argv[1])):
		f.write(f"\t\t\"{i}\",")
		f.write("\n")
	f.flush()
