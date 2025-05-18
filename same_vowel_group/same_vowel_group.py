def same_vowel_group(mlist):
	mvowels = set(['a', 'e', 'i', 'o', 'u'])
	mset = set([i for i in mlist[0] if i in mvowels])
	retlist = []

	for idx in range(1,len(mlist)):
		itm = mlist[idx]
		vowel_count = 0

		for i in set([i for i in itm]):
			if i in mvowels:
				if i in mset:
					vowel_count += 1
				else:
					vowel_count -= 1

		if vowel_count == len(mset):
			retlist.append(itm)

	return [mlist[0]] + retlist
