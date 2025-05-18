from itertools import combinations_with_replacement as cwr

def coin_change_two(amount, coins):
	total_combos = []
	
	for i in range(amount + 1):
		for item in list(cwr(coins, i)):
			total_combos.append(item)
	
	sum_filter = lambda x: sum(x) == amount
	total_combos = list(filter(sum_filter, total_combos))

	print(f"total_combos: {total_combos}")

	return len(total_combos)

res = coin_change_two(4, [1,2,3])
print(f"{res} combinations.")
