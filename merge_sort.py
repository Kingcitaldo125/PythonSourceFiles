def merge(mlist1, mlist2):
	i = 0
	j = 0
	reslist = []

	while i < len(mlist1) and j < len(mlist2):
		i_itm = mlist1[i]
		j_itm = mlist2[j]

		if i_itm < j_itm:
			reslist.append(i_itm)
			i += 1
		else:
			reslist.append(j_itm)
			j += 1

	while i < len(mlist1):
		i_itm = mlist1[i]
		reslist.append(i_itm)
		i += 1

	while j < len(mlist2):
		j_itm = mlist2[j]
		reslist.append(j_itm)
		j += 1

	return reslist

def merge_sort(mlist):
	if len(mlist) <= 1:
		return mlist

	mid = len(mlist) // 2
	
	m1 = merge_sort(mlist[:mid])
	m2 = merge_sort(mlist[mid:])

	return merge(m1, m2)

print(merge_sort([4,1,7,2,5,9,3,6,8]))
