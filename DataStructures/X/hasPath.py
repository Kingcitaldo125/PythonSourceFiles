def bfs(graph, start, target):
	mqueue = [start]

	while(len(mqueue) > 0):
		itm = mqueue.pop()

		if itm == target:
			return True

		print(f'itm: {itm}')

		for n in graph[itm]:
			mqueue.insert(0,n)

	return False

def dfs(graph, node, target, visited):
	print(node)

	if node == target:
		return True

	for n in graph[node]:
		if n not in visited:
			visited.add(n)
			return dfs(graph, n, target, visited)

	print(f'below {node}')
	return False
