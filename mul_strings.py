import sys

i=sys.argv[1]
j=sys.argv[2]

total = 0
idx = 1
carry = 0
for ii in i[::-1]:
	row = 0
	cidx = idx

	for jj in j[::-1]:
		lprod = int(ii) * int(jj) + carry

		print(f"ii {ii} jj {jj}")
		print(f"lprod {lprod}")

		if lprod == 0:
			cidx *= 10
			continue

		carry = (lprod//10) if lprod > 9 else 0

		lprod = (lprod % 10) if carry else lprod

		print(f"carry {carry}")
		print(f"cidx {cidx}")

		row += lprod * cidx
		print(f"row {row}")

		cidx *= 10

	idx *= 10
	total += row
	print(f"total {total}")

if carry:
	print("Carry")
	total += carry * idx

print(f"total {total}")
