def h_index(mlist):
	htotal = 0
	itm = 1

	for m in mlist:
		if m >= itm:
			htotal += 1
		itm += 1
	return htotal

res = h_index([25, 8, 5, 3, 3])
print(f"h_index = {res}")

res = h_index([10, 8, 5, 4, 3])
print(f"h_index = {res}")
