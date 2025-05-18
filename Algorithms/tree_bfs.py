class TreeNode:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

def bfs(root, target):
	mqueue = [root]
	
	layer = 1

	while len(mqueue) > 0:
		itm = mqueue.pop()

		print(f"layer = {layer}")

		if itm.data == target:
			return True
			
		alayer = False
		if itm.left:
			mqueue.insert(0, itm.left)
			layer += 1
			alayer = True

		if itm.right:
			mqueue.insert(0, itm.right)
			if not alayer:
				layer += 1

	return False

root = TreeNode(4)

root.left = TreeNode(2)
root.right = TreeNode(6)

root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

root.left.right.right = TreeNode(5)

root.right.right = TreeNode(15)
root.right.left = TreeNode(10)

res = bfs(root, 5)

print("Found:", res)
