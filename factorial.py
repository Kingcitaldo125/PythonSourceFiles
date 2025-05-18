from sys import argv

prods = {}

def fact(N):
	if N <= 1:
		return N

	if N in prods:
		return prods[N]

	x = N * fact(N-1)

	#prods[N] = x

	return x


if __name__ == "__main__":
	res = fact(int(argv[1]))
	print(res)
