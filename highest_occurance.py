from collections import defaultdict

def highest_occurance(mlist):
	md = defaultdict(int)
	for m in mlist:
		md[m] += 1

	max_in = 0
	max_val = None
	for k,v in md.items():
		if v > max_in:
			max_in = v
			max_val = k

	return max_val

print(highest_occurance(["it", "keeps", "coding", "on", "or", "it", "gets", "the", "hose"]))
