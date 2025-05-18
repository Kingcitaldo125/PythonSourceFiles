from collections import defaultdict

'''
def contains_duplicate(nums):
	for i,j in enumerate(nums):
		for k,l in enumerate(nums):
			if j == l and i != k:
				return True

	return False
'''

def two_sum(nums, target):
	mmap = defaultdict(tuple)

	for i,j in enumerate(nums):
		xt = target - j
		mmap[xt] = (i, j)

	for i,j in enumerate(nums):
		if j in mmap:
			xitem = mmap[j]
			if xitem[1] + j == target and xitem[0] != i:
				return [i, xitem[0]]

	return []

print(two_sum([2,7,11,15], 9))
print(two_sum([3,2,4], 6))
print(two_sum([3,3], 6))
