from collections import defaultdict

def first_uniq_char(s):
	mmap = defaultdict(int)

	for ss in s:
		mmap[ss] += 1

	for i,j in enumerate(s):
		mchr = mmap[j]
		if mchr < 2:
			return i

	return -1

print(first_uniq_char("leetcode"))
print(first_uniq_char("loveleetcode"))
print(first_uniq_char("aabb"))
