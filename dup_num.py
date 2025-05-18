def dup_num(x):
	xmin,xmax = min(x),max(x)
	xsplice = [i for i in range(xmin, xmax + 1)]
	lendiff = abs(len(xsplice) - len(x))

	return abs(sum(xsplice) - sum(x)) // lendiff

print(dup_num([1,2,2,3,4,2]))
print(dup_num([1,2,3,3,4]))
print(dup_num([1,2,3,4,4]))
