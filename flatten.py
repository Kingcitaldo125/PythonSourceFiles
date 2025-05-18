def flatten_help(arr, n):
	if n <= 0:
		return arr

	xl = []
	for a in arr:
		if type(a) == list:
			ftn = flatten_help(a, n-1)
			if type(ftn) == list:
				xl.append(ftn)
				continue
			for f in ftn:
				xl.append(f)
		else:
			xl.append(a)

	return (x for x in xl)

def flatten(arr, n):
	if n <= 0:
		return arr
	return [i for i in flatten_help(arr, n+1)]

print(flatten([1, 2, 3, [4, 5, 6], [7, 8, [9, 10, 11], 12], [13, 14, 15]], 1))
