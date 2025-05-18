# leetcode 684

def find(n, parents):
	if parents[n] == n:
		return n

	return find(parents[n], parents)

def union(n,edges):
	parents = list(range(n + 1))

	for e in edges:
		first = e[0]
		second = e[-1]

		print(f"first {first}")
		print(f"second {second}")

		f = find(first, parents)
		s = find(second, parents)

		if f == s:
			return [first,second]

		parents[s] = f
		print(f"parents {parents}")

	return [-1,-1]

n = 4
edges = [[1,2], [3,4]]

res = union(n,edges)
print(f"res {res}")
