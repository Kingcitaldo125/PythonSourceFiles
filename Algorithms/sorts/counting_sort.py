def counting_sort(arr):
	holder = [0 for i in range(max(arr) + 1)]
	output = [0 for i in range(len(arr))]

	for i in arr:
		holder[i-1] += 1

	for i in range(1,len(arr)):
		holder[i] = holder[i] + holder[i-1]

	for i in arr:
		holder[i-1] -= 1
		output[holder[i-1]] = i

	return output

marr = [1,5,4,2,3,6,4]

print(counting_sort(marr))
