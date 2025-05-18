from sys import argv

def hamming(mint):
	x = 1
	set_bits = 0

	while 1:
		if x >= 4294967296:
			break

		#print(f"x: {x}")

		if mint & x != 0:
			set_bits += 1

		x = x << 1

	return set_bits

print(hamming(int(argv[1])))
