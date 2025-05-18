def merge(arr1, arr2):
	resarr = []
	i,j = (0,0)
	
	while i < len(arr1) and j < len(arr2):
		itm1 = arr1[i]
		itm2 = arr2[j]
		
		if itm1 < itm2:
			resarr.append(itm1)
			i += 1
		else:
			resarr.append(itm2)
			j += 1

	while i < len(arr1):
		itm = arr1[i]
		resarr.append(itm)
		i += 1

	while j < len(arr2):
		itm = arr2[j]
		resarr.append(itm)
		j += 1

	return resarr

def merge_sort(arr):
	mlen = len(arr)

	if mlen <= 1:
		return arr

	midpoint = mlen // 2

	return merge(merge_sort(arr[:midpoint]), merge_sort(arr[midpoint:]))

print(merge_sort([85, 26, 65, 95, 29, 52, 73, 68, 25]))
