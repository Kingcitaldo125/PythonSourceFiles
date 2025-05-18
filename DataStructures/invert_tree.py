class Tree:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

	def add(self, root, data):
		if not root:
			return

		if data < root.data:
			if not root.left:
				root.left = Tree(data)
				return
			self.add(root.left, data)
		else:
			if not root.right:
				root.right = Tree(data)
				return
			self.add(root.right, data)

	def traverse(self, root):
		if not root:
			return

		self.traverse(root.left)
		print(root.data)
		self.traverse(root.right)

	def invert(self, root):
		if not root:
			return

		tmp = root.left
		root.left = root.right
		root.right = tmp

		self.invert(root.left)
		self.invert(root.right)

	def dfs(self, root):
		if not root:
			return 0

		mdepth = 1

		def dfs_help(root, md=1):
			nonlocal mdepth

			if root.left:
				dfs_help(root.left, md + 1)

			if root.right:
				dfs_help(root.right, md + 1)

			mdepth = max(mdepth, md)

		dfs_help(root)

		return mdepth

t = Tree(3) # 1

t.left = Tree(9)
t.right = Tree(20) # 2

t.right.left = Tree(15)
t.right.right = Tree(7) # 3

'''
t.right.left.left = Tree(12) # 4

t.right.left.left.left = Tree(8) # 5
'''

print(t.dfs(t))
