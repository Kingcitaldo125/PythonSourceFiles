def subsets(nums):
	def ss(xlist):
		if len(xlist) < 1:
			return xlist

		retlist = []
		for i in xlist:
			nxlist = [itm for itm in xlist if itm != i]
			res_xlist = ss(nxlist)
			retlist.extend(res_xlist)
		retlist.append(xlist)

		return retlist

	return [[]]+ss(nums)

print(subsets([0]))
