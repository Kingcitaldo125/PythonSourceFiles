# https://www.linkedin.com/posts/simontoth_cpp-cplusplus-coding-activity-7097260677068713985-H3mu?utm_source=share&utm_medium=member_desktop

class Tree:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

def find_target(root, target, ctr):
	if not root:
		return -1
	if root.val == target.val:
		return ctr

	lft = find_target(root.left, target, ctr - 1)
	if lft != -1:
		return lft

	rght = find_target(root.right, target, ctr + 1)
	if rght != -1:
		return rght
	return -1

def traverse_help(root, nodes, target, target_ctr, k, ctr):
	if not root:
		return 0

	if root.val != target.val:
		if ctr == target_ctr or ctr == target_ctr-k or ctr == target_ctr+k:
			nodes.append(root.val)

	traverse_help(root.left, nodes, target, target_ctr, k, ctr - 1)
	traverse_help(root.right, nodes, target, target_ctr, k, ctr + 1)

def traverse(root, target, k):
	nodes = []
	target_ctr = find_target(root, target, 0)
	print(f"target_ctr {target_ctr}")
	traverse_help(root, nodes, target, target_ctr, k, 0)
	return nodes

root = Tree(1)

root.left = Tree(9)
root.right = Tree(3)

root.left.left = Tree(4)
root.left.right = Tree(5)

root.left.right.left = Tree(7)
root.left.right.right = Tree(2)

root.right.right = Tree(6)


nodes = traverse(root, root, 2)

print(f"nodes {nodes}")
