from collections import defaultdict
from math import floor

def sock_merchant(ints):
	xdict = defaultdict(int)
	
	for i in ints:
		xdict[i] += 1
	
	count = 0
	for k,v in xdict.items():
		fres = floor(v//2)
		if fres >= 1:
			count += fres
	return count

print(sock_merchant([50, 20, 30, 90, 30, 20, 50, 20, 90]))
