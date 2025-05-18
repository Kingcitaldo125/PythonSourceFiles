from random import randrange as rr

import heapq

k = 3

xmatx = [sorted([rr(1,100) for i in range(1,rr(5,10))]) for j in range(k)]

def merge_k_lists(lists, k):
	merges = []

	for row in lists:
		for r in row:
			heapq.heappush(merges,r)

	xmerges = []

	while merges:
		xmerges.append(heapq.heappop(merges))

	return xmerges

for x in xmatx:
	print(x)

print(merge_k_lists(xmatx, k))
