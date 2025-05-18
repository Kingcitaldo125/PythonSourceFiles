class Tree:
	def __init__(self, data):
		self.left = None
		self.right = None
		self.data = data
		self.depth = 0
		self.balance_factor = 0

	def __str__(self):
		return str(self.depth) + "," + str(self.data)

	def update_balance_factor(self, root, depth):
		if not root:
			return 0

		if not root.left and not root.right:
			return root.depth - depth

		lv = self.update_balance_factor(root.left, root.depth)
		rv = self.update_balance_factor(root.right, root.depth)

		xdepth = lv - rv
		root.balance_factor = xdepth

		return root.depth + lv + rv

	def add_help(self, root, itm, depth):
		if not root:
			root.data = itm
			return

		if itm < root.data:
			if not root.left:
				root.left = Tree(itm)
				root.left.depth = depth + 1
				return
			self.add_help(root.left, itm, depth + 1)
		else:
			if not root.right:
				root.right = Tree(itm)
				root.right.depth = depth + 1
				return
			self.add_help(root.right, itm, depth + 1)

	def add(self, root, itm):
		self.add_help(root, itm, 0)
		self.update_balance_factor(root, 0)

	def in_traverse(self, root):
		if not root:
			return

		self.in_traverse(root.left)
		print(root.depth, root.balance_factor, root.data)
		self.in_traverse(root.right)

tree = Tree(5)

tree.add(tree, 4)
tree.add(tree, 3)

tree.in_traverse(tree)
