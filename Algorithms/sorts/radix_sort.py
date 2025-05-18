import time

def radix_sort(arr):
	digits = {i:[] for i in range(0,10)}
	digit_offset = 0

	while 1:
		did_insert = False

		for i in arr:
			istr = str(i)
			t_idx = len(istr) - digit_offset - 1

			if t_idx < 0:
				digits[0].append(i)
				continue

			did_insert = True
			ldigit = istr[t_idx]
			digits[int(ldigit)].append(i)

		if not did_insert:
			return arr

		arr = []
		for i in range(0,10):
			subarr = digits[i]
			for s in subarr:
				arr.append(s)

		digits = {i:[] for i in range(0,10)}
		digit_offset += 1

marr = []

with open('out.txt') as f:
	marr = f.readlines()

marr = [int(i.split('\n')[0]) for i in marr]

before = time.time()
marr = radix_sort(marr)
now = time.time()

print(f"Took {now-before} seconds")
