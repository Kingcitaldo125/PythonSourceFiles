from itertools import permutations as perm
from random import randrange

def add(itm_str):
	x = int(itm_str) + 1
	if x > 9:
		x = 0
	return str(x)

def sub(itm_str):
	x = int(itm_str) - 1
	if x < 0:
		x = 9
	return str(x)

def gen_moves(itm):
	itm_list = [i for i in itm]
	minitm = min(itm_list)
	maxitm = max(itm_list)

	idx1 = randrange(0, len(itm_list))
	idx2 = randrange(0, len(itm_list))

	while idx2 == idx1:
		idx2 = randrange(0, len(itm_list))

	combo_seeds = set([])

	itm_list_copy = itm_list[:]

	itm_list[idx1] = add(maxitm)
	combo_seeds.add(''.join(itm_list))

	itm_list_copy[idx2] = sub(minitm)
	combo_seeds.add(''.join(itm_list_copy))

	itm_list[idx2] = sub(minitm)
	combo_seeds.add(''.join(itm_list))

	xset = set([])
	for c in combo_seeds:
		for p in set(perm(c, 4)):
			xset.add(''.join(p))

	return xset


def bfs(start, target, deadends):
	ml = [start]
	count = 0

	while len(ml) > 0:
		front = ml.pop(0)

		deadends.add(front)

		if front == target:
			return count

		count += 1

		for i in gen_moves(front):
			if target == i:
				return count

			if i in deadends:
				continue

			ml.append(i)

	return -1

start = "0000"
target = "8888"

results = []

for i in range(40):
	deadends = set(["8887","8889","8878","8898","8788","8988","7888","9888"])
	results.append(bfs(start, target, deadends))

print(min(results))

#print(gen_moves("0000"))
