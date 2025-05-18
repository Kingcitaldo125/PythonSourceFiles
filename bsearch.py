import sys

def bsearch(itms, mint):
	low = 0
	high = len(itms) - 1
	
	while low <= high:
		mid = (low + high) // 2
		#print(f"mid: {mid}")

		if itms[mid] == mint:
			return True
		if itms[mid] < mint:
			low = mid + 1
			continue
		high = mid

	return False

print(bsearch([1,2,3,4,5,6,7,8,9,], int(sys.argv[1])))
