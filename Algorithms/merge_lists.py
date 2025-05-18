class Node():
	def __init__(self, data):
		self.data = data
		self.next = None

class List():
	def __init__(self):
		self.head = None

	def add(self, itm):
		if not self.head:
			self.head = Node(itm)
			return self.head
		
		nnode = Node(itm)
		nnode.next = self.head
		self.head = nnode
		return self.head

	def reverse(self):
		h = self.head
		prev = None

		if not h:
			return

		while h.next:
			tmp = h.next
			h.next = prev

			prev = h
			h = tmp

		h.next = prev
		self.head = h

	def traverse(self):
		h = self.head

		while(h):
			print(h.data)
			h = h.next


def merge(listone, listtwo):
	h1 = listone.head
	h2 = listtwo.head

	nlist = List()

	while h1 and h2:
		if h1.data <= h2.data:
			nlist.add(h1.data)
			h1 = h1.next
			continue
		nlist.add(h2.data)
		h2 = h2.next

	while h1:
		nlist.add(h1.data)
		h1 = h1.next

	while h2:
		nlist.add(h2.data)
		h2 = h2.next

	nlist.reverse()
	return nlist


m1 = List()
m2 = List()

#'''
m1.add(4)
m1.add(3)
m1.add(1)

m2.add(5)
m2.add(2)
#'''

nlist = merge(m1, m2)
nlist.traverse()
