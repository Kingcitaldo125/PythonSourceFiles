class Node:
	def __init__(self, data = 0):
		self.data = data
		self.left = None
		self.right = None

def c_leaves(root):
	if not root:
		return 0
	if not root.left and not root.right:
		return 1
	return c_leaves(root.left) + c_leaves(root.right)

head = Node(8)

head.left = Node(3)
head.left.left = Node(1)
head.left.right = Node(5)
head.left.right.left = Node(6)

head.right = Node(9)
head.right.left = Node(6)
head.right.left.left = Node(5)
head.right.left.right = Node(7)
head.right.right = Node(15)
head.right.right.right = Node(28)

x = c_leaves(head)

print(f'{x} leaves')
