from itertools import combinations_with_replacement as c_w_r

def dxor(narr):
	if len(narr) == 0:
		return []

	for i in range(len(narr) - 1):
		narr[i] = narr[i] ^ narr[i + 1]

	narr[-1] = narr[-1] ^ narr[0]
	return narr

def nxor(narr):
	gcombo = lambda x: list(c_w_r(x,len(narr)))
	combos = [list(i) for i in set(gcombo([0,1,0]) + gcombo([1,0,1]))]
	for itm in combos:
		print("itm",itm)
		di = dxor(itm)
		print("di",di)
		if di == narr:
			return True
	return False

print(nxor([1,0]))
