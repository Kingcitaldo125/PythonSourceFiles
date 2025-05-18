from collections import defaultdict

def climb(n):
	xdict = defaultdict(int)

	for i in range(4):
		xdict[i] = i

	def climb_help(n):
		if n <= 0:
			return 0

		if n in xdict:
			return xdict[n]

		n_val = climb(n-1) + climb(n-2)

		xdict[n] = n_val

		return xdict[n]

	return climb_help(n)

for i in [i for i in range(11)]:
	x = climb(i)
	print(i,x)
