from random import shuffle

def ip_shuffle(ml):
	shuffle(ml)
	return ml

def pancake_sort(mlist):
	end_idx = len(mlist)

	while 1:
		if end_idx <= 0:
			break

		max_idx = mlist.index(max(mlist[:end_idx]))
		max_idx = max_idx + 1

		mlist[:max_idx] = mlist[:max_idx][::-1]

		mlist[:end_idx] = mlist[:end_idx][::-1]

		end_idx -= 1

def main(ml=ip_shuffle([i for i in range(1,10)])):
	print("before", ml)
	pancake_sort(ml)
	print("after", ml)

main()
