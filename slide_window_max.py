def max_slide_window(mlist, k):
	xmaxl = []
	ik = 0
	while 1:
		if ik >= len(mlist)-(k-1):
			break
		xmaxl.append(max(mlist[ik:ik+k]))
		ik+=1
	return xmaxl

res = max_slide_window([1,3,-1,-3,5,3,6,7], 3)
#res = max_slide_window([1], 1)

print(f"res {res}")
