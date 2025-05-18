from random import randrange as rr

def merge(first, second):
	i=0
	j=0

	resarr=[]

	while i < len(first) and j < len(second):
		f = first[i]
		s = second[j]

		if f < s:
			resarr.append(f)
			i += 1
		else:
			resarr.append(s)
			j += 1

	while i < len(first):
		resarr.append(first[i])
		i += 1

	while j < len(second):
		resarr.append(second[j])
		j += 1

	return resarr

def merge_sort(marr):
	def m_help(m):
		mlen = len(m)

		if mlen == 1:
			return m

		idx = len(m)//2

		return merge(m_help(m[0:idx]), m_help(m[idx:len(m)]))

	return m_help(marr)

xarr = [rr(1,100) for i in range(20)]

print(xarr)

xarr = merge_sort(xarr)

print(xarr)
