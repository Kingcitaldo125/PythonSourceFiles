from itertools import combinations_with_replacement as c_w_r

def missing_rolls(rolls, mean, n):
	faces = [1,2,3,4,5,6]

	sorted_rolls = str(sorted(rolls)).replace('[','').replace(']','')
	roll_count = len(rolls)
	total_count = roll_count + n
	match_lambda = lambda x: sum(x)/total_count == mean

	candidates = list(c_w_r(rolls + faces, total_count))
	lf_rolls = [sorted(i) for i in list(filter(match_lambda, candidates))]
	#print(f"lf_rolls {lf_rolls}")
	#print(f"sorted_rolls {sorted_rolls}")

	for itm in lf_rolls:
		if sorted_rolls in str(itm):
			for i in rolls:
				itm.remove(i)

			return itm

	return []

#print(missing_rolls([3,2,4,3], 4, 2))
print(missing_rolls([1,5,6], 3, 4))
