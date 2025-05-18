class Tree:
	def __init__(self, data):
		self.left = None
		self.right = None
		self.data = data

	def sum_range(self, root, low, high):
		rootval = 0

		if not root:
			return rootval

		if root.data >= low and root.data <= high:
			rootval = root.data

		lval = self.sum_range(root.left, low, high)
		rval = self.sum_range(root.right, low, high)

		return rootval + lval + rval

tree = Tree(10)

tree.left = Tree(5)
tree.left.left = Tree(3)
tree.left.left.left = Tree(1)
tree.left.right = Tree(7)
tree.left.right.left = Tree(6)

tree.right = Tree(15)
tree.right.left = Tree(13)
tree.right.right = Tree(18)

xsum = tree.sum_range(tree, 6, 10)

print(f'xsum {xsum}')
