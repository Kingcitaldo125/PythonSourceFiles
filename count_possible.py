import sys
from itertools import permutations as permutes

def count_possible(n):
	xlist = []
	for i in range(1,n+1):
		xlist.append('P'+str(i))
		xlist.append('D'+str(i))

	pmutes = permutes(xlist, len(xlist))
	pmutes_copy = []

	for perm in pmutes:
		found_p = False
		valid = True
		pset = set([])

		for itm in perm:
			if 'D' in itm and not found_p:
				valid = False
				break

			pint = int(itm[1:])
			if 'P' in itm:
				found_p = True
				pset.add(pint)
			elif 'D' in itm:
				if pint not in pset:
					valid = False
					break

		if valid:
			pmutes_copy.append(perm)

	return len(pmutes_copy)

if len(sys.argv) < 2:
	print("Enter in a number to compute")
	sys.exit(1)

print(count_possible(int(sys.argv[1])))

sys.exit(0)
