class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

def int_lists(list_one, list_two):
	h_one = list_one
	h_two = list_two

	if not h_one or not h_two:
		return None

	x_one = 0
	x_two = 0

	while x_one <= x_two:
		if h_one == h_two:
			return h_one

		if not h_one:
			h_one = list_one
			x_one = 0

		if not h_two:
			h_two = list_two
			x_two = 0

		h_one = h_one.next
		x_one += 1

		if h_one == h_two:
			return h_one

		h_two = h_two.next
		x_two += 1

		if h_one == h_two:
			return h_one

		if not h_two:
			h_two = list_two
			x_two = 0

		h_two = h_two.next
		x_two += 1

	return None

int_node = Node(2)

mlist = Node(3)
mlist.next = Node(1)
mlist.next.next = int_node
mlist.next.next.next = Node(4)

mlist_two = Node(5)
mlist_two.next = Node(6)
mlist_two.next.next = Node(7)
mlist_two.next.next.next = int_node
mlist_two.next.next.next.next = Node(9)

res = int_lists(mlist, mlist_two)

if res:
	print(res, res.data)
