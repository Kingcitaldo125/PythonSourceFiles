def search_rot_arr(marr, target):	
	def hlp(marr, target, start, end):
		mlen = len(marr)

		if mlen <= 0:
			return -1

		if mlen == 1:
			if target == marr[0]:
				return end
			return -1

		half = (start + end)//2
		f_res = hlp(marr[0:mlen//2], target, start, half - 1)
		s_res = hlp(marr[mlen//2:mlen], target, half + 1, end)

		return f_res & s_res

	return hlp(marr, target, 0, len(marr) - 1)

#       0 1 2 3 4 5 6
xarr = [4,5,6,7,0,1,2]

#res = search_rot_arr(xarr, 4)
#res = search_rot_arr(xarr, 1)
res = search_rot_arr([1], 0)

print(f'res {res}')
