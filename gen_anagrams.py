import random

def gen_anagrams(mstr, k):
	mlist = []

	for i in range(k):
		xl = [m for m in mstr]
		random.shuffle(xl)
		mlist.append("".join(xl))

	return mlist

print(gen_anagrams("first", 10))
