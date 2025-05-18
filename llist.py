class Node:
	def __init__(self,d):
		self.data = d
		self.next = None


def reverse_lr(head, left, right):
	h = head
	got_left = False
	got_right = False

	if not h:
		return

	xlist = []

	while 1:
		if not h:
			break
		if h == left:
			got_left = True
		if h == right:
			got_right = True
			xlist.append(h.data)
			break

		if got_left and not got_right:
			xlist.append(h.data)

		h = h.next

	xlist = xlist[::-1]

	h = head
	prev = None
	got_left = False
	got_right = False
	idx = 0

	while 1:
		if not h:
			break
		if h == left:
			got_left = True
		if h == right:
			got_right = True
			tmp = h.next
			print(f"replacing {h.data} with {xlist[idx]}")
			h = Node(xlist[idx])
			h.next = tmp
			if prev:
				prev.next = h
			print("h.data", h.data)
			print("h.next.data", h.next.data)
			break

		if got_left and not got_right:
			tmp = h.next
			print(f"replacing {h.data} with {xlist[idx]}")
			h = Node(xlist[idx])
			h.next = tmp
			if prev:
				prev.next = h
			print("h.data", h.data)
			print("h.next.data", h.next.data)
			idx += 1

		prev = h
		h = h.next

	return head

def traverse(root):
	h = root

	while h:
		print(h.data)
		h = h.next
	print()

root = Node(1)
root.next = Node(2)
root.next.next = Node(3)
root.next.next.next = Node(4)
root.next.next.next.next = Node(5)

traverse(root)

nroot = reverse_lr(root, root.next, root.next.next.next)

traverse(nroot)
