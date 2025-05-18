def permutations(mlist):
	def backtrack(xlist):
		if len(xlist) == 1:
			return [xlist.copy()]

		results = []

		for i in range(len(xlist)):
			itm = xlist.pop(0)
			sub_perms = backtrack([x for x in xlist])

			for sublist in sub_perms:
				sublist.append(itm)

			results.extend(sub_perms)

			xlist.append(itm)

		return results

	return backtrack(mlist)

print(permutations([1,2,3]))
