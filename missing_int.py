xlist = [3, 8, 2, 7, 4, 5]

min_el = min(xlist)
max_el = max(xlist)

total = sum(xlist)

for i in [j for j in range(min_el, max_el + 1)]:
	total -= i

atot = abs(total)
print(atot if atot != 0 else max_el + 1)
