def findMedianSortedArrays(nums1, nums2):
	n1_size = len(nums1)
	n2_size = len(nums2)

	if n1_size <= 1 and n2_size <= 1:
		return (sum(nums1)+sum(nums2))/(n1_size+n2_size)

	half_n1 = n1_size//2
	half_n2 = n2_size//2

	f1 = findMedianSortedArrays(nums1[1:half_n1], nums2[1:half_n2])
	f2 = findMedianSortedArrays(nums1[half_n1:], nums2[half_n2:])

	return (f1 + f2) / 2

print(findMedianSortedArrays([1,3], [2]))
print(findMedianSortedArrays([1,2], [3,4]))
