def num_in_str(mstrs):
	xn = []

	for str in mstrs:
		for m in str:
			if m >= "0" and m <= "9":
				xn.append(str)
				break

	return xn

print(num_in_str(["1a", "a", "2b", "b"]))
