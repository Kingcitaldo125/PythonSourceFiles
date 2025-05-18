class Trie():
	def __init__(self):
		self.mmap = {}

	def print_map_help(self, xmap, idx):
		node = xmap
		print("")
		for i,j in node.items():
			print("-"*idx,i,j,end=' ')
			self.print_map_help(node[i], idx+1)

	def print_map(self):
		self.print_map_help(self.mmap,0)

	def add(self, word):
		node = self.mmap
		for w in word:
			if w in node:
				node = node[w]
				continue
			node[w] = {}
			node = node[w]

	def search_help(self, word, node):
		if len(word) == 0:
			return True
		if len(word) == 1:
			if word[0] == '.' and self.mmap != {}:
				return True
			return word[0] in node

		if word[0] == '.':
			ires = 0
			for k,v in node.items():
				lres = self.search_help(word[1:], node[k])
				ires |= 1 if lres else 0
			return lres == 1
		elif word[0] not in node:
			return False
		return self.search_help(word[1:], node[word[0]])

	def search(self, word):
		return self.search_help(word, self.mmap)

	def starts_with(self, prefix):
		node = self.mmap
		for p in prefix:
			if p not in node:
				return False
			node = node[p]
		return True

trie = Trie()

trie.add("bad")
trie.add("dad")
trie.add("mad")

#trie.print_map()

print("pad",trie.search("pad"))
print("bad",trie.search("bad"))
print("bad",trie.starts_with("bad"))
