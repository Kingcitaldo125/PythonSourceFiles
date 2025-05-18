class Node():
	def __init__(self, n):
		self.payload = n
		self.next = None

def has_cycle(head):
	t_prev = -1

	tort = head
	hare = head

	while 1:
		if not tort or not hare:
			break

		if not tort.next or not hare.next.next:
			break

		tort = tort.next
		hare = hare.next.next

		if tort == hare:
			print(f't_prev {t_prev}')
			return True

		t_prev += 1

	print(f't_prev {t_prev}')
	return False

def main():
	nnode = Node(3)
	#nnode.next = Node(2)
	#nnode.next.next = Node(0)
	#nnode.next.next.next = Node(-4)
	#nnode.next.next.next.next = nnode.next

	print(has_cycle(nnode))

if __name__ == "__main__":
	main()
