import heapq

def dijk(graph, start, end):
	mqueue = []
	visited = set()
	path = []
	distances = {i:9999 for i in graph.keys()}
	last = None

	mqueue.insert(0, (0, start))
	visited.add(start)
	distances[start] = 0

	while len(mqueue) > 0:
		itm = heapq.heappop(mqueue)
		node_dist = itm[0]
		node_name = itm[1]

		print(f'visited {node_name}')

		if last and last not in path:
			path.append(last)

		if node_name == end:
			path.append(end)
			break

		for neigh in graph[node_name]:
			neigh_dist = neigh[0]
			neigh_name = neigh[1]

			distances[neigh_name] = min(distances[neigh_name], node_dist + neigh_dist)

			if neigh_name not in visited:
				last = node_name
				visited.add(neigh_name)
				heapq.heappush(mqueue, (distances[neigh_name], neigh_name))

	return distances, path

def main():
	graph = {
		'A': {(1, 'B'),(2, 'C')},
		'B': {(3, 'C'), (4, 'D'), (5, 'E')},
		'C': {(2, 'A'), (3, 'B')},
		'D': {(2, 'E')},
		'E': {(2, 'D')},
	}

	#'''
	dist, path = dijk(graph, 'A', 'E')
	print(f'dist, path {dist}, {path}')
	#'''

if __name__ == "__main__":
	main()
