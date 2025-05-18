class Node:
	def __init__(self,data):
		self.data = data
		self.next = None

def merge_sorted_lists(first, second):
	if not first or not second:
		return

	nlist = None
	nlist_head = None
	nlist_ptr = None

	first_ptr = first
	second_ptr = second

	while first_ptr and second_ptr:
		if first_ptr.data <= second_ptr.data:
			if not nlist:
				nlist = Node(first_ptr.data)
				nlist_head = nlist
				nlist_ptr = nlist
			else:
				nlist_ptr.next = Node(first_ptr.data)
				nlist_ptr = nlist_ptr.next

			first_ptr = first_ptr.next
		else:
			if not nlist:
				nlist = Node(second_ptr.data)
				nlist_head = nlist
				nlist_ptr = nlist
			else:
				nlist_ptr.next = Node(second_ptr.data)
				nlist_ptr = nlist_ptr.next

			second_ptr = second_ptr.next

	while first_ptr:
		if not nlist:
			nlist = Node(first_ptr.data)
			nlist_head = nlist
			nlist_ptr = nlist
		else:
			nlist_ptr.next = Node(first_ptr.data)
			nlist_ptr = nlist_ptr.next

		first_ptr = first_ptr.next

	while second_ptr:
		if not nlist:
			nlist = Node(second_ptr.data)
			nlist_head = nlist
			nlist_ptr = nlist
		else:
			nlist_ptr.next = Node(second_ptr.data)
			nlist_ptr = nlist_ptr.next

		second_ptr = second_ptr.next

	return nlist_head

def traverse(head):
	if not head:
		return

	hptr = head

	while hptr:
		print(hptr.data)
		hptr = hptr.next

	print()

list_one = Node(1)
list_one.next = Node(2)
list_one.next.next = Node(4)

list_two = Node(1)
list_two.next = Node(3)
list_two.next.next = Node(4)

hd = merge_sorted_lists(list_one, list_two)

traverse(hd)
