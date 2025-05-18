def max_sub_array(arr):
	max_sum = -1

	i = 0
	j = len(arr)

	flg = True

	while i < j:
		narr = arr[i:j]
		#print(f"narr {narr}")
		#ma_help = max_sub_array_help(narr)

		tmp = max_sum
		sumn = sum(narr)
		max_sum = max(max_sum, sumn)

		if tmp != max_sum:
			print(f"{narr} new sum {max_sum}")

		if flg:
			i += 1
			flg = False
			continue

		j -= 1
		flg = True

	return max_sum


if __name__ == "__main__":
	res = max_sub_array([-2,1,-3,4,-1,2,1,-5,4])
	print(f"res {res}")

	res = max_sub_array([1])
	print(f"res {res}")


	res = max_sub_array([5,4,-1,7,8])
	print(f"res {res}")
