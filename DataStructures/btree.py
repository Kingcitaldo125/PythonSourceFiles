class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def traversal_help(root,depth):
	if not root:
		return

	print("\t"*depth, "root val", root.val)
	print("\t"*depth, "left subtree")
	traversal_help(root.left,depth+1)
	print("\t"*depth, "end left subtree")
	print("\t"*depth, "right subtree")
	traversal_help(root.right,depth+1)
	print("\t"*depth, "end right subtree")

def traversal(root):
	traversal_help(root,1)

def flatten_help(root, xnodes):
	if not root:
		return

	xnodes.append(root)
	flatten_help(root.left, xnodes)
	flatten_help(root.right, xnodes)

def flatten(root):
	xnodes = []
	flatten_help(root, xnodes)
	head = None
	h = None

	for x in xnodes:
		if not head:
			head = TreeNode(x.val)
			h = head
			continue
		xnode = TreeNode(x.val)
		h.right = xnode
		h = h.right

	return head

tree = TreeNode(1)

tree.left = TreeNode(2)
tree.left.left = TreeNode(3)
tree.left.right = TreeNode(4)

tree.right = TreeNode(5)
tree.right.right = TreeNode(6)

tree = flatten(tree)
traversal(tree)
