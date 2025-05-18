from itertools import combinations as combos

def filter_tuple_groups(t_groups):
	xlist = []

	for tg in t_groups:
		tset = set([])
		do_include = True
		for t in tg:
			t1,t2 = t[0],t[1]
			if t1 in tset or t2 in tset:
				do_include = False
				break

			tset.add(t1)
			tset.add(t2)

		if do_include:
			xlist.append(tg)

	return xlist

def get_and_sum(g_tuple):
	gsum = 0

	for i,g in enumerate(g_tuple):
		g1,g2 = g[0],g[1]
		gsum += (g1 & (i+1))
		gsum += (g2 & (i+1))

	return gsum

combo_pairs=list(combos([1,2,3,4,5,6], 2))

max_sum = 0

tup_groups = filter_tuple_groups(list(combos(combo_pairs,3)))

for p in tup_groups:
	gas = get_and_sum(p)
	print(p,gas)
	max_sum = max(max_sum, gas)

print(f"max_sum {max_sum}")
