def ransom(ransom_note, magazine):
	xm = {}

	for m in magazine:
		xm[m] = 0

	for m in magazine:
		xm[m] += 1

	for r in ransom_note:
		if r not in xm:
			return False
		if xm[r] <= 0:
			return False

		xm[r] -= 1

	return True

print(ransom("aa", "ab"))
