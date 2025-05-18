# https://leetcode.com/problems/container-with-most-water/
def calc_area(xlist, first, last):
	val = (last-first) * min(xlist[last], xlist[first])
	return val

def max_area_help(xlist, toggle=False):
	marea = 0
	first = 0
	last = len(xlist) - 1

	while first < last:
		marea = max(calc_area(xlist, first, last), marea)

		if toggle:
			first += 1
			toggle = False
		else:
			last -= 1
			toggle = True

	return marea

def max_area(xlist):
	marea = max(
		max_area_help(xlist),
		max_area_help(xlist,toggle=True),
	)
	return marea

print(max_area([1,8,6,2,5,4,8,3,7]))
#print(max_area([2,7,5]))
