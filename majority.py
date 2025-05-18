from collections import defaultdict

def majority(arr):
	mmap = defaultdict(int)

	for i in arr:
		mmap[i] += 1

	majel = -1
	majority_elem = -1
	for i in arr:
		if mmap[i] > majel:
			majel = mmap[i]
			majority_elem = i

	return majority_elem

if __name__ == "__main__":
	print(majority([2,2,1,1,1,2,2]))
