def find_min(mlist):
	low = 0
	high = len(mlist)-1

	mid = (low + high) // 2
	while low <= high:
		mid = (low + high) // 2
		if mlist[low] < mlist[high]:
			high = mid
			continue
		low = mid + 1
	return mlist[mid]

print(find_min([11,13,15,17]))
