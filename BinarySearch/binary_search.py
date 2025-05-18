def binary_search(marray, val):
	low = 0
	high = len(marray)-1

	while low <= high:
		mid = (low + high) // 2

		item = marray[mid]

		if item == val:
			return True

		if low == 0 and high == 0:
			break

		if marray[mid] < val:
			low = mid+1
		else:
			high = mid

	return False

if __name__ == "__main__":
	print(binary_search([1,2,3,4,5,6], 0))
