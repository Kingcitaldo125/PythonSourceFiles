class Graph:
	def __init__(self):
		self.nodes = {}

	def _add_neighbors(self, node, neighbors):
		for n in neighbors:
			if n not in self.nodes:
				self.add_node(n)
			self.nodes[node].add(n)

	def add_node(self, node, neighbors=set([])):
		if node not in self.nodes:
			self.nodes[node] = set([])
		self._add_neighbors(node, neighbors)

	def _tsort_help(self, nodes, visited, node):
		visited.add(str(node))

		for nde in self.nodes[node]:
			if str(nde) in visited:
				continue
			self._tsort_help(nodes, visited, nde)

		nodes.append(str(node))

	def topological_sort(self, start):
		if start not in self.nodes:
			raise Exception(f"Cannot find start node {start} in graph.")

		nodes = []
		visited = set([])

		self._tsort_help(nodes, visited, start)

		return nodes

graph = Graph()

graph.add_node("A",{"B","C","D"})
graph.add_node("B",{"E","F"})
graph.add_node("C",{"G"})
graph.add_node("D",{"G","H"})
graph.add_node("E")
graph.add_node("F",{"I","J"})
graph.add_node("G",{"K"})
graph.add_node("H")
graph.add_node("I")
graph.add_node("J", {"K"})
graph.add_node("K")

print(graph.topological_sort("A"))
