def length_list(nums):
	lens = len(nums)
	if lens <= 1:
		return lens

	if lens == 2:
		first = nums[0]
		second = nums[1]
		xls = []
		
		if first < second:
			xls.append(first)
			xls.append(second)
		else:
			xls.append(second)
			xls.append(first)

		if xls == nums and first != second:
			return 2
		return 0

	midsection = lens//2
	first = nums[:midsection]
	second = nums[midsection:]

	return length_list(first) + length_list(second)

print(length_list([10,9,2,5,3,7,101,18]))
