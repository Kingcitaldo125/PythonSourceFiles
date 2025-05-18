class Tree:
	def __init__(self, info):
		self.info = info
		self.left = None
		self.right = None

def add(root, data):
	prev = None
	head = root

	if not head:
		r = Tree(data)
		r.left = None
		r.right = None
		return r

	while head != None:
		if data <= head.info:
			print(f'{data} less than {head.info}')

			new_node = Tree(data)
			new_node.left = prev
			
			if prev:
				prev.right = new_node

			new_node.right = head
			head.left = new_node

			break

		prev = head
		head = head.right

	return root

def print_tree(root):
	r = root
	
	while r:
		if r.left:
			print(f'LEFT {r.left.info}')

		print(f'DATA {r.info}')

		if r.right:
			print(f'RIGHT {r.right.info}')

		print()

		r = r.right
