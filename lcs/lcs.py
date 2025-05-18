def lcs_help(str1, str2, mset):
	if len(str1) == 0 or len(str2) == 0 or len(mset) == 0:
		return 0

	x1 = ''.join([i for i in str1[1:] if i in mset])
	x2 = ''.join([i for i in str2[1:] if i in mset])

	nms = set(x1).intersection(set(x2))
	return 1 + lcs_help(x1, x2, nms)

def longest_common_substring(str1, str2):
	mset = set(str1).intersection(set(str2))
	return lcs_help(str1, str2, mset)

if __name__ == "__main__":
	import sys
	rv = longest_common_substring(sys.argv[1], sys.argv[2])
	print(rv)
