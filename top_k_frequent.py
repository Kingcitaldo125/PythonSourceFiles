from collections import defaultdict

def top_k_frequent(items, k):
	xd = defaultdict(int)

	for i in items:
		xd[i]+=1

	xd = {v:k for k,v in xd.items()}

	retlist = []

	for i in range(k):
		key = max(xd)
		retlist.append(xd[key])
		del xd[key]

	return retlist

print(top_k_frequent([1,1,1,2,2,3], 2))
