from itertools import permutations as perm
from sys import argv

def check_distance(sequence):
	for seq in sequence:
		if seq < 2:
			continue

		fidx = sequence.index(seq)
		sidx = sequence.index(seq,fidx + 1)

		if abs(sidx - fidx) != seq:
			return False

	return True

def lex_larger(n, seq1, seq2):
	if len(seq1) != len(seq2):
		return [-1 for i in range(n)]

	for i in range(len(seq1)):
		if seq1[i] == seq2[i]:
			continue

		if seq1[i] > seq2[i]:
			return seq1
		elif seq2[i] > seq1[i]:
			return seq2

	return seq2

def main(n):
	duplist = []

	for i in range(2,n + 1):
		for j in range(2):
			duplist.append(i)

	baselist = [1] + duplist
	perms = list(perm(baselist,len(baselist)))
	largest = [-1 for i in range(len(baselist))]

	for p in perms:
		if not check_distance(p):
			continue

		#print("perm",p)
		largest = lex_larger(n, largest, p)
		#print("largest",largest)
		#print("")

	return largest

#print(check_distance([3,1,2,3,2]))

print(main(int(argv[1])))
