class Node:
	def __init__(self, val, neighbors):
		self.val = val
		self.neighbors = neighbors

def clone_graph_help(node, visited):
	head = Node(val=node.val, neighbors=None)
	head.neighbors = [Node(i.val,i.neighbors) for i in node.neighbors]

	visited.add(node.val)

	for neigh in node.neighbors:
		if neigh.val not in visited:
			clone_graph_help(neigh, visited)

	return head

def clone_graph(node):
	visited = set()
	return clone_graph_help(node, visited)

def traverse_help(node, visited):
	print(f"Visited {node.val}")

	visited.add(node.val)

	for n in node.neighbors:
		if n.val not in visited:
			traverse_help(n, visited)

def traverse(node):
	visited = set()
	traverse_help(node, visited)

third = Node(3, [])
second = Node(2, [third])
first = Node(1, [second])

ngraph = clone_graph(first)

print(first, ngraph)
print(first.val, ngraph.val)
print(first.neighbors, ngraph.neighbors)

traverse(first)
traverse(ngraph)
