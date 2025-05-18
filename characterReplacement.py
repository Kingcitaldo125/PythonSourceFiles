# https://leetcode.com/problems/longest-repeating-character-replacement/

from collections import defaultdict

def characterReplacement(str, k):
	def get_max_counts(xlist):
		"""
		split the list into a contiguous collection
		of characters.
		Keep a running count of the longest string in the collection.
		"""
		max_ct = 0
		charset = set([])
		for x in xlist:
			charset.add(x)
		for ch in charset:
			ml = ''.join(xlist).split(ch)
			for m in ml:
				max_ct = max(max_ct, len(m))
		return max_ct

	# Figure out which character is the most 'common'
	# Go through the string and keep a tally of the
	# character occurrences
	# Use the least frequent character as the one that'll
	# be the first char that is subject to replacement
	mdict = defaultdict(int)

	for s in str:
		mdict[s] += 1

	# Figure out the most 'common' char
	max_letter = ''
	max_letter_count = 0
	for key,val in mdict.items():
		if val > max_letter_count:
			max_letter = key
			max_letter_count = val

	if max_letter == "":
		print("error max_letter == ''")
		return -1

	# Walk through a list of the characters 'k' times
	# Replace the characters that are not the most 'common'
	# and then total up the length of the collections of
	# contiguous characters.
	# The largest total for a single pass will then be used
	# to determine the value of 'xmax':
	# The largest total for the string after 'k' passes.
	k_ctr = 0
	xmax = 0
	strlist = [s for s in str]

	while(1):
		print(f"strlist {strlist}")
		xmax = get_max_counts(strlist)
		print(f"xmax: {xmax}")
		if k_ctr >= k:
			break
		lpos = 0
		for i,s in enumerate(strlist):
			if s != max_letter:
				lpos = i
				break
		strlist[lpos] = max_letter
		k_ctr += 1
	return xmax

print(characterReplacement("AABABBA", 1))
