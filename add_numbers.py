class Node():
	def __init__(self, n):
		self.payload = n
		self.next = None

def add_two_numbers(first, second):
	xlist1 = []
	xlist2 = []

	f = first
	s = second
	while f:
		xlist1.insert(0, f.payload)
		f = f.next

	while s:
		xlist2.insert(0, s.payload)
		s = s.next

	intify = lambda x: int(''.join([str(xx) for xx in x]))
	XYZ = intify(xlist1) + intify(xlist2)

	return [int(i) for i in str(XYZ)][::-1]

'''
flist = Node(9)
flist.next = Node(9)
flist.next.next = Node(9)
flist.next.next.next = Node(9)
flist.next.next.next.next = Node(9)
flist.next.next.next.next.next = Node(9)
flist.next.next.next.next.next.next = Node(9)

slist = Node(9)
slist.next = Node(9)
slist.next.next = Node(9)
slist.next.next.next = Node(9)
'''

flist = Node(0)

slist = Node(0)

res = add_two_numbers(flist, slist)

for r in res:
	print(r,end=' ')
print()
