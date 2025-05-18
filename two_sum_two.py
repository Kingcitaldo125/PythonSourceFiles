def two_sum_two(mlist, target):
	idx = len(mlist)-1

	if idx < 0:
		return [-1,-1]

	ctar = target
	indices = []
	while idx >= 0:
		if mlist[idx] > ctar:
			idx -= 1
			continue
		indices.insert(0,idx)
		ctar -= mlist[idx]
		idx -= 1

	if len(indices) == 1:
		cidx = 0
		for i in mlist:
			if i == 0:
				indices.append(cidx)
				break
			cidx += 1

	return [i+1 for i in indices]

print(two_sum_two([2,7,11,15], 9))
#print(two_sum_two([2,3,4], 6))
#print(two_sum_two([-1,0], -1))
